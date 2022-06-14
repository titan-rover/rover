#ifndef _ROS_fake_sensor_test_gps_h
#define _ROS_fake_sensor_test_gps_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace fake_sensor_test
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
      uint32_t destLat_length;
      typedef char* _destLat_type;
      _destLat_type st_destLat;
      _destLat_type * destLat;
      uint32_t destLon_length;
      typedef char* _destLon_type;
      _destLon_type st_destLon;
      _destLon_type * destLon;

    gps():
      baseLat(""),
      baseLon(""),
      roverLat(""),
      roverLon(""),
      destLat_length(0), st_destLat(), destLat(nullptr),
      destLon_length(0), st_destLon(), destLon(nullptr)
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
      *(outbuffer + offset + 0) = (this->destLat_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->destLat_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->destLat_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->destLat_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->destLat_length);
      for( uint32_t i = 0; i < destLat_length; i++){
      uint32_t length_destLati = strlen(this->destLat[i]);
      varToArr(outbuffer + offset, length_destLati);
      offset += 4;
      memcpy(outbuffer + offset, this->destLat[i], length_destLati);
      offset += length_destLati;
      }
      *(outbuffer + offset + 0) = (this->destLon_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->destLon_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->destLon_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->destLon_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->destLon_length);
      for( uint32_t i = 0; i < destLon_length; i++){
      uint32_t length_destLoni = strlen(this->destLon[i]);
      varToArr(outbuffer + offset, length_destLoni);
      offset += 4;
      memcpy(outbuffer + offset, this->destLon[i], length_destLoni);
      offset += length_destLoni;
      }
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
      uint32_t destLat_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      destLat_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      destLat_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      destLat_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->destLat_length);
      if(destLat_lengthT > destLat_length)
        this->destLat = (char**)realloc(this->destLat, destLat_lengthT * sizeof(char*));
      destLat_length = destLat_lengthT;
      for( uint32_t i = 0; i < destLat_length; i++){
      uint32_t length_st_destLat;
      arrToVar(length_st_destLat, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_st_destLat; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_st_destLat-1]=0;
      this->st_destLat = (char *)(inbuffer + offset-1);
      offset += length_st_destLat;
        memcpy( &(this->destLat[i]), &(this->st_destLat), sizeof(char*));
      }
      uint32_t destLon_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      destLon_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      destLon_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      destLon_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->destLon_length);
      if(destLon_lengthT > destLon_length)
        this->destLon = (char**)realloc(this->destLon, destLon_lengthT * sizeof(char*));
      destLon_length = destLon_lengthT;
      for( uint32_t i = 0; i < destLon_length; i++){
      uint32_t length_st_destLon;
      arrToVar(length_st_destLon, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_st_destLon; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_st_destLon-1]=0;
      this->st_destLon = (char *)(inbuffer + offset-1);
      offset += length_st_destLon;
        memcpy( &(this->destLon[i]), &(this->st_destLon), sizeof(char*));
      }
     return offset;
    }

    virtual const char * getType() override { return "fake_sensor_test/gps"; };
    virtual const char * getMD5() override { return "e9cc89c8877281a7452cca517a720dac"; };

  };

}
#endif
