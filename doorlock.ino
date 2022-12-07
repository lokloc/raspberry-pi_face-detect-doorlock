int data;
int relay = 4;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relay, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
    while(Serial.available())
  {
    data = Serial.read();
  }

  if(data == '1')
  {
 
    digitalWrite(relay,HIGH);
     
  }
  else if(data == '0')
  {
    digitalWrite(relay,LOW); 
  }
}


//int data;
//
//void setup() {
//  Serial.begin(9600);
//  pinMode(13, OUTPUT);
//  digitalWrite(13,LOW);
//}
//
//void loop() {
//  while(Serial.available()) {
//    data = Serial.read();
//  }
//
//  if (data == '1') {
//    digitalWrite(13,HIGH);
//  }
//  else if (data == '0') {
//    digitalWrite(13,LOW);
//  }
//}
