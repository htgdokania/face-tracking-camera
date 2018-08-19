#include<Servo.h>

Servo myservo1;
Servo myservo2;

int change=0;
int initial_angle=90;
int final_angle=90;
char buf[10];
//string str()
void setup() 
{
      myservo1.attach(6);
      myservo2.attach(9);
      Serial.begin(9600);
      Serial.println("Connection established...");
      myservo1.write(final_angle);
      myservo2.write(final_angle);
}

void loop() 
{ change=0;
  buf[0]=0; buf[1]=0; buf[2]=0; buf[3]=0;
  if(Serial.available())
  {
    for (int i=0;i<8;i++)
      buf[i]=Serial.read();
  }
  //string str();
  if(buf[0]=="-")
    change=atoi(buf)*-1;
  else
    change=atoi(buf);
  
  Serial.println("change=");
  Serial.println(change);
  change*=10;
  if((final_angle+change)<=180 && (final_angle+change)>=0)
      final_angle+=change;
  
  Serial.println("final angle=");
  Serial.println(final_angle);
  myservo1.write(final_angle);
  myservo2.write(final_angle);

}
