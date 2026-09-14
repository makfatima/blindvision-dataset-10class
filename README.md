# BlindVision — Hybrid 10-Class Dataset & Training Artifacts

> **Scope of this repository:** This is a secondary hybrid-data transparency
> release. It does **not** contain the original 5,600-image training dataset,
> the primary trained weights, or the checkpoint used for the headline 92.2%
> result reported in the manuscript. The dataset and checkpoint here (`best.pt`,
> `last.pt`) come from a separate hybrid run assembled from public sources —
> see [MANIFEST.md](MANIFEST.md) for per-class provenance and licensing.

## What's in this repo

A 10-class YOLOv8 object-detection dataset and training run, assembled from
three public sources (COCO 2017 via FiftyOne, DoorDetect-Dataset, and two
Roboflow sets) to cover classes relevant to the BlindVision assistive-navigation
project.

| Class id | Name | Source |
|---|---|---|
| 0 | person | COCO 2017 |
| 1 | door | DoorDetect-Dataset |
| 2 | chair | COCO 2017 |
| 3 | backpack | COCO 2017 |
| 4 | laptop | COCO 2017 |
| 5 | bottle | COCO 2017 |
| 6 | pole | Roboflow "PoleDetection" |
| 7 | vehicle | COCO 2017 (`car` class) |
| 8 | bicycle | COCO 2017 |
| 9 | stairs | Roboflow "Stairs_Detection" |

Full per-class box counts, licensing terms, and the class-imbalance disclosure
are in [MANIFEST.md](MANIFEST.md) — read that before citing or redistributing
any subset.

## Repository contents

```
images/train/   2,380 training images
images/val/       492 validation images
labels/train/   YOLO-format labels, 1:1 with images/train
labels/val/     YOLO-format labels, 1:1 with images/val
args.yaml       Training run configuration (task, model, hyperparameters)
best (1).pt     Best checkpoint from this hybrid run
last.pt         Final-epoch checkpoint
results.csv     Per-epoch training/validation metrics
results.png     Training curves (loss, mAP, precision, recall)
confusion_matrix.png, confusion_matrix_normalized.png
BoxP_curve.png, BoxR_curve.png, BoxF1_curve.png, BoxPR_curve.png
labels.jpg, train_batch*.jpg, val_batch*_labels.jpg, val_batch*_pred.jpg
    Ultralytics-generated training/validation visualizations
```

## Reproducing this run

`args.yaml` records the exact configuration used (`model: yolov8s.pt`,
100 epochs, batch 16, imgsz 640, seed 0), including `data: data_hybrid.yaml`
as the dataset config it was trained against.

**Status:** `data_hybrid.yaml` and `train_hybrid.py` are both committed to
this repository (`nc: 10`, class list matching the table above, paths set to
`images/train`/`images/val` in this repo). The documented command below runs
from a fresh clone:

```bash
python train_hybrid.py --data data_hybrid.yaml
```

## Class imbalance — disclosed, not hidden

`person` has roughly 40x more boxes than `laptop` or `bicycle`, mirroring
COCO's natural frequency rather than a sampling bug. Expect materially lower
precision/recall on the rarer classes (laptop, bicycle, backpack) than on
person/pole/stairs — see MANIFEST.md for exact per-class train/val box counts.
