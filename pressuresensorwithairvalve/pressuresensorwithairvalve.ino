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
if(leftforce > 500)
{
  Serial.println("left mid stance is right swing");
  digitalWrite(6,HIGH);
}
else
{
  Serial.println("left mid stance finish");
  digitalWrite(6,LOW);
}
if(rightforce > 700)
{
  Serial.println("right mid stance is left swing");
  digitalWrite(3,HIGH);
}
else
{
    Serial.println("right mid stance finish");
    digitalWrite(3,LOW);
}
delay(1);
}

