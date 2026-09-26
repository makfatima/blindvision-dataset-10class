# hybrid_dataset — complete 10-class merge

## Full contents

| Class id | Name | Source | License | Train boxes | Val boxes |
|---|---|---|---|---|---|
| 0 | person | COCO 2017 (via FiftyOne, 1200/150 img sample) | COCO terms of use | 3,939 | 506 |
| 1 | door | DoorDetect-Dataset (github.com/MiguelARD/DoorDetect-Dataset) | Redistribution permitted with citation — author's direct written permission, see [LICENSE.md](LICENSE.md) and [source Issue #4](https://github.com/MiguelARD/DoorDetect-Dataset/issues/4) | 504 | 76 |
| 2 | chair | COCO 2017 | COCO terms of use | 630 | 118 |
| 3 | backpack | COCO 2017 | COCO terms of use | 129 | 16 |
| 4 | laptop | COCO 2017 | COCO terms of use | 81 | 9 |
| 5 | bottle | COCO 2017 | COCO terms of use | 395 | 40 |
| 6 | pole | Roboflow "PoleDetection" (mak-fatima fork, v1) | CC BY 4.0 | 667 | 179 |
| 7 | vehicle | COCO 2017 (`car` class) | COCO terms of use | 720 | 74 |
| 8 | bicycle | COCO 2017 | COCO terms of use | 111 | 7 |
| 9 | stairs | Roboflow "Stairs_Detection" (mak-fatima fork, v1) | MIT | 376 | 169 |

**2,380 training images, 492 validation images total.**

## Honest caveats to disclose, not hide

- **Class imbalance is real and significant** — person has ~40x more boxes
  than laptop or bicycle. This mirrors COCO's natural frequency (people are
  in almost every street/indoor scene; laptops and bicycles are rarer), not
  a sampling bug, but it means laptop/bicycle/backpack will likely have
  markedly lower precision/recall than person/pole/stairs in this run. Say
  so in the manuscript rather than only reporting an averaged mAP that
  hides it — per-class metrics (which `tools/metrics.py` already computes)
  are the right way to show this honestly.
- **COCO subset was capped at 1,200 train / 150 val images** (not the full
  118K/5K COCO), specifically because it only needs to cover 7 of COCO's 80
  classes — this keeps the dataset a reasonable size while still giving
  each of those 7 classes a real (if imbalanced) sample.
- Different classes come from three genuinely different sources with
  different license terms (see table). If you redistribute this dataset
  alongside your thesis/repo, each source's terms apply to its own subset —
  don't describe the merged folder under one blanket license.

## What this is NOT

This is **not a reconstruction of the original 5,600-image training set**
behind the manuscript's primary results (Tables II and IV). It is a separate,
secondary dataset assembled from public sources for an exploratory training
run, reported on its own in the manuscript (Table II-A).

## Training run

This run has already been completed (100 epochs, YOLOv8s, seed 0) and its
outputs are committed to this repository: `results.csv`, `args.yaml`,
`best (1).pt`, `last.pt`. To reproduce from a fresh clone:
```
python train_hybrid.py --data data_hybrid.yaml
```
on a GPU (Colab, with `Runtime → Change runtime type → GPU`, works fine).

## Filenames

`door_*` (DoorDetect), `pole_train_*`/`pole_valid_*`/`pole_test_*` (Roboflow),
`stairs_train_*`/`stairs_valid_*`/`stairs_test_*` (Roboflow),
`coco_train_*`/`coco_val_*` (COCO via FiftyOne).
