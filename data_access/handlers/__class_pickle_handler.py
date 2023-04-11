import pickle
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Pickle(AbstractHandler):
    def __init__(self, link, work_dir=None):
        super().__init__(link, work_dir=work_dir)

    def get(self):
        pass

    def put(self, data=None):
        pass
