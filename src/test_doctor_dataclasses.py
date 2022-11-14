from dataclasses import dataclass


@dataclass
class Test:
    name: str
    path: str
    time: float


@dataclass
class TestDoctorInstructions:
    # contents of the file ( mutually exclusive with the file_name arg )
    file_contents: str
    # starting point from witch the tests should be analysed. Allows to ignore the tests that do not match
    root: str
    # prevent auto parsing of the tests if enabled. By default the test doctor will attempt to find the first module
    # with mode than one test and / or module
    disable_auto_root: bool
    # value at witch the tests are determined to be slow
    slow_test_threshold: float
    # should the graph need to be saved as a picture, you can give a path
    save_graph_path: str
    # allows to display or not the graph
    disable_show_graph: bool

    def __no_none(self, value):
        if type(value) is None:
            return "None"
        return value

    def __str__(self):
        ret = f"file contents : '{self.file_contents}'\n"
        ret += f"root : {self.__no_none(self.root)}\n"
        ret += f"disable_auto_root: {self.__no_none(self.disable_auto_root)}\n"
        ret += f"slow test threshold: {self.__no_none(self.slow_test_threshold)}\n"
        ret += f"save graph path: {self.__no_none(self.save_graph_path)}\n"
        ret += f"disable show graph: {self.__no_none(self.disable_show_graph)}\n"
        return ret
