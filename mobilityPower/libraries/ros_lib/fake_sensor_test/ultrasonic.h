#ifndef _ROS_fake_sensor_test_ultrasonic_h
#define _ROS_fake_sensor_test_ultrasonic_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace fake_sensor_test
{

  class ultrasonic : public ros::Msg
  {
    public:
      typedef float _max_distance_type;
      _max_distance_type max_distance;

    ultrasonic():
      max_distance(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_max_distance;
      u_max_distance.real = this->max_distance;
      *(outbuffer + offset + 0) = (u_max_distance.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_max_distance.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_max_distance.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_max_distance.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->max_distance);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_max_distance;
      u_max_distance.base = 0;
      u_max_distance.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_max_distance.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_max_distance.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_max_distance.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->max_distance = u_max_distance.real;
      offset += sizeof(this->max_distance);
     return offset;
    }

    virtual const char * getType() override { return "fake_sensor_test/ultrasonic"; };
    virtual const char * getMD5() override { return "14d2c553085e6766406b10adb41220b3"; };

  };

}
#endif
