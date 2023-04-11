import toml
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Toml(AbstractHandler):
    def __init__(self, link, work_dir=None):
        super().__init__(link, work_dir=work_dir)

    def get(self):
        with open(self.link) as toml_file:
            return toml.load(toml_file)

    def put(self, data: dict = None):
        data = data if data else {}
        with open(self.link, 'w') as toml_file:
            result = toml.dump(data, toml_file)
        return result or data
