//Arduino基板ピン配置設定
int yamahasensor = 3;
int pressuresensor = 5;
int pwm = 11;
int onoff = 12;
//int INTERVAL = 5000;

//出力設定
void setup() {
  pinMode(pwm, OUTPUT);
  pinMode(onoff, OUTPUT);
  Serial.begin(9600);//シリアル信号用
  TCCR2B &= B11111000;//PWM周波数高速化3,11ピン
  TCCR2B |= B00000010;//PWM周波数高速化3,11ピン
}

void loop() {
  int analog_val1, analog_val2;
  long m, oldm, r, y, e, u, ud, ud1, kp, ke, ks, kd, y_max, y_min, m_max, m_min, a, b, c, d, inc;
  String message = "";
  
  d=4.0;    //定値
  kp=1.0;   //Pゲイン
  ke=10.0/d;//排気
  ks=15.0/d;//給気
  kd=1.0;   //Dゲイン
  
  /*-----------------------------------------------*/
  /*             キャリブレーション値              */
  
      y_max=681; //圧力350kPaのAD値
      m_max=200; //圧力最大時のストレッチャブルセンサのAD値
      y_min=240; //圧力最小時ののAD値
      m_min=600; //圧力最小時のストレッチャブルセンサのAD値
  
      a=y_max-y_min;
      b=m_max-m_min;
  
      inc=a/b;
      c=y_max-(m_max*inc);
  
  /*-----------------------------------------------*/
  
  
  analog_val1 = analogRead(yamahasensor);
  analog_val2 = analogRead(pressuresensor);
  
  /*-----------------------------------------------*/
  /*                   給気強く                    */
   
    m=analog_val1-oldm;
          
    if(m>0)
      {
        m=analog_val1;
      }
    else if(m<0)
      {
        m=analog_val1-25;
      }
    else{m=analog_val1-25;}
      oldm=analog_val1;
  
  /*-----------------------------------------------*/
  
  r = long(m*inc+c); //YAMAHAセンサAD値
  y = long(analog_val2); //圧力センサAD値
  
  e = r-y;
//    u=kp*(e+kd*(e-olde));   //PD制御
      u=kp*e;                 //P制御
//    olde=e;

//サーボ弁の制御
  if(u>30)//給気
    {
      digitalWrite(onoff,HIGH);
      ud=(u/d*ks)/d;
      if(ud>255){ud=255;}
      else{ ud=ud;}
        ud1 = (200+ud);//数値は172を基準//0～255まで調整可
        analogWrite(pwm,ud1);
    }
          
  else if(u<-30)//排気
    {
      digitalWrite(onoff,LOW);
      ud=((-u)/d*ke)/d;
      
      if(ud>255){ud=255;}
      else{ ud=ud;}
        ud1 = (172+ud);//数値は172を基準//0～255まで調整可
        analogWrite(pwm,ud1);
    }
    
  else//保持
    {
      ud1 = 0;
      analogWrite(pwm,ud1);
    }
    
  /*-----------------------------------------------*/
  /*                  シリアル表記                 */  
  
    message = "AD_value : ";
  
    Serial.print(message);
    Serial.print(r);
    Serial.print(message);
    Serial.print(y  );
    Serial.print(message);
    Serial.print(e);
    Serial.println("");
    
  /*-----------------------------------------------*/
  
}
