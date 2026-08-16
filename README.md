# reba-dicom

A Python package for reading, converting, and inspecting DICOM medical imaging files.

## Features

- Read DICOM files (`.dcm`) via `pydicom`
- Visualize a DICOM image's pixel array
- Export a DICOM image's pixel array to PNG
- Export a DICOM dataset's metadata to JSON

## Install

```bash
pip install rebadicom
```

## Usage

```python
from rebadicom.image import Image

image = Image("path/to/file.dcm")
image.show()               # display pixel array
image.save("out.png")      # export pixel array to PNG
image.to_json("out.json")  # export metadata to JSON
```
