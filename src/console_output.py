import humanize
import datetime
from src.test_doctor_dataclasses import TestCase


class ConsoleOutput:
    @staticmethod
    def get_total_test_time(tests: [TestCase]) -> str:
        time = 0
        for test in tests:
            time += test.time
        delta = datetime.timedelta(seconds=time)
        return humanize.precisedelta(delta)

    @staticmethod
    def __counter_buffer(index: int, str_top: str) -> str:
        ret = str(index)
        while len(ret) < len(str_top):
            ret = f" {ret}"
        return ret

    @staticmethod
    def get_console_output(tests: [TestCase], slow_test_threshold: float, top: int):
        tests.sort()
        ret = f"There are a total of {len(tests)} tests requiring {ConsoleOutput.get_total_test_time(tests)} to run"
        str_top = str(top)
        for i in range(0, top):
            ret += f"{ConsoleOutput.__counter_buffer(i, str_top)} : {tests[i - 1]}\n"
        return ret
