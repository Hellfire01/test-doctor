from dataclasses import dataclass


@dataclass
class Test:
    name: str
    path: str
    time: float


@dataclass
class TestDoctorInstructions:
    # path of the report to analyse
    file_name: str
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
    graph_save_path: str
    # allows to display or not the graph
    display_graph: bool
