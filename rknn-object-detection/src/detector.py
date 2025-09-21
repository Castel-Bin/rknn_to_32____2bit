import cv2
import numpy as np
from rknn.api import RKNN
from uart_sender import send_target
from types.index import LABELS

class ObjectDetector:
    def __init__(self, model_path):
        self.rknn = RKNN()
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        self.rknn.load_model(self.model_path)
        self.rknn.init_runtime()

    def detect(self, frame):
        # Preprocess the frame for the model
        input_data = self.preprocess(frame)
        output = self.rknn.inference(inputs=[input_data])
        return self.postprocess(output)

    def preprocess(self, frame):
        # Resize and normalize the frame
        frame_resized = cv2.resize(frame, (640, 640))
        frame_normalized = frame_resized / 255.0
        return frame_normalized.astype(np.float32)

    def postprocess(self, output):
        # Assuming output is a list of detections
        for detection in output[0]:
            label_index = int(detection[0])
            if label_index in LABELS:
                return label_index
        return None

def main():
    model_path = 'path/to/your/model.rknn'
    detector = ObjectDetector(model_path)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        label_index = detector.detect(frame)
        if label_index is not None:
            send_target(label_index)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()