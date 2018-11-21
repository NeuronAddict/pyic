from abc import abstractmethod, ABCMeta


class StringFinder(metaclass=ABCMeta):
    @abstractmethod
    def read_string(self, sql):
        pass

    @abstractmethod
    def read_file(self, filename):
        pass
