#ifndef _ROS_mobility_Mobility_h
#define _ROS_mobility_Mobility_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mobility
{

  class Mobility : public ros::Msg
  {
    public:
      typedef int8_t _ForwardY_type;
      _ForwardY_type ForwardY;
      typedef int8_t _TurningX_type;
      _TurningX_type TurningX;

    Mobility():
      ForwardY(0),
      TurningX(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_ForwardY;
      u_ForwardY.real = this->ForwardY;
      *(outbuffer + offset + 0) = (u_ForwardY.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->ForwardY);
      union {
        int8_t real;
        uint8_t base;
      } u_TurningX;
      u_TurningX.real = this->TurningX;
      *(outbuffer + offset + 0) = (u_TurningX.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->TurningX);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_ForwardY;
      u_ForwardY.base = 0;
      u_ForwardY.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->ForwardY = u_ForwardY.real;
      offset += sizeof(this->ForwardY);
      union {
        int8_t real;
        uint8_t base;
      } u_TurningX;
      u_TurningX.base = 0;
      u_TurningX.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->TurningX = u_TurningX.real;
      offset += sizeof(this->TurningX);
     return offset;
    }

    virtual const char * getType() override { return "mobility/Mobility"; };
    virtual const char * getMD5() override { return "80c0a058aa7119b3181b6edb07201e22"; };

  };

}
#endif
