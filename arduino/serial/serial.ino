#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62

void setup() {

  pinMode(Y_STEP_PIN,OUTPUT); 
  pinMode(Y_DIR_PIN ,OUTPUT);
  pinMode(Y_ENABLE_PIN ,OUTPUT);
  pinMode(Z_STEP_PIN,OUTPUT); 
  pinMode(Z_DIR_PIN ,OUTPUT);
  pinMode(Z_ENABLE_PIN ,OUTPUT);

  Serial.begin(9600);
  while (! Serial);
  Serial.println("hols");
}

void loop() {

  if (Serial.available()) {
    switch (int (Serial.read())) {

      case '0':
      digitalWrite(Y_DIR_PIN ,HIGH); 
          for(int y = 0; y < 50; y++) {
            digitalWrite(Y_STEP_PIN,HIGH); 
            delayMicroseconds(50); 
            digitalWrite(Y_STEP_PIN,LOW); 
            delayMicroseconds(50);
  }
        break;
      case '1':
      digitalWrite(Y_DIR_PIN ,LOW); 
          for(int y = 0; y < 50; y++) {
            digitalWrite(Y_STEP_PIN,HIGH); 
            delayMicroseconds(50); 
            digitalWrite(Y_STEP_PIN,LOW); 
            delayMicroseconds(50);
  }
        break;
      case '2':
      digitalWrite(Z_DIR_PIN ,HIGH); 
          for(int y = 0; y < 50; y++) {
            digitalWrite(Z_STEP_PIN,HIGH); 
            delayMicroseconds(50); 
            digitalWrite(Z_STEP_PIN,LOW); 
            delayMicroseconds(50);
  }
        break;
      case '3':
      digitalWrite(Z_DIR_PIN ,LOW); 
          for(int y = 0; y < 50; y++) {
            digitalWrite(Z_STEP_PIN,HIGH); 
            delayMicroseconds(50); 
            digitalWrite(Z_STEP_PIN,LOW); 
            delayMicroseconds(50);
  }
        break;
    }
  }
}
