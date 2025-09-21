import time
import cv2
from camera import Camera
from detector import Detector
from uart_sender import send_to_uart

def main():
    camera = Camera()
    detector = Detector()

    while True:
        frame = camera.capture_frame()
        label = detector.detect(frame)

        if label is not None:
            send_to_uart(label)
            print(f"Detected and sent label: {label}")
            break
        else:
            print("No target detected, capturing again...")
            time.sleep(1)

if __name__ == "__main__":
    main()