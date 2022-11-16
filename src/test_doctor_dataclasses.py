import humanize
import datetime
from dataclasses import dataclass


@dataclass
class TestCase:
    name: str
    path: str
    time: float

    def __gt__(self, other):
        return self.time < other.time

    def __str__(self):
        delta = datetime.timedelta(seconds=self.time)
        return f"{self.path}.{self.name} : {humanize.precisedelta(delta)}"


class TestNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.total_time = 0

    def is_in(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def insert(self, test_case):
        self.children.append(test_case)
        self.total_time += test_case.total_time

    def __str__(self):
        return f"{self.name} / {self.total_time} / {len(self.children)}"


@dataclass
class TestDoctorInstructions:
    # contents of the file ( mutually exclusive with the file_name arg )
    report_contents: str
    # starting point from witch the tests should be analysed. Allows to ignore the tests that do not match
    root: str
    # prevent auto parsing of the tests if enabled. By default the test doctor will attempt to find the first module
    # with mode than one test and / or module
    disable_auto_root: bool
    # show the top worst X tests in the console. used to present flooding of the console
    top: int
    # value at witch the tests are determined to be slow
    slow_test_threshold: float
    # should the graph need to be saved as a picture, you can give a path
    save_graph_path: str
    # allows to display or not the graph
    disable_show_graph: bool
    # enables or disables the console display of the test doctor.
    # The test doctor will still return the console output as a string
    disable_console: bool

    def __no_none(self, value):
        if type(value) is None:
            return "None"
        return value

    def __str__(self):
        ret = f"file contents : '{self.report_contents}'\n"
        ret += f"root : {self.__no_none(self.root)}\n"
        ret += f"disable_auto_root: {self.__no_none(self.disable_auto_root)}\n"
        ret += f"slow test threshold: {self.__no_none(self.slow_test_threshold)}\n"
        ret += f"save graph path: {self.__no_none(self.save_graph_path)}\n"
        ret += f"disable show graph: {self.__no_none(self.disable_show_graph)}\n"
        return ret
