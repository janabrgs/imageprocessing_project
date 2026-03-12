import os
from ultralytics import YOLO

# Paths
INPUT_FOLDER = "input_pages"
OUTPUT_FOLDER = "runs/detect"

MODEL_PATH = "model/best.pt"


def run_detection():
    print("Loading YOLO model...")
    model = YOLO(MODEL_PATH)

    print("Running detection on input pages...")
    model.predict(
        source=INPUT_FOLDER,
        save=True,
        save_txt=True,
        conf=0.25
    )

    print("Detection finished.")
    print(f"Results saved in: {OUTPUT_FOLDER}")


if __name__ == "__main__":
    run_detection()