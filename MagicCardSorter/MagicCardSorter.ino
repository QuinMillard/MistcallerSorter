#include <Servo.h>

Servo servo[8];
#define motorPower 6
#define motorForward 8
#define motorBackward 9

int incomingByte = 0;   // for incoming serial data


int pos = 0;  

void setup() {
  Serial.begin(9600);
  
  for (int i = 0; i < 5; i ++) {
    servo[i].attach(i + 15);
  }
  pinMode(motorPower, OUTPUT);
  pinMode(motorForward, OUTPUT);
  pinMode(motorBackward, OUTPUT);

  //digitalWrite(motorForward, HIGH);
//  digitalWrite(motorBackward, LOW);
 // analogWrite(motorPower, 0); // can be from 0 - 255
}

void loop() {
  if (Serial.available()) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    if (incomingByte == 49) {
      for (pos = 0; pos <= 180; pos += 1) { 
        moveAllServos(pos);    
        delay(15);                       
      }
    }
  }
  delay(100);
  //moveDCMotor(255, "backward");
//  for (pos = 0; pos <= 180; pos += 1) { 
//    moveAllServos(pos);    
//    delay(15);                       
//  }
//  for (pos = 180; pos >= 0; pos -= 1) { 
//    //moveAllServos(pos);            
//    delay(15);                     
//  }
}

void moveDCMotor(int power, String orientation) {
  if ( orientation == "forward" ) {
    digitalWrite(motorBackward, LOW);
    digitalWrite(motorForward, HIGH);
  }
  if ( orientation == "backward" ) {
    digitalWrite(motorForward, LOW);
    digitalWrite(motorBackward, HIGH);
  }
}

void stopDCMotor() {
  digitalWrite(motorForward, LOW);
  digitalWrite(motorBackward, LOW);
}

void moveAllServos(int pos) {
  for (int i = 0; i < 5; i ++) {
    servo[i].write(pos);
  }   
}

