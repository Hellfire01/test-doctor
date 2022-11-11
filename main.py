import sys
from src.test_doctor import TestDoctor


def main():
    test_doctor = TestDoctor()
    # This is the cli usage but you can use a hardcoded set of instructions should you wish to integrate in a program
    print(test_doctor.analyse(sys.argv))


if __name__ is "__main__":
    main()
