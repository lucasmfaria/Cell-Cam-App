import os
import sys
sys.path.append(os.path.abspath("./cellcam"))
sys.path.append(os.path.abspath("./neuralnet"))
from cellcam import CellphoneCam
import cv2

if __name__ == "__main__":
    cap = CellphoneCam(protocol = "http")
    while True:
        ret, frame = cap.stream.read()
        cv2.imshow('VIDEO', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.stream.release()
    cv2.destroyAllWindows()