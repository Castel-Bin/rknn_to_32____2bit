import cv2
import time
from detector import detect_object
from uart_sender import send_to_uart

def capture_and_detect():
    cap = cv2.VideoCapture(0)  # 打开默认摄像头

    while True:
        ret, frame = cap.read()  # 捕获视频帧
        if not ret:
            print("无法读取摄像头数据")
            continue

        label = detect_object(frame)  # 使用检测模块进行目标检测

        if label is not None:  # 如果检测到目标
            send_to_uart(label)  # 通过UART发送目标标签
            break  # 退出循环

        time.sleep(0.1)  # 等待一段时间再进行下一次捕获

    cap.release()  # 释放摄像头资源
    cv2.destroyAllWindows()  # 关闭所有OpenCV窗口

if __name__ == "__main__":
    capture_and_detect()