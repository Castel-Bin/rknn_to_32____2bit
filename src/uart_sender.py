import serial
import time

class UartSender:
    def __init__(self, port='/dev/ttyS1', baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # 等待串口初始化

    def send_target(self, target_label):
        if target_label in [0, 1, 2]:  # 确保目标标签有效
            self.ser.write(bytes([target_label]))
            self.ser.flush()
        else:
            raise ValueError("Invalid target label. Must be 0, 1, or 2.")

    def close(self):
        self.ser.close()