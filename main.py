import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
def send_command(command):
    arduino.write(bytes(command, 'utf-8'))
    time.sleep(1)
    response = arduino.readline().decode('utf-8').strip()
    print("Arduino response:", response)
send_command("ON")
send_command("OFF")
arduino.close()
