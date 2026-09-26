# BlindVision — Hybrid 10-Class Dataset & Training Artifacts

> **Scope:** This repository is a reproducibility release for a **separate hybrid 10-class YOLOv8s training run**. It must not be treated as the source of every metric reported elsewhere in the BlindVision manuscript. The run uses 2,380 training images and 492 validation images assembled from public sources. See [MANIFEST.md](MANIFEST.md) for provenance, licensing, and class counts.

## Classes

| ID | Class | Source |
|---:|---|---|
| 0 | person | COCO 2017 |
| 1 | door | DoorDetect-Dataset |
| 2 | chair | COCO 2017 |
| 3 | backpack | COCO 2017 |
| 4 | laptop | COCO 2017 |
| 5 | bottle | COCO 2017 |
| 6 | pole | Roboflow PoleDetection |
| 7 | vehicle | COCO 2017 (car) |
| 8 | bicycle | COCO 2017 |
| 9 | stairs | Roboflow Stairs_Detection |

## Released artifacts

The repository contains the dataset, training configuration, trained checkpoints, epoch-wise log, and Ultralytics evaluation/training plots.

~~~text
images/train/                 2,380 training images
images/val/                     492 validation images
labels/train/                 YOLO-format labels
labels/val/                   YOLO-format labels
data_hybrid.yaml              Dataset configuration
train_hybrid.py               Reproduction script
args.yaml                     Recorded Ultralytics training arguments
best (1).pt                   Best checkpoint from this run
last.pt                       Final-epoch checkpoint
results.csv                   100-epoch training/validation log
results.png                   Training curves
confusion_matrix*.png         Confusion matrices
Box*_curve.png                Precision/recall/F1/PR curves
~~~

The checkpoint filenames retain their original recorded names (`best (1).pt` and `last.pt`) so the released artifacts can be traced directly to the completed training run.

## Reproducing this run

The recorded run used:
- Model: YOLOv8s pretrained checkpoint (`yolov8s.pt`)
- Epochs: 100
- Batch size: 16
- Image size: 640
- Seed: 0
- Deterministic training: enabled
- AMP: enabled
- Workers: 8
- Dataset configuration: `data_hybrid.yaml`
- Training script: `train_hybrid.py`

Re-run from a fresh clone on a compatible GPU:

~~~bash
python train_hybrid.py --data data_hybrid.yaml
~~~

The complete recorded argument set is in [args.yaml](args.yaml). Because the original execution environment did not capture a complete lockfile, this repository **does not claim an exact package-level environment reproduction**. Do not infer exact Ultralytics/PyTorch versions unless they are independently recorded.

## Training result recorded in results.csv

The committed `results.csv` is the authoritative epoch-wise record for this hybrid run. At epoch 100 it records approximately:
- Precision: 67.63%
- Recall: 48.40%
- mAP@0.50: 50.23%
- mAP@0.50:0.95: 33.24%

These values describe this **hybrid YOLOv8s run only**. They must not be substituted for, or merged with, results from another training/evaluation experiment.

## Reproducibility and provenance

`MANIFEST.md` documents source datasets, class-level box counts, licenses, class imbalance, and the distinction between this hybrid release and the earlier/original dataset configuration.

For a complete experiment audit, preserve together:
1. The repository commit containing the dataset/configuration.
2. `args.yaml`.
3. `results.csv`.
4. The released checkpoints.
5. The generated evaluation plots.
6. The exact manuscript/table that cites the experiment.

## Class imbalance

The dataset is intentionally documented as imbalanced. `person` has substantially more boxes than rare classes such as `laptop` and `bicycle`. Per-class metrics should therefore be reported when this run is used for analysis.

## Citation

The door subset is redistributed with the permission of the DoorDetect author, on condition of citation ([Issue #4](https://github.com/MiguelARD/DoorDetect-Dataset/issues/4)). If you use it, cite:

~~~bibtex
@article{Arduengo_2021,
  title   = {Robust and adaptive door operation with a mobile robot},
  author  = {Arduengo, Miguel and Torras, Carme and Sentis, Luis},
  journal = {Intelligent Service Robotics},
  year    = {2021},
  doi     = {10.1007/s11370-021-00366-7}
}
~~~

## License and source attribution

The merged dataset contains components with different source licenses and terms. Follow the source-specific terms documented in [MANIFEST.md](MANIFEST.md) and [LICENSE.md](LICENSE.md); do not describe the entire merged dataset as being covered by one blanket upstream license.