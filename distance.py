import serial
import time

# YOUR PORTS
arduino_port = 'COM3'  # Arduino R3
esp32_port = 'COM6'    # ESP32

arduino = serial.Serial(arduino_port, 9600, timeout=1)
esp32 = serial.Serial(esp32_port, 9600, timeout=1)
time.sleep(2)

print("🌡️ DISTANCE BRIDGE ACTIVE")
print("Arduino → ESP32 → ThingSpeak Channel 3258381")

while True:
    if arduino.in_waiting:
        data = arduino.readline().decode('utf-8').strip()
        if "DIST:" in data:
            print("📏 " + data)
            esp32.write((data + '\n').encode())
    time.sleep(0.1)

