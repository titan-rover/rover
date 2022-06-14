#ifndef _ROS_mobility_Mode_h
#define _ROS_mobility_Mode_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mobility
{

  class Mode : public ros::Msg
  {
    public:
      typedef int8_t _source_type;
      _source_type source;
      typedef int8_t _mode_type;
      _mode_type mode;

    Mode():
      source(0),
      mode(0)
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
        int8_t real;
        uint8_t base;
      } u_mode;
      u_mode.real = this->mode;
      *(outbuffer + offset + 0) = (u_mode.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->mode);
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
        int8_t real;
        uint8_t base;
      } u_mode;
      u_mode.base = 0;
      u_mode.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->mode = u_mode.real;
      offset += sizeof(this->mode);
     return offset;
    }

    virtual const char * getType() override { return "mobility/Mode"; };
    virtual const char * getMD5() override { return "e723ef336a7f05c34998a8d285438ef6"; };

  };

}
#endif
