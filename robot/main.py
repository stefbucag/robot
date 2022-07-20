"""Toy Robot"""
from argparse import ArgumentParser
from re import compile,X

from robot.robot import Robot
from robot.point import Point
from robot.table import Table


def get_arg_parser():
    """Get arguments from the command line."""
    description = "Retrieve user input file."

    parser = ArgumentParser(description=description)
    parser.add_argument('input', type=str, help='Input text file')
    parser.add_argument('--filname', type=str, help='Textfile filename')

    return parser

def parse_input_file(file):
    """Retrieve the commands from the input file."""
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    pattern = compile(
                r"""(?<=^)                                # start
                (?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
                (?=\s?                                    # space
                (?P<x>\d+),                               # x coordinate
                (?P<y>\d+),                               # y coordinate
                (?P<dir>NORTH|EAST|SOUTH|WEST)            # direction
                $))                                       # EOL
                """, X)

    # Table with dimensions of dimensions 5 units x 5 units
    table = Table(Point(0,0),Point(4,4))
    robot = Robot(directions = directions)

    with open(file) as f:
        for line in f:
            command = pattern.match(line.rstrip('\n'))
            if command is not None and command.group("cmd") == "PLACE":
                robot = robot.place(Point(float(command.group("x")),
                                          float(command.group("y"))),
                                          directions.index(command.group("dir"))/2.0,
                                          table)
            elif command is not None and hasattr(robot, command.group("cmd").lower()):
                robot = getattr(robot, command.group("cmd").lower())()


def __run():
    """Run Toy Robot."""
    arg_parser = get_arg_parser()
    options = arg_parser.parse_args()

    parse_input_file(options.input)

if __name__ == '__main__':
    __run()
