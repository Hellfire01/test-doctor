import humanize
import datetime
from src.test_doctor_dataclasses import TestCase


class ConsoleOutput:
    @staticmethod
    def __display_time(time: float) -> str:
        delta = datetime.timedelta(seconds=time)
        return humanize.precisedelta(delta)

    @staticmethod
    def __get_total_test_time(tests: [TestCase]) -> float:
        time = 0
        for test in tests:
            time += test.time
        return time

    @staticmethod
    def __counter_buffer(index: int, str_top: str) -> str:
        ret = str(index)
        while len(ret) < len(str_top):
            ret = f" {ret}"
        return ret

    @staticmethod
    def __separate_tests(tests: [TestCase], slow_test_threshold: float) -> ([TestCase], [TestCase]):
        slow = []
        good = []
        for test in tests:
            if test.time >= slow_test_threshold:
                slow.append(test)
            else:
                good.append(test)
        return slow, good

    @staticmethod
    def __slow_tests_display(slow_tests: [TestCase], good_tests: [TestCase], slow_test_threshold: float) -> str:
        good_time = ConsoleOutput.__get_total_test_time(good_tests)
        good_time_test = good_time / len(good_tests)
        slow_time = ConsoleOutput.__get_total_test_time(slow_tests)
        slow_time_test = slow_time / len(slow_tests)
        total_time = good_time + slow_time
        ret = f"There are a total of {len(slow_tests)} tests with a time of more or equal than {ConsoleOutput.__display_time(slow_test_threshold)}\n"
        ret += f"The slow tests amount to {ConsoleOutput.__display_time(slow_time)} witch represents {round(slow_time / total_time * 100, 2)}% of the total run time"
        ret += f" with an average of {ConsoleOutput.__display_time(slow_time_test)} per test\n\n"
        ret += f"There are a total of {len(good_tests)} test with a time of less than {ConsoleOutput.__display_time(slow_test_threshold)}\n"
        ret += f"The good tests amount to {ConsoleOutput.__display_time(good_time)} witch represents {round(good_time / total_time * 100, 2)}% of the total run time"
        ret += f" with an average of {ConsoleOutput.__display_time(good_time_test)} per test\n\n"
        gain = total_time - (len(slow_tests) * good_time_test + good_time)
        ret += f"Getting the slow tests to run as fast as the good tests would result in a gain of {ConsoleOutput.__display_time(gain)}\n"
        ret += f"This amounts to a gain of {round(gain / total_time * 100, 2)}% of run time\n"
        return ret

    @staticmethod
    def __no_slow_tests(slow_test_threshold: float) -> str:
        ret = f"There are no tests with an execution time of more than {ConsoleOutput.__display_time(slow_test_threshold)}\n"
        return ret

    @staticmethod
    def get_console_output(tests: [TestCase], slow_test_threshold: float, top: int):
        tests.sort()
        ret = f"\nThere are a total of {len(tests)} tests requiring {ConsoleOutput.__display_time(ConsoleOutput.__get_total_test_time(tests))} to run\n"
        ret += f"slowest tests sorted by decreasing order :\n\n"
        str_top = str(top)
        for i in range(0, top):
            ret += f"{ConsoleOutput.__counter_buffer(i + 1, str_top)} : {tests[i]}\n"
        ret += "\n"
        slow_tests, good_tests = ConsoleOutput.__separate_tests(tests, slow_test_threshold)
        if len(slow_tests) == 0:
            ret += ConsoleOutput.__no_slow_tests(slow_test_threshold)
        else:
            ret += ConsoleOutput.__slow_tests_display(slow_tests, good_tests, slow_test_threshold)
        return ret
