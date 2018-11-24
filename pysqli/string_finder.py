from abc import abstractmethod, ABCMeta


class StringFinder(metaclass=ABCMeta):
    """
    A string finder is a class that can extract a string from the database via a technique.

    see BlindStringFinder to use a Blind technique or UnionStringFinder to use the union based technique.
    """
    @abstractmethod
    def read_string(self, sql):
        """
        read a string
        :param sql: sql code to read as a string
        :return: string read, or None if not possible (can be a NULL, string, you must make another test to be sure)
        """
        pass

    @abstractmethod
    def read_file(self, filename):
        """
        Read a file.
        :param filename: file to read
        :return: Content of the file, or None if it can be read (it can be that it not exsists, or don't be accessible)
        """
        pass
