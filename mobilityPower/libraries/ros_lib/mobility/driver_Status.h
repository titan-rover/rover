#ifndef _ROS_mobility_driver_Status_h
#define _ROS_mobility_driver_Status_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mobility
{

  class driver_Status : public ros::Msg
  {
    public:
      typedef bool _autoActive_type;
      _autoActive_type autoActive;
      typedef float _goto_lat_type;
      _goto_lat_type goto_lat;
      typedef float _goto_lon_type;
      _goto_lon_type goto_lon;

    driver_Status():
      autoActive(0),
      goto_lat(0),
      goto_lon(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_autoActive;
      u_autoActive.real = this->autoActive;
      *(outbuffer + offset + 0) = (u_autoActive.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->autoActive);
      union {
        float real;
        uint32_t base;
      } u_goto_lat;
      u_goto_lat.real = this->goto_lat;
      *(outbuffer + offset + 0) = (u_goto_lat.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_goto_lat.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_goto_lat.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_goto_lat.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->goto_lat);
      union {
        float real;
        uint32_t base;
      } u_goto_lon;
      u_goto_lon.real = this->goto_lon;
      *(outbuffer + offset + 0) = (u_goto_lon.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_goto_lon.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_goto_lon.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_goto_lon.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->goto_lon);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_autoActive;
      u_autoActive.base = 0;
      u_autoActive.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->autoActive = u_autoActive.real;
      offset += sizeof(this->autoActive);
      union {
        float real;
        uint32_t base;
      } u_goto_lat;
      u_goto_lat.base = 0;
      u_goto_lat.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_goto_lat.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_goto_lat.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_goto_lat.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->goto_lat = u_goto_lat.real;
      offset += sizeof(this->goto_lat);
      union {
        float real;
        uint32_t base;
      } u_goto_lon;
      u_goto_lon.base = 0;
      u_goto_lon.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_goto_lon.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_goto_lon.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_goto_lon.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->goto_lon = u_goto_lon.real;
      offset += sizeof(this->goto_lon);
     return offset;
    }

    virtual const char * getType() override { return "mobility/driver_Status"; };
    virtual const char * getMD5() override { return "ffafddb4e7e443ff552d29a8b07ed846"; };

  };

}
#endif
