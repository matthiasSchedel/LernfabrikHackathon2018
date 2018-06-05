''' This programm creates a Python to json device'''
import numpy as np
import json
import serial
import sys
import time
import datetime
import matplotlib.pyplot as plt
import scipy.special as sp

class SensorData:
    ''' Contains methods of reading datas
        Create Json files
        Simulate Data
        '''

    # define parameter for json output
    product_id=[]
    error_messages=[]
    measured_property=[]
    data=[]
    
    
    def __init__(self,id_nummer,version):
        # Initialise key arguments for class
        self.id=id_nummer
        self.version=version

        

    def get_data(self,baudrate=9600,port="/dev/ttyACM0"):

    # Switching tool to handle data
        switch=True
        name=[]
        input_value=[]


        if len(sys.argv) == 3:
            ser = serial.Serial(sys.argv[1], sys.argv[2])
        else:
            print "# Please specify a port and a baudrate"
            print "# using hard coded defaults " + port + " " + str(baudrate)
            ser = serial.Serial(port, baudrate)


        # enforce a reset before we really start
        ser.setDTR(1)
        time.sleep(0.25)
        ser.setDTR(0)

        while(ser.readline().rstrip()!="end_measurement") :
            ''' Still need a stoppting  criteria'''
        # get the measured values and remove not needed string codes
            if(switch):
                # get the measured values and remove not needed string codes
                input_value=np.append(input_value,ser.readline().rstrip())      
                switch=False
            else:
                u=ser
                name=np.append(name,ser.readline().rstrip())
                switch=True
            sys.stdout.flush()
        ''' Create switch for getting the data'''

        
        if(input_value=='simulate'):
            # case single event
            s_data=SensorData.simulated_singleevent(self)
            self.data.append(s_data)
            # case simulated measurement
            return s_data
        if(input_value=="simulate_series"):
            # case measurement
            s_data=SensorData.simulated_simulated_measurement(self)
            self.data.append(s_data)
            # case simulated measurement
            return s_data
            
          
        else:
            self.data.append(input_value)
        
            
        return input_value






            
            
    def timestamp(self):
            # import time and get each measurement 
            ts=time.time()
            time_stamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            return time_stamp




        
        
    def create_json(self):
        # Simulate event
        #SensorData.get_data()
        json_object=json.dumps({'Version': self.version,'Product id': self.id,'Timestamp': SensorData.timestamp(self), 'Humidity': SensorData.data,'Error messages':self.error_messages}, sort_keys=True,indent=5, separators=(',', ': '))
        return json_object




        
        
    def simulated_singleevent(self):
        mean_data=10
        # Crate random number according to poission distribution
        simulated_value=np.random.poisson(mean_data)
        self.data.append(simulated_value)


        if(True):
            x=np.linspace(0,1.5*mean_data,1000)
            plt.plot(x,SensorData.fPoisson(self,x,mean_data), label=" Measurement distribution")
            plt.errorbar(simulated_value, 0.1, xerr=1,yerr=0.02,linestyle="", marker="o",markersize="8",color="r",label="Measured data")
            plt.xlabel("Data")
            plt.ylabel("Probability")
            plt.legend()
            plt.savefig(str(self.product_id)+str(self.version)+".png")
            plt.close()
        if(simulated_value<8):
            self.error_messages.append(" Measurement out of range during process")

        return simulated_value




    def f(self,x,a=1,b=0.5):
        # define simulated function
        return (a*x+b)





    def fPoisson(self,x, mu):
        # Distribution of signle data events
        k=np.around(x)
        return (mu**k)/np.exp(mu)/sp.gamma(k+1.)



    def fGauss(self,x, mu=70., sigma=10.):
       # Gauss distribution
        return (np.exp(-(x-mu)**2/2./sigma**2)/np.sqrt(2.*np.pi)/sigma)



    def simulated_measurement(self):

        # Number of events
        N=100

        # create x_data
        x=(np.linspace(0,10,N))
        yerr=np.random.randn(N)
        y=SensorData.f(self,x)+yerr
        if(False):
            # eventually do plot
            plt.plot(x,y, linestyle="", marker='o', label="Simulated data")
            plt.legend()
            plt.show()
            plt.savefig(str(self.product_id)+str(self.version)+".png")
            plt.close()
        if(np.random.randint(size=(0,2))==1):
            self.error_messages.append(" Something wrong with your criteria")
        
        return yerr


        

# Get id and version from scanning

d1=SensorData(1,1)
print d1.create_json()





