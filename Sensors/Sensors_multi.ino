// Input for differnet measurements


// Temperature mesurement
#include "DHT.h" //DHT Bibliothek laden
#define DHTPIN 2 //Der Sensor wird an PIN 2 angeschlossen    
#define DHTTYPE DHT11    // Es handelt sich um den DHT11 Sensor

// Import class for measurement
DHT dht(DHTPIN, DHTTYPE); //Der Sensor wird ab jetzt mit „dth“ angesprochen




// Define Parameters for linear-Hall

const int SIGNPIN=A0;
const float GAUSS_PER_STEP=2.713;
float rawValue=0.0;
float value=0.0;
float mTesla=0.0;
float zeroLevel=538.0;
const float GAUSS_IN_TESLA=1./10;





// Getting data from pin
int eventpin= 4;
// Variable for start booting

// Variable for switch
int measurement;

int aufruf=0;


void setup() {
  Serial.begin(9600); //Serielle Verbindung starten
  pinMode(eventpin,INPUT);


  // Start temperature sensor
  dht.begin(); //DHT11 Sensor starten
}

void loop() {

  measurement=digitalRead(eventpin);


  if(aufruf==3 and measurement==HIGH ){
      
    Serial.println("simulate"); //die Dazugehörigen Werte anzeigen
    delay(2000);
    aufruf++;
    }
    measurement=digitalRead(eventpin);

    if(aufruf==2 and measurement==HIGH ){
      Serial.println("simulate"); //die Dazugehörigen Werte anzeigen
      delay(2000);
      aufruf++;
    }
  measurement=digitalRead(eventpin);

    if(aufruf==1 and measurement==HIGH){
  float Luftfeuchtigkeit = dht.readHumidity(); //die Luftfeuchtigkeit auslesen und unter „Luftfeutchtigkeit“ speichern
  float Temperatur = dht.readTemperature();//die Temperatur auslesen und unter „Temperatur“ speichern
  Serial.println(Luftfeuchtigkeit); //die Dazugehörigen Werte anzeigen
  delay(2000);
      aufruf++;
    }



  measurement=digitalRead(eventpin);

    if(aufruf==0 and measurement==HIGH){
    rawValue=analogRead(SIGNPIN)-zeroLevel;
  
    // Convert to real values
    
    value=rawValue*GAUSS_PER_STEP;
    mTesla=value*GAUSS_IN_TESLA;
  
    // print values
    
    Serial.println(mTesla);
    delay(2000);
        aufruf++;
    }


      measurement=digitalRead(eventpin);

    if(aufruf==4 and measurement==HIGH){
      Serial.println("simulate"); //die Dazugehörigen Werte anzeigen
      delay(2000);
      aufruf++;
    }

    if(aufruf==5){

      Serial.println("end_measurement");
      delay(10000);
      
    }


    

    


  

}


