# Toy Robot Code Challenge

## Overview:
The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.

### Technical requirement:
Please use Python 3.x

### Installation
1. Clone repository
    ```
    $ git clone git@github.com:stefbucag/robot.git
    $ cd robot
    ```
2. Install virtual environment
    ```
    $ virtualenv .virtualenv
    ```
3. Lastly, execute code
    ```
    python setup.py develop
    ```

### To use the Toy Robot
- Activate virtual environment and run command:
    ```
    python -m robot.main [location-of-the-input-file/filename]
    ```

## Code Challenge Details
- Create a console application that can read in commands of the following form
    ```
        PLACE X,Y,F
        MOVE
        LEFT
        RIGHT
        REPORT
    ```

- **PLACE** will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.

- **MOVE** will move the toy robot one unit forward in the direction it is currently facing.

- **LEFT** and **RIGHT** will rotate the robot 90 degrees in the specified direction without changing the position of the robot. 

- **REPORT** will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.

- A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. Input can be from a file, or from standard input, as the developer chooses.

### Constraints
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. **Any move that would cause the robot to fall must be ignored.**

### Example Input and Output:
- First example
    ```
    PLACE 0,0,NORTH
    MOVE
    REPORT
    ```

    **Output:** 0,1,NORTH

- Second example
    ```
    PLACE 0,0,NORTH
    LEFT
    REPORT
    ```

    **8Output:** 0,0,WEST

- Third example
    ```
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    ```

    **Output:** 3,3,NORTH

- Fourth example: Ignore any move that would cause the robot to fall from the table. Initial place of the robot is outside the table's boundary
    ```
    PLACE 8,9,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    ```

    **Output:** _none_

- Fifth example: No use of REPORT command
    ```
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    ```

    **Output:** _none_
