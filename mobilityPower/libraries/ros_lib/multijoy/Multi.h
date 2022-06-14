#ifndef _ROS_multijoy_Multi_h
#define _ROS_multijoy_Multi_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"
#include "std_msgs/UInt8.h"
#include "sensor_msgs/Joy.h"

namespace multijoy
{

  class Multi : public ros::Msg
  {
    public:
      typedef std_msgs::Header _header_type;
      _header_type header;
      typedef int8_t _source_type;
      _source_type source;
      typedef std_msgs::UInt8 _njoys_type;
      _njoys_type njoys;
      uint32_t joys_length;
      typedef sensor_msgs::Joy _joys_type;
      _joys_type st_joys;
      _joys_type * joys;

    Multi():
      header(),
      source(0),
      njoys(),
      joys_length(0), st_joys(), joys(nullptr)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      union {
        int8_t real;
        uint8_t base;
      } u_source;
      u_source.real = this->source;
      *(outbuffer + offset + 0) = (u_source.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->source);
      offset += this->njoys.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->joys_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->joys_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->joys_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->joys_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->joys_length);
      for( uint32_t i = 0; i < joys_length; i++){
      offset += this->joys[i].serialize(outbuffer + offset);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      union {
        int8_t real;
        uint8_t base;
      } u_source;
      u_source.base = 0;
      u_source.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->source = u_source.real;
      offset += sizeof(this->source);
      offset += this->njoys.deserialize(inbuffer + offset);
      uint32_t joys_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      joys_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      joys_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      joys_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->joys_length);
      if(joys_lengthT > joys_length)
        this->joys = (sensor_msgs::Joy*)realloc(this->joys, joys_lengthT * sizeof(sensor_msgs::Joy));
      joys_length = joys_lengthT;
      for( uint32_t i = 0; i < joys_length; i++){
      offset += this->st_joys.deserialize(inbuffer + offset);
        memcpy( &(this->joys[i]), &(this->st_joys), sizeof(sensor_msgs::Joy));
      }
     return offset;
    }

    virtual const char * getType() override { return "multijoy/Multi"; };
    virtual const char * getMD5() override { return "dad8305bc89f7ba9a86f4aba09f437c2"; };

  };

}
#endif
