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


### folloed by optional arguments
-lenght int anomalyLength\
-factor int anomalyfactor\ 
-n int  anomalyRepetitions

The default lenght is 10 and number of repertitions 1. The factor depends 
When the first data row only contains numerical arguments there is assumed to be no header.
### plotting and saving arguments:
-plot\
-legendoff\
-save filename  


All the arguments try to match if only the beginning is given i.e., **-t** instead of **-type** or **a** insteaf of **amplitude_shift**
### Examples:


$python .\terminal.py -d .\Data\stock10k.data -col 2 -type a -n 12 -l 100 -sa out -t d -n 3  -l 200 -plot -t g -n 4
