from data_access._class_local_access import LocalHandler


class UniversalHandler:

    def __init__(self, link, work_dir=None):
        self.handler = LocalHandler(link, work_dir=work_dir)

