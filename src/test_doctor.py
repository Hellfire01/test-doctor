import xml.etree.ElementTree as et
from src.test_doctor_dataclasses import TestCase, TestNode
from src.console_output import ConsoleOutput


class TestDoctor:
    def __init__(self, file_content: str, root: str, disable_auto_root: bool, slow_test_threshold: float,
                 top: int, save_graph_path: str, disable_show_graph: bool, disable_output: bool):
        self.file_content = file_content
        self.root = root
        self.disable_auto_root = disable_auto_root
        self.slow_test_threshold = slow_test_threshold
        self.top = top
        self.disable_show_graph = disable_show_graph
        self.save_graph_path = save_graph_path
        self.disable_output = disable_output

    def __get_test_list(self) -> [TestCase]:
        tests = []
        tree = et.ElementTree(et.fromstring(self.file_content))
        root = tree.getroot()
        for test_suite in root:
            for test in test_suite:
                buffer = TestCase(name=test.attrib['name'],
                                  path=test.attrib['classname'],
                                  time=float(test.attrib['time']))
                tests.append(buffer)
        return tests

    def __recursive_insert_test_tree(self, test_case: TestCase, name: str, parent):
        if name == "":  # end of the branch
            node = TestNode(test_case.name)
            node.total_time = test_case.time
            parent.insert(node)
            return
        else:  # need more insertion
            split = name.split('.')
            # does the branch already exist ?
            buff = parent.is_in(split[0])
            if buff is None:
                node = TestNode(split[0])
                parent.insert(node)
                self.__recursive_insert_test_tree(test_case, ".".join(split[1:]), node)
                return
            else:  # use existing branch
                parent.total_time += test_case.time
                self.__recursive_insert_test_tree(test_case, ".".join(split[1:]), buff)
                return

    def __get_test_tree(self, tests: [TestCase]) -> TestNode:
        root = TestNode("")  # create root test node
        for test in tests:
            self.__recursive_insert_test_tree(test, test.path, root)
        return root

    def __console_output(self, tests: [TestCase]) -> str:
        return ConsoleOutput.get_console_output(tests, self.slow_test_threshold, self.top)

    def __plot_graph(self):
        pass

    def __find_valid_root(self, root: TestNode) -> TestNode:
        if len(root.children) == 1:
            return self.__find_valid_root(root.children[0])
        return root

    def analyse(self) -> str:
        tests = self.__get_test_list()
        root = self.__get_test_tree(tests)
        ret = self.__console_output(tests)
        if self.disable_output is not True:
            print(ret)
        if self.disable_auto_root is not True:
            root = self.__find_valid_root(root)
        # analyse tree
        # matplotlib output
        # return copy of the console output
        return ret
