# Relay Package

The *Relay* package contains modules and files that allow the base station 433mhz (yagi) antenna to communicate ROS commands to the Rover's 433mhz antenna.

The package facilitates the connection to the Ebyte radio modules via GPIO pins on the RPi, and creates a networking socket to receive commands to encode into a payload, and then sent over 433mhz radio to the Rover. 
The program is designed to wait until a valid GPIO connection is made at the specified serial path to continue executing. 
It can be started via command line or made into a systemd daemon. 


# Files
- `Relay.py`
	- Driver program for the package
- `relay.py`
	- Class definition that contains methods to create and send payloads over 433mhz radio, and set up GPIO serial connections
- `config.py`
	- Config object that gets its values from the `config.json` file, used by the Relay module and driver program
- `errors.py`
	- Custom error definitions
- `config.js`
	- JSON file that contains keys that can be set to custom values to ease configuration changes. 

## Prerequisites
It is recommended to run this package with python3.6 or higher.  

Make sure the RPi.GPIO package is installed in your python environment.
https://pypi.org/project/RPi.GPIO/

`pip install RPi.GPIO`

Make sure the GPIO connection to the Ebyte modules is secure and that the module has significant power to operate. 
## Example Usage

`sudo python3 Relay.py`

## Creating Systemd daemon

https://en.wikipedia.org/wiki/Systemd
Systemd allows for the autostarting of this progam at boot.

To do so we need to make a `.service` file.
`sudo nano /etc/systemd/system/433relay.service`

Paste the following into the file:
(if your path to the `Relay.py` is different, use that path instead of this example)
```
[Unit]
Description=My test service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/phobos/Development/relay/Relay.py
[Install]
WantedBy=multi-user.target
```

Then enable the service file 
`sudo chmod 777 /etc/systemd/system/433relay.service`

Then reload the daemons to pick up the new service file
`sudo systemctl daemon-reload`

Then enable the daemon
`sudo systemctl enable 433relay`

Finally start the daemon
`sudo systemctl start 433relay`

Then you can check the status to see if it had ran
`sudo systemctl status 433relay`
