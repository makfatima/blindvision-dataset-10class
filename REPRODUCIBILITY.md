# Reproducibility Record

## Experiment identity

**Experiment:** BlindVision hybrid 10-class object-detection training run  
**Model:** YOLOv8s  
**Epochs:** 100  
**Training images:** 2,380  
**Validation images:** 492  
**Seed:** 0  
**Image size:** 640  
**Batch size:** 16

## Artifact inventory

| Artifact | Status | Purpose |
|---|---|---|
| `data_hybrid.yaml` | Released | Dataset/class/path configuration |
| `train_hybrid.py` | Released | Reproduction script |
| `args.yaml` | Released | Recorded Ultralytics training configuration |
| `results.csv` | Released | Epoch-wise training and validation metrics |
| `best (1).pt` | Released | Best checkpoint from the recorded run |
| `last.pt` | Released | Final checkpoint |
| `results.png` | Released | Training curves |
| `confusion_matrix.png` | Released | Confusion matrix |
| `confusion_matrix_normalized.png` | Released | Normalized confusion matrix |
| `BoxP_curve.png` | Released | Precision curve |
| `BoxR_curve.png` | Released | Recall curve |
| `BoxF1_curve.png` | Released | F1 curve |
| `BoxPR_curve.png` | Released | Precision-recall curve |
| Exact Python/package lockfile | Not captured | Must not be fabricated |
| Raw latency traces | Not part of this training release | Use separately documented system-evaluation artifacts |
| TensorBoard event files | Not captured in this release | Do not claim they are available |

## Reproduction command

~~~bash
python train_hybrid.py --data data_hybrid.yaml
~~~

The command is intended for a compatible GPU environment. The recorded `args.yaml` is the authoritative source for the training configuration.

## Important metric boundary

The committed `results.csv` is the authoritative training log for this experiment. It records approximately 67.63% precision, 48.40% recall, 50.23% mAP@0.50, and 33.24% mAP@0.50:0.95 at epoch 100.

Other BlindVision repositories may contain aggregate or manuscript-era evaluation records with different values. Those records must be assigned to their own experiment/evaluation provenance and must not be presented as reproduced results from this hybrid run without evidence establishing that relationship.

## Dataset provenance

The merged dataset contains COCO-derived classes, DoorDetect-Dataset data, and Roboflow-derived pole/stairs data. See `MANIFEST.md` for source-level provenance, licensing, and class counts.

## Environment transparency

The original run recorded the Ultralytics training arguments but did not preserve a complete package-version lockfile. Therefore this release deliberately avoids inventing an `environment.yml` or pinned `requirements.txt`. A future rerun should capture:
- Python version
- Ultralytics version
- PyTorch version
- torchvision version
- CUDA version
- GPU model
- operating-system/runtime information
- `pip freeze` or an equivalent environment lockfile

Those values should be added only from the actual execution environment.