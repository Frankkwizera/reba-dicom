__author__ = "Frank Kwizera"

import pydicom


class Utils:
    @staticmethod
    def read_dicom_file(dicom_file_path: str) -> pydicom.dataset.FileDataset:
        return pydicom.dcmread(dicom_file_path)