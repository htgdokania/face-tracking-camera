#include<Servo.h>

const int led=13;
int c=180;
Servo myservo1;
int value=4;
void setup() 
{
      myservo1.attach(6);
      Serial.begin(9600);
      pinMode(led, OUTPUT);
      digitalWrite (led, LOW);
      Serial.println("Connection established...");
      Serial.println("\n enter value between 1 to 9 ");
      
}

void loop() 
{ 
  while (Serial.available())
    {
           value = Serial.read();
           //value=value-48;
           Serial.println(value);
           
    }
     
    myservo1.write(value*12);
    
}
