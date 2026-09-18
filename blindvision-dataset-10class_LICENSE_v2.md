# License

This repository mixes original project files with third-party image data under different terms. No single blanket license applies to everything in `images/`.

## Original files (this repository's own content)

`MANIFEST.md`, `README.md`, `HYBRID_DATA_DISCLOSURE.md`, `args.yaml`, `results.csv`, and `last.pt` (the trained checkpoint weights) are released under the **MIT License**:

> Copyright (c) 2026 [author name]
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of these files and associated documentation, to deal in them without restriction, including the rights to use, copy, modify, merge, publish, distribute, and/or sublicense copies, subject to inclusion of this notice in all copies.
>
> THESE FILES ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

## Third-party image subsets — each keeps its source's own terms

This repository does **not** have the authority to relicense third-party source images, and does not attempt to. Per-class sourcing is in `MANIFEST.md`; the terms are:

| Source | Classes | License |
|---|---|---|
| COCO 2017 (via FiftyOne) | person, chair, backpack, laptop, bottle, vehicle, bicycle | COCO Terms of Use — see https://cocodataset.org/#termsofuse |
| DoorDetect-Dataset (github.com/MiguelARD/DoorDetect-Dataset) | door | **No LICENSE file in the source repository.** Verified directly against the source: its README states the images are drawn from Open Images Dataset V4 and MCIndoor20000, with door/handle/cabinet-door/refrigerator-door bounding-box annotations added by the dataset's author; the only stated condition is a request to cite the associated paper. The underlying Open Images V4 photographs are individually CC BY 2.0 per Google's Open Images terms, but the curated, annotated DoorDetect-Dataset release itself carries no explicit redistribution license from its author. A third-party Roboflow mirror of this dataset displays "CC BY 4.0," but that is Roboflow's own default tag on an unofficial re-upload, not a license grant by the original author — treat it as unverified, not as authoritative. Do not redistribute this subset beyond citation-only use without contacting the dataset's author for explicit permission, or replacing it with a retrieval script pointing at the original repository instead of shipping the images directly. |
| Roboflow "PoleDetection" (mak-fatima fork, v1) | pole | CC BY 4.0 |
| Roboflow "Stairs_Detection" (mak-fatima fork, v1) | stairs | MIT |

If you redistribute the merged `images/`/`labels/` folders, you are redistributing a mix of licenses, not one license — carry this table forward with any copy you make. The door subset specifically should not be treated as clearly redistributable; see the recommendation above.
