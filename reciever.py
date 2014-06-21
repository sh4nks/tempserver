"""
    tempserver.reciever
    ~~~~~~~~~~~~~~~~~~~

    The reciever gets the temperature from the CAN Bus and writes it
    to the file.

    :copyright: (c) 2014 by Peter Justin.
    :license: BSD, see LICENSE for more details.
"""


def recieve_temperature(bus, output_file):
    """Recieves a temperature over the CAN Bus.

    :param output_file: The file in which the temperature should be written.
    :param bus: The Bus instance.
    """
    # get the message
    msg = bus.recv()

    # convert the message to a string
    if msg.data is not None:
        data = str(msg.data[0])

    #print("Recieved message: {}".format(data))

    with open(output_file, "w") as f:
        # write the temperature into the file
        f.write(data)
