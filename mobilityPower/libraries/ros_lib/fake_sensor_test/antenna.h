#ifndef _ROS_fake_sensor_test_antenna_h
#define _ROS_fake_sensor_test_antenna_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace fake_sensor_test
{

  class antenna : public ros::Msg
  {
    public:
      typedef int32_t _signal_strength_type;
      _signal_strength_type signal_strength;

    antenna():
      signal_strength(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_signal_strength;
      u_signal_strength.real = this->signal_strength;
      *(outbuffer + offset + 0) = (u_signal_strength.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_signal_strength.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_signal_strength.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_signal_strength.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->signal_strength);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_signal_strength;
      u_signal_strength.base = 0;
      u_signal_strength.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_signal_strength.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_signal_strength.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_signal_strength.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->signal_strength = u_signal_strength.real;
      offset += sizeof(this->signal_strength);
     return offset;
    }

    virtual const char * getType() override { return "fake_sensor_test/antenna"; };
    virtual const char * getMD5() override { return "d25cadb0a355f32f725fab4b5c457e32"; };

  };

}
#endif
