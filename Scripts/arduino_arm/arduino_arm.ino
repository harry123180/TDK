#include <Servo.h>
#define LED 13
String str;
Servo myservo1; 
Servo myservo2; 
int deg1= 90;
int deg2 = 10;
void setup() {
  pinMode(LED, OUTPUT);
  myservo1.attach(2); 
  myservo2.attach(3);
  Serial.begin(9600);
  myservo1.write(0);
  myservo2.write(10);
}

void loop() {
  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
 
    if (str == "ADD_A") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(LED, HIGH);     // 開燈
        Serial.println(deg1); // 回應訊息給電腦
        for (int i = 0 ; i < 1 ; i++)
        {
          deg1 = deg1+1;
          myservo1.write(deg1);
          delay(20);
        }
         
    } else if (str == "ADD_B") {
        digitalWrite(LED, LOW);
        Serial.println(deg1 );
         
        for (int i = 0 ; i <1 ; i++)
        {
          deg2 = deg2+1;
          myservo2.write(deg2);
          delay(20);
          
        }
    }
    else if (str == "MIN_A") {
        digitalWrite(LED, LOW);
        Serial.println("MIN_A");
        for (int i = 0 ; i <1 ; i++)
        {
          deg1 = deg1-1;
          myservo1.write(deg1);
          delay(20);
        }
    }
    else if (str == "MIN_B") {
        digitalWrite(LED, LOW);
        Serial.println("MIN_B");
       for (int i = 0 ; i <1 ; i++)
        {
          deg2 = deg2-1;
          myservo2.write(deg2);
          delay(20);
        }
    }
  }
}
