# import rospy
from paramiko.ssh_exception import NoValidConnectionsError
from datetime import datetime, timezone
import roslibpy
import paramiko
import time
# from std_msgs.msg import Int32
# from signal_strength_publisher.msg import signal
from modules import config

def ssh_connect():
    """
    Function to initiate a paramiko ssh connection object at a specified address.
    Uses information from config. 
    
    Parameters:
        None 
    Returns:
        paramiko ssh connection object
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(config.ubiquiti_address, username=config.username, password=config.password)
    return ssh

def get_signal(ssh_connection):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_connection.exec_command("mca-status | grep signal")
    time.sleep(.1)
    signal_value = ssh_stdout.readlines()[0]
    signal_value = int('-' + ''.join(i for i in signal_value if i.isdigit()))
    return signal_value


if __name__ == '__main__':
    retry_time = 5
    while True:
        try:
            ssh = ssh_connect()
        except NoValidConnectionsError as e:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"[{now}] Unable to ssh at {config.username}@{config.ubiquiti_address} - Retry in {retry_time} seconds")
            time.sleep(retry_time))
            if retry_time < 120:
                retry_time += 5

        client = roslibpy.Ros(host='192.168.1.200', port=8112)
        client.run()

        talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')
        while client.is_connected:


    # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mca-status | grep signal")
    # time.sleep(.1)
    # signal_value = ssh_stdout.readlines()[0]
    # signal_value = int('-' + ''.join(i for i in signal_value if i.isdigit()))
    # print(signal_value)
        # msg.rover_ubiq = signal_value
        # msg.timestamp = now
        # publisher.publish(msg)
        # rospy.loginfo(msg) #loginfo will print the contents of the topic to the local console that ran the command
        # rate.sleep()