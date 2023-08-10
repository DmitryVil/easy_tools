import pickle
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Pickle(AbstractHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        with open(self.link, "rb") as binary_file:
            data = pickle.load(binary_file)
        return data

    def put(self, data=None):
        with open(self.link, 'wb') as binary_file:
            pickle.dump(data, binary_file)
