import argparse
import os
import pandas as pd
import numpy as np
from res.Injector import Anomalygenerator


parser = argparse.ArgumentParser()
parser.add_argument("-data","-d" ,nargs=2, type=str ,  required=True)
parser.add_argument('-sep',nargs=1, default=[','])

parser.add_argument('-save',  nargs="*", type=str , default=False )
parser.add_argument('-plotoff', action='store_false')
parser.add_argument('-withoutlegend', action='store_false')
parser.add_argument('-anomalydetails', action='store_true')

#anomalies
parser.add_argument("-type","-t" ,nargs=1, type=str )
parser.add_argument("-typex" ,"-tx",nargs=2, type=str , help = "types and parameter file")

args = parser.parse_args()


filepath = "Data/" + args.data[0].replace("Data/","")
files = []



if(os.path.isfile(filepath)):
    files = [filepath]
    print(files)
else:
    files = [  os.fsdecode(filepath+"/"+file)  for file in os.listdir(filepath) if  os.path.isfile(filepath+"/"+file)   ]
    print(files)

for file in files:
    data = pd.read_csv(file, sep=args.sep[0] , header = None)
    header = None
    #check if first data col has string
    for i in data.iloc[0]:
        if isinstance(i, str):
            header = 0

    data = pd.read_csv(file, sep=args.sep[0] , names=list(range(data.shape[1])) , header = header)
    print(data.head(4))


    types = None
    if args.typex is not None:
        injector = Anomalygenerator(np.array(data[int(args.data[1])],dtype=np.float64) ,args.typex[1] )
        types = args.typex[0]

    else:
        injector = Anomalygenerator(np.array(data[int(args.data[1])], dtype=np.float64))
        if args.type is not None:
            types = args.type[0]


    if types is not None:
        for anom in types.split(","):
            anom = anom[0].lower()
            if anom == "a":
                injector.add_amplitude_shift()
            elif anom == "d":
                injector.add_distortion()
            elif anom == "g":
                injector.add_growth()
            elif anom == "e":
                injector.add_extreme_point()
            else:
                print(f'anomaly type {anom} not recognized')

    if(args.anomalydetails):
        print()
        for key, value in injector.anomaly_infos.items():
            value = value.copy()
            value["index_range"] = ( value["index_range"][0] , value["index_range"][-1])
            try:
                value.pop("std_range")
            except:
                pass
            print(key,value , "\n")

    if(injector is not None):
        injector.repair_print()


    if(args.plotoff):
        injector.plot(legend=args.withoutlegend)

    print(args.save)
    if(args.save):
        print("aaaaaaa" , args.save)
        injector.save(args.save[0]+file.split("/")[-1])

    elif (args.save == []):
        print(file.split("/")[-1], args.save)
        injector.save(file.split("/")[-1])

