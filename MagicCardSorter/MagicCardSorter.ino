#include <Servo.h>

Servo servo[8];
#define motorPower 9
#define motorForward 7
#define motorBackward 6

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
  
  closeAllBins();
//  delay(1000);
//  servo1Drop();
//  servo2Drop();
//  servo3Drop();
//  servo4Drop();
//  delay(1000);
//  openBin1();
//  delay(1000);
//  openBin2();
//  delay(1000);
//  openBin3();
//  delay(1000);
//  openBin4();
//  delay(1000);
//  closeAllBins();
//  digitalWrite(motorForward, HIGH);
//  digitalWrite(motorBackward, LOW);
//  analogWrite(motorPower, 150); // can be from 0 - 255
//  moveDCMotor(255, "forward");
  delay(1000);
  launchCard();
}

void loop() {
//  if (Serial.available()) {
//    // read the incoming byte:
//    incomingByte = Serial.read();
//    
//    if (incomingByte == 49) {
//      sendToBin1();
//    }
//    if (incomingByte == 50) {
//      sendToBin2();
//    }
//    if (incomingByte == 51) {
//      sendToBin3();
//    }
//    if (incomingByte == 52) {
//      sendToBin4();
//    }
//    if (incomingByte == 53) {
//      sendToBin5();
//    }
//  }
//  closeAllBins();
//  digitalWrite(motorForward, LOW);
//  digitalWrite(motorBackward, LOW);

  delay(500);
  launchCard();
}

void sendToBin1() {
  openBin1();
  launchCard();
}

void sendToBin2() {
  openBin2();
  launchCard();
}

void sendToBin3() {
  openBin3();
  launchCard();
}

void sendToBin4() {
  openBin4();
  launchCard();
}

void sendToBin5() {
  closeAllBins();
  delay(400);
  launchCard();
}

void launchCard() {
  delay(400);
  moveDCMotor(255, "forward");
  delay(700);
  stopDCMotor();
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

void moveDCMotor(int power, String orientation) {
  analogWrite(motorPower, power); // can be from 0 - 255
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


