#include <Servo.h>
#include <TimerThree.h>
Servo join[6]; 
String str;
char x [8]; 
int deg [6];
int cnt = 0;
int ini[6]={180,90,90,90,90,90};
float cur [6] = {110,90,90,90,90,90};
int d_theda[6];
float add_value[6];
bool initial_state = true;
bool state = false;
void setup() {
  for (int k = 0 ; k<6 ; k ++){
    join[k].attach(k+2);
    join[k].write(ini[k]);
  }
Serial.begin(38400);
Timer3.initialize(150);
Timer3.attachInterrupt(servo_control);
}

void loop() {
  
       for (int u = 0 ; u < 6 ; u++)
     {if(initial_state ==true){
       join[u].write(ini[u]);//寫入角度
       //Serial.println(ini[u]);
     }
     if(initial_state !=true){
       join[u].write(deg[u]);//寫入角度
       //Serial.println(deg[u]);
     }
       }

 }
 void servo_control(void)
{

   //if (Serial.available()){
    initial_state = false;
    int inChar = Serial.read();
    //Serial.println(inChar);
    if(inChar != -1){
      //Serial.println(inChar);
      Serial.println(deg[4]);
    if(state == true){
      deg[cnt]=inChar;
      cnt++;
    }
    if(inChar == 255){//開始碼
      state = true;
    }
    if(inChar ==238){//結束碼 
      state = false;
      cnt = 0;
     //Serial.println("end");  
   }
    }
}

  
