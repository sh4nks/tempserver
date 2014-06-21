"""
    tempserver.sender
    ~~~~~~~~~~~~~~~~~

    The sender gets the temperature from a file and sends it via
    the CAN Bus.

    :copyright: (c) 2014 by Peter Justin.
    :license: BSD, see LICENSE for more details.
"""


def send_temperature(bus, input_file):
    """Sends a temperature over the CAN Bus.

    :param input_file: The file from which the temperature should be read.
    :param bus: The Bus instance.
    """
    temperature = read_temperature_from_file(input_file)

    # python-can doesn't support strings at the moment, so we need to convert
    # them to integers.
    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Could not convert temperature to float")
    else:
        temperature = int(temperature)

    #print("Sending message: {}".format(temperature))

    msg = can.Message(data=[temperature])
    bus.send(msg)


def read_temperature_from_file(input_file):
    """Reads a temperature from the given file and returns it.

    :param intput_file: The full path to the file from which the temperature
                        should be read.
    """
    temperature = None
    with open(input_file) as f:
        # Note: read() only reads the first line of the file. Do we need more
        # values?
        temperature = f.read().rstrip()

    return temperature
