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
  
//  moveAllServos(160);
  closeAllBins();
  delay(1000);
  servo1Drop();
  servo2Drop();
  servo3Drop();
  servo4Drop();
  delay(1000);
//  openBin1();
//  delay(1000);
//  openBin2();
//  delay(1000);
//  openBin3();
//  delay(1000);
//  openBin4();
//  delay(1000);
  //closeAllBins();
//  servo[0].write(10);
  digitalWrite(motorForward, HIGH);
  digitalWrite(motorBackward, LOW);
 // analogWrite(motorPower, 0); // can be from 0 - 255
//  launchCard();
}

void loop() {
  if (Serial.available()) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    if (incomingByte == 49) {
      sendToBin1();
    }
    if (incomingByte == 50) {
      sendToBin2();
    }
    if (incomingByte == 51) {
      sendToBin3();
    }
    if (incomingByte == 52) {
      sendToBin4();
    }
    if (incomingByte == 53) {
      sendToBin5();
    }
  }

  
  delay(100);
  //moveDCMotor(255, "backward");
   //servo[0].write(20);
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

void launchCard() {
  moveDCMotor(255, "forward");
  delay(300);
  stopDCMotor();
  delay(500);
}

void moveAllServos(int pos) {
  for (int i = 0; i < 5; i ++) {
    servo[i].write(pos);
  }   
}

void servo1Close() {
  servo[0].write(160);
}

void servo2Close() {
  servo[1].write(158);
}

void servo3Close() {
  servo[3].write(165);
}

void servo4Close() {
  servo[2].write(145);
}

void servo1Drop() {
  servo[0].write(87);
}

void servo2Drop() {
  servo[1].write(87);
}

void servo3Drop() {
  servo[3].write(87);
}

void servo4Drop() {
  servo[2].write(90);
}

void openBin1() {
  servo1Drop();
  servo2Close();
  servo3Close();
  servo4Close();
}

void openBin2() {
  servo1Close();
  servo2Drop();
  servo3Close();
  servo4Close();
}

void openBin3() {
  servo1Close();
  servo2Close();
  servo3Drop();
  servo4Close();
}

void openBin4() {
  servo1Close();
  servo2Close();
  servo3Close();
  servo4Drop();
}

void closeAllBins() {
  servo1Close();
  servo2Close();
  servo3Close();
  servo4Close();
}

void sendToBin1() {
  openBin1();
}

void sendToBin2() {
  openBin2();
}

void sendToBin3() {
  openBin3();
}

void sendToBin4() {
  openBin4();
}

void sendToBin5() {
  closeAllBins();
}

