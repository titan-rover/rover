   /*
    * rosserial Publisher Example
  * Prints "hello world!"
     */
    
   // Use the following line if you have a Leonardo or MKR1000
   //#define USE_USBCON

#include <Robojax_AllegroACS_Current_Sensor.h>
#include <ros.h> // for using arduino as ROS node
#include <std_msgs/Float32.h>

const int VIN_1 = A1; 
const int VIN_2 = A2;
const int VIN_3 = A3;
const int VIN_4 = A4;
const int VOLT_PIN = A5;
int relay_pin = 9;
const float VCC   = 6.1;// supply voltage
const int MODEL = 17;   // enter the model (see above list)
        //using ACS770x-200B
Robojax_AllegroACS_Current_Sensor Wheel_1(MODEL,VIN_1);
Robojax_AllegroACS_Current_Sensor Wheel_2(MODEL,VIN_2);
Robojax_AllegroACS_Current_Sensor Wheel_3(MODEL,VIN_3);
Robojax_AllegroACS_Current_Sensor Wheel_4(MODEL,VIN_4);
   
        
int offset =20;// set the correction offset value
//Current and Voltage value variables
float wheel1_current;
float wheel2_current;
float wheel3_current;
float wheel4_current;
float volt_val;
double voltage;

ros::NodeHandle nh;
   
std_msgs::Float32 w1_current;
std_msgs::Float32 w2_current;
std_msgs::Float32 w3_current;
std_msgs::Float32 w4_current;

ros::Publisher wheel1("wheel1", &w1_current);
ros::Publisher wheel2("wheel2", &w2_current);
ros::Publisher wheel3("wheel3", &w3_current);
ros::Publisher wheel4("wheel4", &w4_current);
   
void setup(){

  pinMode(relay_pin,OUTPUT);
  nh.initNode();
  nh.advertise(wheel1);
  nh.advertise(wheel2);
  nh.advertise(wheel3);
  nh.advertise(wheel4);
  
  //Serial.begin(9600);
}
   
void loop(){
  volt_val = analogRead(A0);// read the input
  voltage = map(volt_val,0,1023, 0, 2500) + offset;
  voltage /=100;
  wheel1_current = Wheel_1.getCurrentAverage(300);
  wheel2_current = Wheel_2.getCurrentAverage(300);
  wheel3_current = Wheel_3.getCurrentAverage(300);
  wheel4_current = Wheel_4.getCurrentAverage(300);

  
  w1_current.data = wheel1_current;
  wheel1.publish(&w1_current);
  w2_current.data = wheel2_current;
  wheel2.publish(&w1_current);
  w3_current.data = wheel3_current;
  wheel3.publish(&w3_current);
  w4_current.data = wheel4_current;
  wheel4.publish(&w4_current);
  if (voltage <= 19 && voltage >= 2){
    digitalWrite(8, HIGH);
    
  }
  else if(voltage < 2){// if the battery is this low, killswitch was hit.
    digitalWrite(8, LOW);
  }
  else{
    digitalWrite(8, LOW);
  }
  
  nh.spinOnce();
  delay(1000);
}
