from abc import ABC, abstractmethod
from pathlib import Path
from data_access.handlers.__class_universal_handler import UniversalFileHandler


class AbstractAccess(ABC):
    # It is abstract class for data access
    def __init__(self, link, work_dir=None):
        self.link = Path(link)
        self.link_folder = self.link.parent
        self.work_dir = Path(work_dir) if work_dir else None
        self.file_type = self.file_type_recognition()
        self.local_file_handler = UniversalFileHandler(self.file_type).get_file_handler()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    def file_type_recognition(self):
        return self.link.suffix
