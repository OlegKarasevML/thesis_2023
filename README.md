# Thesis 2023 by Oleg Karasev

To reproduce yolo experiments first use documentation from ultralytics to install and prepare yolo v5 and v8. 

Then you should prepare your dataset. To do this, use .py module dataset-creator.py

Train yolo v8

```bash
yolo \
task=<detect or segment> \
mode=train \
model=<path/to/yolo/weights> \
project=runs/<project_name> \
batch=32 \
epochs=250 \
imgsz=1024 \
data=<path/to/your/data> \
optimizer=Adam \
lr0=1e-3 \
weight_decay=1e-5
```

Train yolo v5

```bash
python yolov5/train.py \
    --project <path/to/your/project> \
    --name <name_of_your_project>  \
    --img 1024 \
    --batch 64 \
    --epochs 100 \
    --data <path/to/your/data> \
    --weights <path/to/yolo/weights> \
    --cache ram \
    --optimizer Adam
```

