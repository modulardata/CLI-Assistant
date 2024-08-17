import os
from hstest import *


class CliTest(StageTest):
    @dynamic_test()
    def test_1(self):

        with open("data.txt", "w") as file:
            file.write("Some text of data")

        main = TestedProgram()
        output = main.start("--exist=data.txt")

        os.remove("data.txt")

        solution = "The file data.txt exists!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_2(self):
        main = TestedProgram()
        output = main.start("--create=audio")

        is_dir = os.path.isdir("audio")

        solution = "The folder audio was created!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)
        if is_dir:
            return CheckResult.correct()

    @dynamic_test()
    def test_3(self):
        main = TestedProgram()
        output = main.start("--create=videos/first_video")

        is_dir = os.path.isdir("videos/first_video")

        solution = "The folders videos/first_video were created!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)
        if is_dir:
            return CheckResult.correct()

    @dynamic_test()
    def test_4(self):
        main = TestedProgram()
        output = main.start("--remove=audio")

        is_exist = os.path.exists("audio")

        solution = "The folder audio was deleted!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)
        if not is_exist:
            return CheckResult.correct()

    @dynamic_test()
    def test_5(self):
        main = TestedProgram()
        output = main.start("--remove=videos/first_video")

        is_exist = os.path.exists("videos/first_video")

        solution = "The folder videos in first_video folder was deleted!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)
        if not is_exist:
            return CheckResult.correct()

    @dynamic_test()
    def test_6(self):
        main = TestedProgram()
        output = main.start("--remove=fake_folder")

        is_exist = os.path.exists("fake_folder")

        solution = "This fake_folder folder doesn't exist!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        # delete videos folder because it should not exist after tests
        if os.path.exists("videos"):
            os.rmdir("videos")

        if not is_exist:
            return CheckResult.correct()


if __name__ == '__main__':
    CliTest().run_tests()
