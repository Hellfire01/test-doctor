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
    def get_console_output(tests: [TestCase]):
        tests.sort()
        ret = f"There are a total of {len(tests)} tests requiring {ConsoleOutput.get_total_test_time(tests)} to run"
        return ret
