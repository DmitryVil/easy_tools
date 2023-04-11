from data_access.handlers.__class_feather_handler import Feather
from data_access.handlers.__class_pickle_handler import Pickle
from data_access.handlers.__class_yaml_handler import Yaml
from data_access.handlers.__class_toml_handler import Toml
from data_access.handlers.__class_json_handler import Json
from data_access.handlers.__class_txt_handler import Txt


class UniversalFileHandler:
    file_handler_pointer = {
        '': Txt,
        '.txt': Txt,
        '.yaml': Yaml,
        '.toml': Toml,
        '.json': Json,
        '.pickle': Pickle,
        '.pkl': Pickle,
        '.feather': Feather,
        '.fthr': Feather
    }

    def __init__(self, file_type):
        self.file_type = file_type

    def get_file_handler(self):
        # If handler class is not recognized, assuming it is the class Txt
        return self.file_handler_pointer.get(self.file_type, Txt)

