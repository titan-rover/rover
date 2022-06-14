#ifndef _ROS_multimaster_msgs_fkie_ROSMaster_h
#define _ROS_multimaster_msgs_fkie_ROSMaster_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace multimaster_msgs_fkie
{

  class ROSMaster : public ros::Msg
  {
    public:
      typedef const char* _name_type;
      _name_type name;
      typedef const char* _uri_type;
      _uri_type uri;
      typedef float _timestamp_type;
      _timestamp_type timestamp;
      typedef float _timestamp_local_type;
      _timestamp_local_type timestamp_local;
      typedef bool _online_type;
      _online_type online;
      typedef const char* _discoverer_name_type;
      _discoverer_name_type discoverer_name;
      typedef const char* _monitoruri_type;
      _monitoruri_type monitoruri;

    ROSMaster():
      name(""),
      uri(""),
      timestamp(0),
      timestamp_local(0),
      online(0),
      discoverer_name(""),
      monitoruri("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      uint32_t length_name = strlen(this->name);
      varToArr(outbuffer + offset, length_name);
      offset += 4;
      memcpy(outbuffer + offset, this->name, length_name);
      offset += length_name;
      uint32_t length_uri = strlen(this->uri);
      varToArr(outbuffer + offset, length_uri);
      offset += 4;
      memcpy(outbuffer + offset, this->uri, length_uri);
      offset += length_uri;
      offset += serializeAvrFloat64(outbuffer + offset, this->timestamp);
      offset += serializeAvrFloat64(outbuffer + offset, this->timestamp_local);
      union {
        bool real;
        uint8_t base;
      } u_online;
      u_online.real = this->online;
      *(outbuffer + offset + 0) = (u_online.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->online);
      uint32_t length_discoverer_name = strlen(this->discoverer_name);
      varToArr(outbuffer + offset, length_discoverer_name);
      offset += 4;
      memcpy(outbuffer + offset, this->discoverer_name, length_discoverer_name);
      offset += length_discoverer_name;
      uint32_t length_monitoruri = strlen(this->monitoruri);
      varToArr(outbuffer + offset, length_monitoruri);
      offset += 4;
      memcpy(outbuffer + offset, this->monitoruri, length_monitoruri);
      offset += length_monitoruri;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      uint32_t length_name;
      arrToVar(length_name, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_name; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_name-1]=0;
      this->name = (char *)(inbuffer + offset-1);
      offset += length_name;
      uint32_t length_uri;
      arrToVar(length_uri, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_uri; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_uri-1]=0;
      this->uri = (char *)(inbuffer + offset-1);
      offset += length_uri;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->timestamp));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->timestamp_local));
      union {
        bool real;
        uint8_t base;
      } u_online;
      u_online.base = 0;
      u_online.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->online = u_online.real;
      offset += sizeof(this->online);
      uint32_t length_discoverer_name;
      arrToVar(length_discoverer_name, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_discoverer_name; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_discoverer_name-1]=0;
      this->discoverer_name = (char *)(inbuffer + offset-1);
      offset += length_discoverer_name;
      uint32_t length_monitoruri;
      arrToVar(length_monitoruri, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_monitoruri; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_monitoruri-1]=0;
      this->monitoruri = (char *)(inbuffer + offset-1);
      offset += length_monitoruri;
     return offset;
    }

    virtual const char * getType() override { return "multimaster_msgs_fkie/ROSMaster"; };
    virtual const char * getMD5() override { return "08ea76968a3be2b8b1c6550b39616f72"; };

  };

}
#endif
