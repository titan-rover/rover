#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <string>
#include <tf/transform_broadcaster.h>

int main(int argc, char **argv) {
  ros::init(argc, argv, "physics_state_publisher");
  ros::NodeHandle n;
  ros::Publisher joint_pub =
      n.advertise<sensor_msgs::JointState>("joint_states", 1);
  tf::TransformBroadcaster broadcaster;
  ros::Rate loop_rate(30);

  const double degree = M_PI / 180;

  double delta_length = 0.02;

  // robot state
  double grip_length = 0, angle = 0;

  // message declarations
  geometry_msgs::TransformStamped odom_trans;
  sensor_msgs::JointState joint_state;
  odom_trans.header.frame_id = "odom";
  odom_trans.child_frame_id = "base_link";

  while (ros::ok()) {
    // update joint_state
    joint_state.header.stamp = ros::Time::now();
    joint_state.name.resize(8);
    joint_state.position.resize(8);
    joint_state.name[0] = "gripper_extension";
    joint_state.position[0] = grip_length;
    joint_state.name[1] = "left_gripper_joint";
    joint_state.position[1] = 0;
    joint_state.name[2] = "right_gripper_joint";
    joint_state.position[2] = 0;
    joint_state.name[3] = "right_back_wheel_joint";
    joint_state.position[3] = 0;
    joint_state.name[4] = "right_front_wheel_joint";
    joint_state.position[4] = 0;
    joint_state.name[5] = "left_back_wheel_joint";
    joint_state.position[5] = 0;
    joint_state.name[6] = "left_front_wheel_joint";
    joint_state.position[6] = 0;
    joint_state.name[7] = "head_swivel";
    joint_state.position[7] = 0;

    // update transform
    // (moving in a circle with radius=2)
    odom_trans.header.stamp = ros::Time::now();
    odom_trans.transform.translation.x = cos(angle) * 2;
    odom_trans.transform.translation.y = sin(angle) * 2;
    odom_trans.transform.translation.z = 0;
    odom_trans.transform.rotation =
        tf::createQuaternionMsgFromYaw(angle + M_PI / 2);

    // send the joint state and transform
    joint_pub.publish(joint_state);
    broadcaster.sendTransform(odom_trans);

    // Create new robot state
    grip_length -= delta_length;
    if (grip_length < -0.38 || grip_length > 0) {
      delta_length *= -1;
    }

    angle += degree / 4;

    // This will adjust as needed per iteration
    loop_rate.sleep();
  }

  return 0;
}
