import sys
from src.test_doctor import TestDoctor
from src.test_doctor_cli import TestDoctorCLI


def main():
    # This is the cli usage but you can call the test doctor directly should you wish to integrate it
    test_doctor_cli = TestDoctorCLI()
    instructions = test_doctor_cli.get_instructions(sys.argv)
    test_doctor = TestDoctor(file_content=instructions.report_contents,
                             root=instructions.root,
                             disable_auto_root=instructions.disable_auto_root,
                             slow_test_threshold=instructions.slow_test_threshold,
                             top=instructions.top,
                             save_graph_path=instructions.save_graph_path,
                             disable_show_graph=instructions.disable_show_graph,
                             disable_output=instructions.disable_console)
    test_doctor.analyse()


if __name__ == "__main__":
    main()
