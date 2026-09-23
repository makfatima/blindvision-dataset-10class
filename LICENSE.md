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
| DoorDetect-Dataset (github.com/MiguelARD/DoorDetect-Dataset) | door | **Redistribution permission granted by the dataset's author, with citation.** The source repository has no LICENSE file; permission to redistribute this subset (with citation to the DoorDetect paper) was requested and granted directly by the repository owner, github.com/MiguelARD, in [Issue #4](https://github.com/MiguelARD/DoorDetect-Dataset/issues/4) of the source repository ("I'm using this dataset's door images in a public GitHub repo for a university project... would you be okay with me redistributing them, with citation?" — MiguelARD: "yes", 2026). This is a real, attributable grant from the dataset's own maintainer, not an inferred or third-party license. Citation to the DoorDetect paper is required, per the terms of that request. |
| Roboflow "PoleDetection" (mak-fatima fork, v1) | pole | CC BY 4.0 |
| Roboflow "Stairs_Detection" (mak-fatima fork, v1) | stairs | MIT |

If you redistribute the merged `images/`/`labels/` folders, you are redistributing a mix of licenses, not one license — carry this table forward with any copy you make. The door subset is now clearly redistributable with citation, per the granted permission above; the other subsets' own terms in the table still apply independently.
