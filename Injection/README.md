# Anomaly injection for Time Series  
Support multiple injections of amplitude shift, distortion , growth change and extrem values of a single data column containing numerical values.


## Prerequisites
To run the programm you need Python with pandas and matplotlib installed

- For ubuntu 18 or 20
- Clone this repository.
- Execute:
```bash
    $ cd my_injcetion
    $ sudo apt install python-dev
    $ sudo apt install python3-pip
    $ pip install pandas
    $ pip install matplotlib
    $ python3 run.py [arguments]
```

### Data arguments
-data  yourdatapath 


#### optional data arguments 
-col  default: 0 ,has to be an integer
-seperator default: ","

The supported data files are in csv style format. The first line is disgarded automatically if it contains string values.

## Anomalies
-type [amplitude_shift,
distortion ,
growth_change ,
extreme]


### Followed by optional numerical arguments
-lenght int\
-factor numeric\
-n int\
-index int 

The default lenght is 10 and number of repetitions n is 1. The factor depends on the anomayly and the index is random.

### Plotting and saving arguments:
-plot\
-whitoutlegend\
-save filename\
-anomalydetails

The file will be saved into the Data/generated folder unless specified otherwise


All the arguments try to match if only the beginning is given i.e., **-t** instead of **-type** or **a** insteaf of **amplitude_shift**
### Examples:
```bash
$ python3 run.py -data Data/stock10k.data -plot -col 2 -type  amplitude_shift -type distortion -length 30 -factor 6 -n 6 -anomalydetails

$ python3 run.py -data Data/stock10k.data -plot -col 2 -t a -t d -l 30 -f 6 -n 6

$ python3 run.py -data Data/stock10k.data  -col 2 -t a -l 100  -save output -t a -t e -f 6 -p 
```

### Additional experimental run
The file runc.py has an optional argument -cont where one can continue working on the same anomalies and -delete to delete an anomalie by index

#### Example
```bash
$ python3 runc.py -data Data/stock10k.data -col 2 -cont
-t a -l 10 
-t d   
-t g
-an 

1 {'type': 'amplitude_shift', 'factor': 8, 'index_range': (690, 699)} 

2 {'type': 'distortion', 'factor': 8, 'index_range': (11270, 11279)} 

3 {'type': 'growth_change', 'factor': 8, 'index_range': (5064, 5073)} 

-delete 2 
-an 

1 {'type': 'amplitude_shift', 'factor': 8, 'index_range': (690, 699)} 

3 {'type': 'growth_change', 'factor': 8, 'index_range': (5064, 5073)} 

-save continiousoutput
exit
```


