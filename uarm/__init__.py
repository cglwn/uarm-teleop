"""Python module containing Flask application for teleoperation of uARM
Contains logic for manipulator communication through serial port
"""
from flask import Flask, render_template

import serial

app = Flask(__name__)

ser = serial.Serial(port='COM3', 
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=3)

@app.route("/")
def index():
    return render_template("teleop.jinja2")

@app.route("/move/<rotation>/<stretch>/<height>")
def move_http(rotation):
    serial_message = move(rotation, 0, 0, 0, False)
    ser.write(bytes(serial_message))
    return "Rotated to rotation"

def move(rotation, stretch, height, hand_angle, grip):
    """Returns the byte array to be sent to the arm corresponding to the 
    parameters
    """
    serial_message = bytearray([0xff, 0xaa])
    serial_message.append((rotation >> 8) & 0xff)
    serial_message.append(rotation & 0xff)
    serial_message.append((stretch >> 8) & 0xff)
    serial_message.append(stretch & 0xff)
    serial_message.append((height >> 8) & 0xff)
    serial_message.append(height & 0xff)
    serial_message.append((hand_angle >> 8) & 0xff)
    serial_message.append(hand_angle & 0xff)
    serial_message.append(1 if grip else 2)
    return serial_message

if __name__ == "__main__":
    app.run(debug=True)
    ser.close()