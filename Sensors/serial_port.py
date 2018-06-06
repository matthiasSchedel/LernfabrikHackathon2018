from time import sleep
import serial
import numpy as np
import json
import serial
import sys
import time
import datetime
import matplotlib.pyplot as plt
import scipy.special as sp
import requests


def fGauss(x, mu=70., sigma=10.):
       # Gauss distribution
    return (np.exp(-(x-mu)**2/2./sigma**2)/np.sqrt(2.*np.pi)/sigma)

def simulated_singlevent():
       mean_data=10
       # Crate random number according to poission distribution
       simulated_value=np.random.poisson(mean_data)


       if(True):
              x=np.linspace(0,1.5*mean_data,1000)
              plt.plot(x,fPoisson(x,mean_data), label=" Measurement distribution")
              plt.errorbar(simulated_value, 0.1, xerr=1,yerr=0.02,linestyle="", marker="o",markersize="8",color="r",label="Measured data")
              plt.xlabel("Data")
              plt.ylabel("Probability")
              plt.legend()
              plt.savefig("out.png")
              plt.close()
       return simulated_value


       
def fPoisson(x, mu):
       # Distribution of signle data events
       k=np.around(x)
       return (mu**k)/np.exp(mu)/sp.gamma(k+1.)


def get_data(baudrate=9600,port="/dev/ttyACM0"):

    # Switching tool to handle data
        switch=True
        name=[]
        input_value=[]

        
        if len(sys.argv) == 3:
            ser = serial.Serial(sys.argv[1], sys.argv[2])
        else:
            ser = serial.Serial(port, baudrate)


        # enforce a reset before we really start
        ser.setDTR(1)
        time.sleep(0.25)
        ser.setDTR(0)
        
        while(True) :
            ''' Still need a stoppting  criteria'''
            input_value=ser.readline().rstrip()
    
            sys.stdout.flush()
            if(input_value=="simulate"):
                input_value=simulated_singlevent()
               
            if(input_value=="end_measurement"):
                return 0

            #Evenutally delete
            #r = requests.urlopen("http://172:18.04:3000/hallo2").read()
            print input_value
            
        
for i in range(0,5):
    print "product " +str(i)
    get_data()
    sleep(1)
    
