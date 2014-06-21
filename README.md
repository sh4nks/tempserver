# INTRODUCTION

This is a project for a lecture at our university.
The _tempserver_ manages the connection between RPi temperature sensor and
RPi LED display. The temperature is then being send over the CAN Bus.

**Note:** This project is just for learning purposes.


# DEPENDENCIES

It depends on python >= 3.3 and on the [python-can](https://bitbucket.org/hardbyte/python-can) library.


# USAGE

The server provides two different types:
* **Reciever**

    The recieving server writes the value in a file, so that the Pi can read it
    from there.

* **Sender**

    The sending server reads the value from the file in which the Pi's
    sensor the temperature writes, and broadcasts it via a CAN Bus.


```
usage: server.py [-h] [-t TYPE] -p PATH [-c CHANNEL]

Sends or recieves messages from a CAN Bus.

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  The server type. '--type send' sends the message and '
                        --type recieve' recieves the message
  -p PATH, --path PATH  The full path path to the file which should
                        contain/recieve the temperature
  -c CHANNEL, --channel CHANNEL
                        The name of the CAN channel. For example, such a
                        channel could be named 'vcan0'. If not provided, it
                        defaults back to the channel which is defined in the
                        can.conf/ini
```
