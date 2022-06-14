#ifndef _ROS_gnss_gps_h
#define _ROS_gnss_gps_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace gnss
{

  class gps : public ros::Msg
  {
    public:
      typedef const char* _baseLat_type;
      _baseLat_type baseLat;
      typedef const char* _baseLon_type;
      _baseLon_type baseLon;
      typedef const char* _roverLat_type;
      _roverLat_type roverLat;
      typedef const char* _roverLon_type;
      _roverLon_type roverLon;
      typedef const char* _tennisLat_type;
      _tennisLat_type tennisLat;
      typedef const char* _tennisLong_type;
      _tennisLong_type tennisLong;

    gps():
      baseLat(""),
      baseLon(""),
      roverLat(""),
      roverLon(""),
      tennisLat(""),
      tennisLong("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      uint32_t length_baseLat = strlen(this->baseLat);
      varToArr(outbuffer + offset, length_baseLat);
      offset += 4;
      memcpy(outbuffer + offset, this->baseLat, length_baseLat);
      offset += length_baseLat;
      uint32_t length_baseLon = strlen(this->baseLon);
      varToArr(outbuffer + offset, length_baseLon);
      offset += 4;
      memcpy(outbuffer + offset, this->baseLon, length_baseLon);
      offset += length_baseLon;
      uint32_t length_roverLat = strlen(this->roverLat);
      varToArr(outbuffer + offset, length_roverLat);
      offset += 4;
      memcpy(outbuffer + offset, this->roverLat, length_roverLat);
      offset += length_roverLat;
      uint32_t length_roverLon = strlen(this->roverLon);
      varToArr(outbuffer + offset, length_roverLon);
      offset += 4;
      memcpy(outbuffer + offset, this->roverLon, length_roverLon);
      offset += length_roverLon;
      uint32_t length_tennisLat = strlen(this->tennisLat);
      varToArr(outbuffer + offset, length_tennisLat);
      offset += 4;
      memcpy(outbuffer + offset, this->tennisLat, length_tennisLat);
      offset += length_tennisLat;
      uint32_t length_tennisLong = strlen(this->tennisLong);
      varToArr(outbuffer + offset, length_tennisLong);
      offset += 4;
      memcpy(outbuffer + offset, this->tennisLong, length_tennisLong);
      offset += length_tennisLong;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      uint32_t length_baseLat;
      arrToVar(length_baseLat, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_baseLat; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_baseLat-1]=0;
      this->baseLat = (char *)(inbuffer + offset-1);
      offset += length_baseLat;
      uint32_t length_baseLon;
      arrToVar(length_baseLon, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_baseLon; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_baseLon-1]=0;
      this->baseLon = (char *)(inbuffer + offset-1);
      offset += length_baseLon;
      uint32_t length_roverLat;
      arrToVar(length_roverLat, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_roverLat; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_roverLat-1]=0;
      this->roverLat = (char *)(inbuffer + offset-1);
      offset += length_roverLat;
      uint32_t length_roverLon;
      arrToVar(length_roverLon, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_roverLon; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_roverLon-1]=0;
      this->roverLon = (char *)(inbuffer + offset-1);
      offset += length_roverLon;
      uint32_t length_tennisLat;
      arrToVar(length_tennisLat, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_tennisLat; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_tennisLat-1]=0;
      this->tennisLat = (char *)(inbuffer + offset-1);
      offset += length_tennisLat;
      uint32_t length_tennisLong;
      arrToVar(length_tennisLong, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_tennisLong; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_tennisLong-1]=0;
      this->tennisLong = (char *)(inbuffer + offset-1);
      offset += length_tennisLong;
     return offset;
    }

    virtual const char * getType() override { return "gnss/gps"; };
    virtual const char * getMD5() override { return "0e3fb25d1342dcd84c677d8314423556"; };

  };

}
#endif
