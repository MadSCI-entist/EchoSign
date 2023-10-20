import serial
import time
# Configure the serial connections
arduino1_port = "COM4"  # Replace with the actual COM port for Arduino 1
arduino2_port = "COM7"  # Replace with the actual COM port for Arduino 2
baud_rate = 9600

arduino1_serial = serial.Serial(arduino1_port, baud_rate)
arduino2_serial = serial.Serial(arduino2_port, baud_rate)

while True:
    # Read data from Arduino 1
    data1 = arduino1_serial.readline().decode().strip()
    # Read data from Arduino 2
    data2 = arduino2_serial.readline().decode().strip()

    # Process data from Arduino 1
    sensor_data1 = data1.split(",")
    
    # Process data from Arduino 2
    sensor_data2 = data2.split(",")
    
    # Print or process the sensor data from both Arduino
    print("Arduino 1 Sensor Data:", sensor_data1)
    print("Arduino 2 Sensor Data:", sensor_data2)

    X1, Y1, Z1 , F1, F2, F3, F4, F5 = sensor_data1
    X2, Y2, Z2 , F6, F7, F8, F9, F10 = sensor_data2

    time.sleep(0.5)

    
