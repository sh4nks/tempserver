#!/usr/bin/env python
"""
    tempserver.server
    ~~~~~~~~~~~~~~~~~

    This module provides the server for recieving and sending messages
    over the CAN Bus.

    The recieving server writes the value in a file, so that the Pi can read it
    from there.

    The sending server reads the value from the file in which the Pi's
    sensor the temperature writes, and broadcasts it via a CAN Bus.

    :copyright: (c) 2014 by Peter Justin.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
import time
import argparse
from datetime import datetime

import can

from reciever import recieve_temperature
from sender import send_temperature


def run_server(callback, startup_message=None, shutdown_message=None, **kwargs):
    try:
        if startup_message is not None:
            print(startup_message)

        while True:
            callback(**kwargs)
            time.sleep(1)

    except KeyboardInterrupt:
        bus.shutdown()

        if shutdown_message is not None:
            print(shutdown_message)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Sends or recieves messages from a CAN Bus."
    )

    parser.add_argument('-t', '--type',
        help=("The server type. '--type send' sends the message and "
              "'--type recieve' recieves the message"),
        default="send"
    )

    parser.add_argument('-p', '--path',
        help=("The full path path to the file which should contain/recieve "
              "the temperature"),
        required=True,
    )

    parser.add_argument('-c', '--channel',
        help=("The name of the CAN channel. For example, such a channel could "
              "be named 'vcan0'. If not provided, it defaults back to the "
              "channel which is defined in the can.conf/ini"),
    )

    results = parser.parse_args()

    # We need the file on both sides because we need to read from the sensor on
    # the first Pi which stores the value in a file (?) and the other Pi reads
    # this value from a file (?). I'm not certain if this is actually the case.
    if not os.path.exists(results.path):
        parser.print_help(sys.stderr)
        parser.exit(2, "Path does not exist. Please enter a valid path/file.\n")

    if results.channel is not None:
        channel = results.channel
    else:
        channel = can.rc["channel"]

    bus = can.interface.Bus(channel)

    date = datetime.now().strftime("%d. %B %Y - %Mmin %Ssec")

    # sender
    if results.type == "send":
        startup_message = 'Sender started on {}'.format(date)

        run_server(send_temperature, bus=bus, input_file=results.path,
                   startup_message=startup_message)

    # reciever
    elif results.type == "recieve":
        startup_message = 'Sender started on {}'.format(date)

        run_server(recieve_temperature, bus=bus, output_file=results.path,
                   startup_message=startup_message)

    # nothing - abort
    else:
        parser.print_help(sys.stderr)
        parser.exit(2, "{} is not a correct type.\n".format(results.type))
