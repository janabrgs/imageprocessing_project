# Flashcard Detection & Automated Print Pipeline

## Project Overview

This project implements a complete computer vision workflow to automatically generate printable flashcards from scanned learning sheets.

The pipeline performs:

1. Detection of flashcard regions using YOLOv8  
2. Cropping of individual cards  
3. Separation of image side (front) and text side (back)  
4. Automatic generation of 3x3 A4 print layouts  
5. Duplex alignment for correct front/back printing  

The final output is a duplex-ready printable PDF file.

---

## Technologies Used

- Python  
- YOLOv8 (Ultralytics)  
- OpenCV (image preprocessing & cropping)  
- Pillow (PIL)  
- LabelImg  

---

## Project Structure

```text
imageprocessing_project/
├── README.md
├── .gitignore
├── data.yaml
├── data/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── flashcards/
│   ├── front/
│   └── back/
├── notebooks/
└── print_pages/
    └── print_short_edge.pdf```

---

## Workflow

### 1️⃣ Data Annotation
Flashcard regions were manually annotated using LabelImg in YOLO format.

### 2️⃣ Model Training
A YOLOv8 model was trained to detect flashcard bounding boxes on scanned pages.

### 3️⃣ Card Extraction
Detected bounding boxes were used to crop individual flashcards automatically using OpenCV.

### 4️⃣ Front/Back Separation
Each cropped card was programmatically split into:
- Upper part (image side)
- Lower part (text side)

### 5️⃣ Layout Generation
Flashcards were arranged into 3x3 A4 layouts with cutting guides.

Special handling was implemented to ensure correct duplex alignment so that each front side matches the corresponding back side after printing.

---

## Final Output

The project generates a duplex-ready printable PDF:

print_short_edge.pdf


After double-sided printing and cutting, the cards can be used as physical learning flashcards.

---

## Key Learning Outcomes

- Building an object detection dataset  
- Training and fine-tuning YOLOv8  
- Post-processing detection outputs  
- Automated image cropping  
- Generating print-ready layouts  
- Handling duplex alignment logic  
