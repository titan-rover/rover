#ifndef _ROS_mobility_Status_h
#define _ROS_mobility_Status_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mobility
{

  class Status : public ros::Msg
  {
    public:
      typedef int8_t _source_type;
      _source_type source;
      typedef bool _armAttached_type;
      _armAttached_type armAttached;
      typedef int8_t _mode_type;
      _mode_type mode;
      typedef float _throttle_type;
      _throttle_type throttle;
      typedef const char* _arm_action_type;
      _arm_action_type arm_action;
      typedef const char* _wheel_action_type;
      _wheel_action_type wheel_action;
      typedef const char* _pysaber_mode_type;
      _pysaber_mode_type pysaber_mode;
      typedef const char* _pysaber_cmd_type;
      _pysaber_cmd_type pysaber_cmd;
      typedef const char* _pysaber_motor1_type;
      _pysaber_motor1_type pysaber_motor1;
      typedef const char* _pysaber_motor2_type;
      _pysaber_motor2_type pysaber_motor2;
      typedef const char* _pysaber_send_type;
      _pysaber_send_type pysaber_send;
      typedef const char* _pysaber_port_type;
      _pysaber_port_type pysaber_port;
      typedef const char* _pyarm_motor1_type;
      _pyarm_motor1_type pyarm_motor1;
      typedef const char* _pyarm_motor2_type;
      _pyarm_motor2_type pyarm_motor2;
      typedef const char* _pyarm_port_type;
      _pyarm_port_type pyarm_port;
      typedef const char* _pyarm_mode_type;
      _pyarm_mode_type pyarm_mode;
      char* cmd_msg[7];
      typedef const char* _wheel_state_type;
      _wheel_state_type wheel_state;
      typedef const char* _j1_fb_type;
      _j1_fb_type j1_fb;
      typedef const char* _j2_fb_type;
      _j2_fb_type j2_fb;
      typedef const char* _j3_fb_type;
      _j3_fb_type j3_fb;
      typedef const char* _j4_fb_type;
      _j4_fb_type j4_fb;
      typedef const char* _j5_wrist_fb_type;
      _j5_wrist_fb_type j5_wrist_fb;

    Status():
      source(0),
      armAttached(0),
      mode(0),
      throttle(0),
      arm_action(""),
      wheel_action(""),
      pysaber_mode(""),
      pysaber_cmd(""),
      pysaber_motor1(""),
      pysaber_motor2(""),
      pysaber_send(""),
      pysaber_port(""),
      pyarm_motor1(""),
      pyarm_motor2(""),
      pyarm_port(""),
      pyarm_mode(""),
      cmd_msg(),
      wheel_state(""),
      j1_fb(""),
      j2_fb(""),
      j3_fb(""),
      j4_fb(""),
      j5_wrist_fb("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_source;
      u_source.real = this->source;
      *(outbuffer + offset + 0) = (u_source.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->source);
      union {
        bool real;
        uint8_t base;
      } u_armAttached;
      u_armAttached.real = this->armAttached;
      *(outbuffer + offset + 0) = (u_armAttached.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->armAttached);
      union {
        int8_t real;
        uint8_t base;
      } u_mode;
      u_mode.real = this->mode;
      *(outbuffer + offset + 0) = (u_mode.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->mode);
      union {
        float real;
        uint32_t base;
      } u_throttle;
      u_throttle.real = this->throttle;
      *(outbuffer + offset + 0) = (u_throttle.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_throttle.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_throttle.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_throttle.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->throttle);
      uint32_t length_arm_action = strlen(this->arm_action);
      varToArr(outbuffer + offset, length_arm_action);
      offset += 4;
      memcpy(outbuffer + offset, this->arm_action, length_arm_action);
      offset += length_arm_action;
      uint32_t length_wheel_action = strlen(this->wheel_action);
      varToArr(outbuffer + offset, length_wheel_action);
      offset += 4;
      memcpy(outbuffer + offset, this->wheel_action, length_wheel_action);
      offset += length_wheel_action;
      uint32_t length_pysaber_mode = strlen(this->pysaber_mode);
      varToArr(outbuffer + offset, length_pysaber_mode);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_mode, length_pysaber_mode);
      offset += length_pysaber_mode;
      uint32_t length_pysaber_cmd = strlen(this->pysaber_cmd);
      varToArr(outbuffer + offset, length_pysaber_cmd);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_cmd, length_pysaber_cmd);
      offset += length_pysaber_cmd;
      uint32_t length_pysaber_motor1 = strlen(this->pysaber_motor1);
      varToArr(outbuffer + offset, length_pysaber_motor1);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_motor1, length_pysaber_motor1);
      offset += length_pysaber_motor1;
      uint32_t length_pysaber_motor2 = strlen(this->pysaber_motor2);
      varToArr(outbuffer + offset, length_pysaber_motor2);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_motor2, length_pysaber_motor2);
      offset += length_pysaber_motor2;
      uint32_t length_pysaber_send = strlen(this->pysaber_send);
      varToArr(outbuffer + offset, length_pysaber_send);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_send, length_pysaber_send);
      offset += length_pysaber_send;
      uint32_t length_pysaber_port = strlen(this->pysaber_port);
      varToArr(outbuffer + offset, length_pysaber_port);
      offset += 4;
      memcpy(outbuffer + offset, this->pysaber_port, length_pysaber_port);
      offset += length_pysaber_port;
      uint32_t length_pyarm_motor1 = strlen(this->pyarm_motor1);
      varToArr(outbuffer + offset, length_pyarm_motor1);
      offset += 4;
      memcpy(outbuffer + offset, this->pyarm_motor1, length_pyarm_motor1);
      offset += length_pyarm_motor1;
      uint32_t length_pyarm_motor2 = strlen(this->pyarm_motor2);
      varToArr(outbuffer + offset, length_pyarm_motor2);
      offset += 4;
      memcpy(outbuffer + offset, this->pyarm_motor2, length_pyarm_motor2);
      offset += length_pyarm_motor2;
      uint32_t length_pyarm_port = strlen(this->pyarm_port);
      varToArr(outbuffer + offset, length_pyarm_port);
      offset += 4;
      memcpy(outbuffer + offset, this->pyarm_port, length_pyarm_port);
      offset += length_pyarm_port;
      uint32_t length_pyarm_mode = strlen(this->pyarm_mode);
      varToArr(outbuffer + offset, length_pyarm_mode);
      offset += 4;
      memcpy(outbuffer + offset, this->pyarm_mode, length_pyarm_mode);
      offset += length_pyarm_mode;
      for( uint32_t i = 0; i < 7; i++){
      uint32_t length_cmd_msgi = strlen(this->cmd_msg[i]);
      varToArr(outbuffer + offset, length_cmd_msgi);
      offset += 4;
      memcpy(outbuffer + offset, this->cmd_msg[i], length_cmd_msgi);
      offset += length_cmd_msgi;
      }
      uint32_t length_wheel_state = strlen(this->wheel_state);
      varToArr(outbuffer + offset, length_wheel_state);
      offset += 4;
      memcpy(outbuffer + offset, this->wheel_state, length_wheel_state);
      offset += length_wheel_state;
      uint32_t length_j1_fb = strlen(this->j1_fb);
      varToArr(outbuffer + offset, length_j1_fb);
      offset += 4;
      memcpy(outbuffer + offset, this->j1_fb, length_j1_fb);
      offset += length_j1_fb;
      uint32_t length_j2_fb = strlen(this->j2_fb);
      varToArr(outbuffer + offset, length_j2_fb);
      offset += 4;
      memcpy(outbuffer + offset, this->j2_fb, length_j2_fb);
      offset += length_j2_fb;
      uint32_t length_j3_fb = strlen(this->j3_fb);
      varToArr(outbuffer + offset, length_j3_fb);
      offset += 4;
      memcpy(outbuffer + offset, this->j3_fb, length_j3_fb);
      offset += length_j3_fb;
      uint32_t length_j4_fb = strlen(this->j4_fb);
      varToArr(outbuffer + offset, length_j4_fb);
      offset += 4;
      memcpy(outbuffer + offset, this->j4_fb, length_j4_fb);
      offset += length_j4_fb;
      uint32_t length_j5_wrist_fb = strlen(this->j5_wrist_fb);
      varToArr(outbuffer + offset, length_j5_wrist_fb);
      offset += 4;
      memcpy(outbuffer + offset, this->j5_wrist_fb, length_j5_wrist_fb);
      offset += length_j5_wrist_fb;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_source;
      u_source.base = 0;
      u_source.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->source = u_source.real;
      offset += sizeof(this->source);
      union {
        bool real;
        uint8_t base;
      } u_armAttached;
      u_armAttached.base = 0;
      u_armAttached.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->armAttached = u_armAttached.real;
      offset += sizeof(this->armAttached);
      union {
        int8_t real;
        uint8_t base;
      } u_mode;
      u_mode.base = 0;
      u_mode.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->mode = u_mode.real;
      offset += sizeof(this->mode);
      union {
        float real;
        uint32_t base;
      } u_throttle;
      u_throttle.base = 0;
      u_throttle.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_throttle.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_throttle.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_throttle.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->throttle = u_throttle.real;
      offset += sizeof(this->throttle);
      uint32_t length_arm_action;
      arrToVar(length_arm_action, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_arm_action; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_arm_action-1]=0;
      this->arm_action = (char *)(inbuffer + offset-1);
      offset += length_arm_action;
      uint32_t length_wheel_action;
      arrToVar(length_wheel_action, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_wheel_action; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_wheel_action-1]=0;
      this->wheel_action = (char *)(inbuffer + offset-1);
      offset += length_wheel_action;
      uint32_t length_pysaber_mode;
      arrToVar(length_pysaber_mode, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_mode; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_mode-1]=0;
      this->pysaber_mode = (char *)(inbuffer + offset-1);
      offset += length_pysaber_mode;
      uint32_t length_pysaber_cmd;
      arrToVar(length_pysaber_cmd, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_cmd; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_cmd-1]=0;
      this->pysaber_cmd = (char *)(inbuffer + offset-1);
      offset += length_pysaber_cmd;
      uint32_t length_pysaber_motor1;
      arrToVar(length_pysaber_motor1, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_motor1; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_motor1-1]=0;
      this->pysaber_motor1 = (char *)(inbuffer + offset-1);
      offset += length_pysaber_motor1;
      uint32_t length_pysaber_motor2;
      arrToVar(length_pysaber_motor2, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_motor2; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_motor2-1]=0;
      this->pysaber_motor2 = (char *)(inbuffer + offset-1);
      offset += length_pysaber_motor2;
      uint32_t length_pysaber_send;
      arrToVar(length_pysaber_send, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_send; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_send-1]=0;
      this->pysaber_send = (char *)(inbuffer + offset-1);
      offset += length_pysaber_send;
      uint32_t length_pysaber_port;
      arrToVar(length_pysaber_port, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pysaber_port; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pysaber_port-1]=0;
      this->pysaber_port = (char *)(inbuffer + offset-1);
      offset += length_pysaber_port;
      uint32_t length_pyarm_motor1;
      arrToVar(length_pyarm_motor1, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pyarm_motor1; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pyarm_motor1-1]=0;
      this->pyarm_motor1 = (char *)(inbuffer + offset-1);
      offset += length_pyarm_motor1;
      uint32_t length_pyarm_motor2;
      arrToVar(length_pyarm_motor2, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pyarm_motor2; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pyarm_motor2-1]=0;
      this->pyarm_motor2 = (char *)(inbuffer + offset-1);
      offset += length_pyarm_motor2;
      uint32_t length_pyarm_port;
      arrToVar(length_pyarm_port, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pyarm_port; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pyarm_port-1]=0;
      this->pyarm_port = (char *)(inbuffer + offset-1);
      offset += length_pyarm_port;
      uint32_t length_pyarm_mode;
      arrToVar(length_pyarm_mode, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_pyarm_mode; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_pyarm_mode-1]=0;
      this->pyarm_mode = (char *)(inbuffer + offset-1);
      offset += length_pyarm_mode;
      for( uint32_t i = 0; i < 7; i++){
      uint32_t length_cmd_msgi;
      arrToVar(length_cmd_msgi, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_cmd_msgi; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_cmd_msgi-1]=0;
      this->cmd_msg[i] = (char *)(inbuffer + offset-1);
      offset += length_cmd_msgi;
      }
      uint32_t length_wheel_state;
      arrToVar(length_wheel_state, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_wheel_state; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_wheel_state-1]=0;
      this->wheel_state = (char *)(inbuffer + offset-1);
      offset += length_wheel_state;
      uint32_t length_j1_fb;
      arrToVar(length_j1_fb, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_j1_fb; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_j1_fb-1]=0;
      this->j1_fb = (char *)(inbuffer + offset-1);
      offset += length_j1_fb;
      uint32_t length_j2_fb;
      arrToVar(length_j2_fb, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_j2_fb; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_j2_fb-1]=0;
      this->j2_fb = (char *)(inbuffer + offset-1);
      offset += length_j2_fb;
      uint32_t length_j3_fb;
      arrToVar(length_j3_fb, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_j3_fb; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_j3_fb-1]=0;
      this->j3_fb = (char *)(inbuffer + offset-1);
      offset += length_j3_fb;
      uint32_t length_j4_fb;
      arrToVar(length_j4_fb, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_j4_fb; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_j4_fb-1]=0;
      this->j4_fb = (char *)(inbuffer + offset-1);
      offset += length_j4_fb;
      uint32_t length_j5_wrist_fb;
      arrToVar(length_j5_wrist_fb, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_j5_wrist_fb; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_j5_wrist_fb-1]=0;
      this->j5_wrist_fb = (char *)(inbuffer + offset-1);
      offset += length_j5_wrist_fb;
     return offset;
    }

    virtual const char * getType() override { return "mobility/Status"; };
    virtual const char * getMD5() override { return "653e89863aa3dbc6fe2e3d1b7d7761dc"; };

  };

}
#endif
