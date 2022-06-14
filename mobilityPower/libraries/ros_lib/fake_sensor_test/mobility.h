#ifndef _ROS_fake_sensor_test_mobility_h
#define _ROS_fake_sensor_test_mobility_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace fake_sensor_test
{

  class mobility : public ros::Msg
  {
    public:
      typedef int32_t _current_draw_type;
      _current_draw_type current_draw;

    mobility():
      current_draw(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_current_draw;
      u_current_draw.real = this->current_draw;
      *(outbuffer + offset + 0) = (u_current_draw.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_current_draw.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_current_draw.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_current_draw.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->current_draw);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_current_draw;
      u_current_draw.base = 0;
      u_current_draw.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_current_draw.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_current_draw.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_current_draw.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->current_draw = u_current_draw.real;
      offset += sizeof(this->current_draw);
     return offset;
    }

    virtual const char * getType() override { return "fake_sensor_test/mobility"; };
    virtual const char * getMD5() override { return "f201fd693b139583c25b18c341a670c8"; };

  };

}
#endif
