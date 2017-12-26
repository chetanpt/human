int rightpressurePin = A0;
int leftpressurePin = A1;
int rightforce;
int leftforce;

void setup() {
Serial.begin(9600);
pinMode(6, OUTPUT);
pinMode(3, OUTPUT);
}
void loop() {
  rightforce = analogRead(rightpressurePin);
  leftforce = analogRead(leftpressurePin);
  Serial.println(rightforce);
  Serial.println(leftforce);
  /*
   * Below if conditions detects the stance phase and support swing phase of contralateral limb.
   * i.e. mid stance on rigt limb will actuates pgm on left limb to support and assist swing phase. 
   */
  if(leftforce > 500 && rightforce < 700)
  {
    Serial.println("left mid stance is right swing");
    digitalWrite(6,HIGH);
  }
  else
  {
    Serial.println("left mid stance finish");
    digitalWrite(6,LOW);
  }
  if(rightforce > 700 && leftforce < 500)
  {
    Serial.println("right mid stance is left swing");
    digitalWrite(3,HIGH);
  }
  else
  {
      Serial.println("right mid stance finish");
      digitalWrite(3,LOW);
  }
  /*
   * Below code tries to detect no walking motion to void actuating pgm in such situation due gait 
   * detection code. e.g. sitting, standing or anytihng that results in not walking actuation of 
   * pgm is avoided. We try to do that by our first assumption i.e.
   * 1. When not walking both the sensors will return values greater than threshold. 
   */
   if(rightforce >700 && leftforce > 500)
   {
    Serial.println("user not moving");
    digitalWrite(3,LOW);
    digitalWrite(6,LOW);
   }
  delay(1);
}

