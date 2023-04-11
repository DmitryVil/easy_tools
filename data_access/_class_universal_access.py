from data_access._class_local_access import LocalAccess


class UniversalAccess:

    def __init__(self, link, work_dir=None):
        self.handler = LocalAccess(link, work_dir=work_dir)

