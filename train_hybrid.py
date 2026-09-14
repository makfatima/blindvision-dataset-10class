#!/usr/bin/env python

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args():
    p = argparse.ArgumentParser(description="Train YOLOv8 on the BlindVision hybrid 10-class dataset")
    p.add_argument("--data", type=str, default="data_hybrid.yaml",
                    help="Path to the dataset YAML (default: data_hybrid.yaml)")
    p.add_argument("--model", type=str, default="yolov8s.pt",
                    help="Base model/checkpoint to start from")
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--batch", type=int, default=16)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--device", type=str, default="0",
                    help="CUDA device id, or 'cpu'")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--patience", type=int, default=100)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--project", type=str, default="/kaggle/working/runs",
                    help="Output directory for run artifacts. On Kaggle this is "
                         "typically under /kaggle/working/; change it if running "
                         "locally or in a different notebook environment.")
    p.add_argument("--name", type=str, default="blindvision_hybrid",
                    help="Run name (subfolder under --project)")
    p.add_argument("--resume", action="store_true", default=False)
    return p.parse_args()


def main():
    args = parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset config not found: {data_path}. "
            f"Make sure data_hybrid.yaml is present in the working directory "
            f"(or pass --data with the correct path) before running."
        )

    model = YOLO(args.model)

    model.train(
        data=str(data_path),
        epochs=args.epochs,
        batch=args.batch,
        imgsz=args.imgsz,
        device=args.device,
        workers=args.workers,
        patience=args.patience,
        seed=args.seed,
        deterministic=True,
        single_cls=False,
        rect=False,
        cos_lr=False,
        close_mosaic=10,
        resume=args.resume,
        amp=True,
        fraction=1.0,
        optimizer="auto",
        pretrained=True,
        cache=False,
        save=True,
        save_period=-1,
        exist_ok=False,
        verbose=True,
        project=args.project,
        name=args.name,
    )


if __name__ == "__main__":
    main()
