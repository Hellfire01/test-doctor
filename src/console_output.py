import humanize
import datetime
from src.test_doctor_dataclasses import TestCase


class ConsoleOutput:
    @staticmethod
    def get_total_test_time(tests: [TestCase]) -> float:
        ret = 0
        for test in tests:
            ret += test.time
        return ret

    @staticmethod
    def get_console_output(tests: [TestCase]):
        tests.sort()
        time = humanize.naturaldelta(datetime.timedelta(seconds=ConsoleOutput.get_total_test_time(tests)))
        ret = f"There are a total of {len(tests)} tests requiring {time} to run"
        return ret
