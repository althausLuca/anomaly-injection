import argparse
import sys
import pandas as pd
import numpy as no

from Injector import *

parser = argparse.ArgumentParser()
parser.add_argument("-data","-d" ,nargs=1, type=str ,  required=True)
parser.add_argument('-sep',nargs=1, default=[','])
parser.add_argument('-datacol',"-col" , nargs=1, default=[0] ,type=int )

parser.add_argument('-save',  nargs=1, type=str , default=False )
parser.add_argument('-plot', action='store_true')
parser.add_argument('-whitoutlegend', action='store_false')
parser.add_argument('-anomalydetails', action='store_true')

#anomalies
parser.add_argument("-type" ,nargs=1, type=str , action="extend")
parser.add_argument("-length" ,nargs=1, type=int , action="extend")
parser.add_argument("-factor", nargs=1, type=int,  action="extend")
parser.add_argument("-number_of_iterations" ,nargs=1, type=int,  action="extend")
parser.add_argument("-direction", nargs=1, type=str,  action="extend",required=False)
parser.add_argument("-index", nargs=1, type=int,  action="extend",required=False)

args = parser.parse_args()


data = pd.read_csv(args.data[0], sep=args.sep[0] , header = None)
header = None
#check if first data col has string
for i in data.iloc[0]:
    if isinstance(i, str):
        header = 0

data = pd.read_csv(args.data[0], sep=args.sep[0] , names=list(range(data.shape[1])) , header = header)
print(data.head(4))

injector = Anomalygenerator(np.array(data[int(args.datacol[0])],dtype=np.float64))


anomalies = []
current_dict = {}
lastkey = None

for x in sys.argv[1:]:
    if x[0] == "-":
        if x[1] == "t":
            anomalies.append(current_dict)
            current_dict = dict()
        try:
            lastkey = [s for s in vars(args).keys() if  s.startswith(x[1:])][0]
        except:
            pass
    else:
        current_dict[lastkey] = x

anomalies.append(current_dict)
anomalies = anomalies[1:]

for anom in anomalies:
    type = anom["type"]
    if type[0] == "a":
        #length=10, factor=8, starting_index=None,  number_of_ranges=1 , std_range=(-10, 10),directions=[1, -1]
        injector.add_amplitude_shift(starting_index = int(anom.get("index",0)) or None, length=int(anom.get("length",10)),factor=int(anom.get("factor",8)),number_of_ranges =int(anom.get("number_of_iterations",1)))
    elif type[0] == "d":
        injector.add_distortion(starting_index = int(anom.get("index",0)) or None, length=int(anom.get("length",10)),factor=int(anom.get("factor",8)),number_of_ranges =int(anom.get("number_of_iterations",1)))
    elif type[0] == "g":
        injector.add_growth(starting_index = int(anom.get("index",0)) or None, length=int(anom.get("length",10)),factor=int(anom.get("factor",8)),number_of_ranges =int(anom.get("number_of_iterations",1)))
    elif type[0] == "e":
        injector.add_extreme_point(starting_index = int(anom.get("index",0)) or None, length=1,factor=int(anom.get("factor",8)),number_of_ranges =int(anom.get("number_of_iterations",1)))
    else:
        print(f'anomaly type {type[0]} not recognized')



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


if(args.plot):
    injector.plot(legend=args.whitoutlegend)

if(args.save):
    injector.save(args.save[0])

