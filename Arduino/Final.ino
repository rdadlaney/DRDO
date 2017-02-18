#include <SoftwareSerial.h>

SoftwareSerial mySerial(8, 5);//Define Software Serial Rx,Tx

void setup(){
 Serial.begin(9600);//Begin Serial Connection
 mySerial.begin(9600);
 pinMode(10, OUTPUT);
 pinMode(9, OUTPUT);
 pinMode(7, OUTPUT);
    
}

void loop(){
 if(mySerial.available() > 0){  // To check if PC has sent any data
       char a=mySerial.read();
          if(a=='w')
       {        
        digitalWrite(10, HIGH);   //LED indicator
        delay(100);              
        digitalWrite(10, LOW);    
        delay(100);
        Serial.write(30);   //Move in the forward direction
        delay(10);
        Serial.write(158);
        delay(10);
        }
         if(a=='s')
       {
        Serial.write(94); //Reverse direction
        delay(10);
        Serial.write(222);
        delay(10);
        }
         
         if(a=='a')
       {
        Serial.write(30);// Turn Left
        delay(10);
        Serial.write(222);
        delay(10);
        }
        if(a=='d')
       {
        Serial.write(94);//Turn Right
        delay(10);
        Serial.write(158);
        delay(10);
        }
        if(a=='z')
       {
        Serial.write(0);//Stop both Motors
        delay(100);
        }
 }
}
