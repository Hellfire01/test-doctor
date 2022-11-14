import sys
from src.test_doctor import TestDoctor
from src.test_doctor_cli import TestDoctorCLI


def main():
    # This is the cli usage but you can call the test doctor directly should you wish to integrate it
    test_doctor_cli = TestDoctorCLI()
    instructions = test_doctor_cli.get_instructions(sys.argv)
    test_doctor = TestDoctor(instructions.report_contents,
                             instructions.root,
                             instructions.disable_auto_root,
                             instructions.slow_test_threshold,
                             instructions.save_graph_path,
                             instructions.disable_show_graph)
    test_doctor.analyse()


if __name__ == "__main__":
    main()
