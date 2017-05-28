#include <SoftwareSerial.h>

SoftwareSerial mpuSerial(8, 6);//Define Software Serial Rx,Tx
SoftwareSerial serverSerial(10, 9);


void setup(){
 Serial.begin(9600);//Begin Serial Connection
 serverSerial.begin(9600);
 mpuSerial.begin(9600);// Very imp....Mpu after server begin. Dont know why??
 pinMode(13, OUTPUT);

    
}

void loop() {
if(mpuSerial.available() > 0){
char inChar = (char)mpuSerial.read();
    // add it to the inputString:
    //serverSerial.print(inChar);
    Serial.print(inChar);
}

if(serverSerial.available() > 0){  // To check if PC has sent any data
       char ch=serverSerial.read();
          
          if(ch=='s')
       {
        Serial.write(94); //Reverse direction
        Serial.write(222);        

        }
        
          if(ch=='w')
       {   
        Serial.write(30);   //Move in the forward direction
        Serial.write(158);
       }
         
         if(ch=='a')
       {
        Serial.write(30);// Turn Left
        //delay(7);
        Serial.write(222);
        //delay(7);
        }

        
        if(ch=='d')
       {
        Serial.write(94);//Turn Right
        //delay(7);
        Serial.write(135);
        //delay(7);
        }
        
        if(ch=='z')
       {
        Serial.write(0);//Stop both Motors
        delay(2);
        Serial.write(0);
        }
 }

}

