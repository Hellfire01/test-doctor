import argparse
from src.test_doctor_dataclasses import TestDoctorInstructions


class TestDoctorCLI:
    def __init__(self):
        self.parser = None
        self.__configure_cli()

    def __configure_cli(self):
        self.parser = argparse.ArgumentParser(
            prog="Test doctor",
            description="A software designed to allow you to analyse your test results",
        )
        self.parser.add_argument("-f", "--file", type=str, help="the path of the junit xml file to analyse", required=True)
        self.parser.add_argument("-r", "--root", type=str, help="the starting from witch the tests are analysed, the others are ignored. Default=None", required=False)
        self.parser.add_argument("-dr", "--disable-auto-root", help="If given, prevents the test doctor from automatically finding a root with morethan one test / directory", action="store_true", required=False)
        self.parser.add_argument("-s", "--slow-test-threshold", type=float, help="The value at witch the tests are determined to be slow. Default=1", default=1, required=False)
        self.parser.add_argument("-dg", "--disable-show-graph", help="If given, will disable the graph display windows ( compatible with the --save-graph-path argument )")
        self.parser.add_argument("-p", "--save-graph-path", type=str, help="If given, will save the graph at the given path. Default=None", required=False)

    def __get_namespace(self, args: [str]) -> argparse.Namespace:
        return self.parser.parse_args(args)

    def get_instructions(self, args: [str]) -> TestDoctorInstructions:
        namespace = self.__get_namespace(args)
        print(namespace)
        instructions = TestDoctorInstructions(

        )
        return instructions
