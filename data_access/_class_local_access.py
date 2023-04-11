import os
from data_access._class_abstract_access import AbstractAccess
import traceback


class LocalAccess(AbstractAccess):

    def __init__(self, link, work_dir=None):
        super().__init__(link, work_dir)

    def read_data(self):
        return self.local_file_handler(self.link).get()

    def write_data(self, data):
        if not self.link_folder.exists():
            os.makedirs(self.link_folder)
        self.local_file_handler(self.link).put(data)
