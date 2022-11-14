import xml.etree.ElementTree as et
from src.test_doctor_dataclasses import TestCase, TestNode


class TestDoctor:
    def __init__(self, file_content: str, root: str, disable_auto_root: bool, slow_test_threshold: float,
                 save_graph_path: str, disable_show_graph: bool):
        self.file_content = file_content
        self.root = root
        self.disable_auto_root = disable_auto_root
        self.slow_test_threshold = slow_test_threshold
        self.disable_show_graph = disable_show_graph
        self.save_graph_path = save_graph_path

    def __get_test_list(self) -> [TestCase]:
        tests = []
        tree = et.ElementTree(et.fromstring(self.file_content))
        root = tree.getroot()
        for test_suite in root:
            for test in test_suite:
                buffer = TestCase(name=test.attrib['name'],
                                  path=test.attrib['classname'],
                                  time=test.attrib['time'])
                tests.append(buffer)
        return tests

    def __recursive_insert_test_tree(self, test_case: TestCase):
        pass

    def __get_test_tree(self, tests: [TestCase]) -> TestNode:
        root = TestNode()
        for test in tests:
            self.__recursive_insert_test_tree(test, root)

    def __console_output(self) -> str:
        pass

    def __plot_graph(self):
        pass

    def analyse(self):
        tests = self.__get_test_list()
        tree = self.__get_test_tree(tests)
        # parse file or file content
        # build tree from tests
        # analyse tree
        # console output
        # matplotlib output
        # return copy of the console output
        pass
