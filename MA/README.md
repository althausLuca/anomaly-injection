# Anomaly injection for Time Series  
Support multiple injections of amplitude shoft, distortion , growth change and extrem values of a single data column containing numerical values.


## Prerequisites
To run the programm you need Python with pandas and matplotlib installed

- For ubuntu 18 or 20
- Clone this repository.
- in the folder run : 


## Execution
```bash
    $ cd my_injcetion
    $ sudo apt install python-dev
    $ sudo apt install python3-pip
    $ pip install pandas
    $ pip install matplotlib
    $ python3 terminal.py [arguments]
```

### data Arguments
-data  yourdatapath 


### optional arguments 
-datacol  default: 0 has to be an index \
-seperator default: ","

The supported data files are in csv style the first line is disgarded automatically if intcontains string values.

## Anomalies
-type [amplitude_shift 
distortion ,
growth_change ,
extreme]


### Followed by optional arguments
-lenght int anomalyLength\
-factor int anomalyfactor\ 
-n int  anomalyRepetitions

The default lenght is 10 and number of repertitions 1. The factor depends 
When the first data row only contains numerical arguments there is assumed to be no header.
### Plotting and saving arguments:
-plot\
-legendoff\
-save filename  

The file will be saved into the Data/generated folder unless specified otherwise


All the arguments try to match if only the beginning is given i.e., **-t** instead of **-type** or **a** insteaf of **amplitude_shift**
### Examples:

$python3 terminal.py -data Data/stock10k.data -plot -col 2 -type  amplitude_shift -type distortion -length 30 -factor 6 -n 6

$ python3 terminal.py -data Data/stock10k.data -plot -col 2 -t a -t d -l 30 -f 6 -n 6

