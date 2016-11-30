from ConfigParser import ConfigParser

CONFIG_DIR = '/Users/cary/Projects/headway_consulting/configs/'

class BaseConfig(ConfigParser):

    def __str__(self):
        return self.__class__.__name__.lower()

    def __init__(self, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        self.read(CONFIG_DIR + '{}.cfg'.format(str(self)))


class Main(BaseConfig):
    pass


class Assembler(BaseConfig):
    pass


class Tests(BaseConfig):
    pass


if __name__ == '__main__':
    print Tests().get('XML_VALIDATION', 'test_dir')
    assembler = Assembler()
    print assembler.get('APPLICATION', 'app_dir')
    print assembler.get('APPLICATION', 'data_dir')
