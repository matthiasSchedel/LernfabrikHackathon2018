// Getting data from pin
int eventpin= 4;
// Variable for start booting

// Variable for switch
int measurement;




// Import class for measurement

void setup() {
  Serial.begin(9600); //Serielle Verbindung starten
  pinMode(eventpin,INPUT);
}

void loop() {

  measurement=digitalRead(eventpin);
  if(measurement==HIGH){

  Serial.println("simulate"); //Im seriellen Monitor den Text und 
  Serial.println("simulate"); //die Dazugehörigen Werte anzeigen
  Serial.println("end_measurement");
  delay(1000);
  }
  

}
