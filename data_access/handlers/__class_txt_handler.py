from data_access.handlers.__class_abstract_handler import AbstractHandler


class Txt(AbstractHandler):
    def __init__(self, link, work_dir=None):
        super().__init__(link, work_dir=work_dir)

    def get(self):
        with open(self.link) as file:
            return file.read()

    def put(self, data: str = None):
        with open(self.link, 'w') as file:
            file.write(data)
