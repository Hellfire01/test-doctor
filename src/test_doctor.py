

class TestDoctor:
    def __init__(self, file_content: str, root: str, disable_auto_root: bool, slow_test_threshold: float,
                 save_graph_path: str, disable_show_graph: bool):
        self.file_content = file_content
        self.root = root
        self.disable_auto_root = disable_auto_root
        self.slow_test_threshold = slow_test_threshold
        self.disable_show_graph = disable_show_graph
        self.save_graph_path = save_graph_path

    def analyse(self):
        # check received instructions
        # parse file or file content
        # build tree from tests
        # analyse tree
        # console output
        # matplotlib output
        # return copy of the console output
        pass
