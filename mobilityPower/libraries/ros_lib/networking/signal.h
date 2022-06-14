#ifndef _ROS_networking_signal_h
#define _ROS_networking_signal_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace networking
{

  class signal : public ros::Msg
  {
    public:
      typedef int32_t _base_ubiq_type;
      _base_ubiq_type base_ubiq;
      typedef int32_t _timestamp_type;
      _timestamp_type timestamp;
      typedef bool _timeout_type;
      _timeout_type timeout;

    signal():
      base_ubiq(0),
      timestamp(0),
      timeout(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_base_ubiq;
      u_base_ubiq.real = this->base_ubiq;
      *(outbuffer + offset + 0) = (u_base_ubiq.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_base_ubiq.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_base_ubiq.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_base_ubiq.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->base_ubiq);
      union {
        int32_t real;
        uint32_t base;
      } u_timestamp;
      u_timestamp.real = this->timestamp;
      *(outbuffer + offset + 0) = (u_timestamp.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_timestamp.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_timestamp.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_timestamp.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->timestamp);
      union {
        bool real;
        uint8_t base;
      } u_timeout;
      u_timeout.real = this->timeout;
      *(outbuffer + offset + 0) = (u_timeout.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->timeout);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_base_ubiq;
      u_base_ubiq.base = 0;
      u_base_ubiq.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_base_ubiq.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_base_ubiq.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_base_ubiq.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->base_ubiq = u_base_ubiq.real;
      offset += sizeof(this->base_ubiq);
      union {
        int32_t real;
        uint32_t base;
      } u_timestamp;
      u_timestamp.base = 0;
      u_timestamp.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_timestamp.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_timestamp.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_timestamp.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->timestamp = u_timestamp.real;
      offset += sizeof(this->timestamp);
      union {
        bool real;
        uint8_t base;
      } u_timeout;
      u_timeout.base = 0;
      u_timeout.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->timeout = u_timeout.real;
      offset += sizeof(this->timeout);
     return offset;
    }

    virtual const char * getType() override { return "networking/signal"; };
    virtual const char * getMD5() override { return "6005bf414da4c14fe7d1c3bb6698044f"; };

  };

}
#endif
