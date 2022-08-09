import serial

ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()

while True:
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        print(line)
    except KeyboardInterrupt:
        break