# softserve-python-course

## Description

This repo contains solutions for the Softserve's Python Elementary Tasks.  
Each package inside the *tasks* folder represents each task of the course.

The project was created using the Visual Studio Code (version 1.60.0) and Python 3.9.1.

## Installation

You can directly clone this project and try it for yourself:

    git clone https://github.com/gotoindex/softserve-python-course.git

## Usage

This project takes advantage of Python's *argparse*. To launch a task, call it in console using *python* or *python3* command:

    python3 path/to/file <arguments>

Example:

    python3 tasks/task1/method1.py 8 8

### Goals

During the development of the project following goals were achieved:
- Learned how to use following software and services:
  - [ ] [Django](https://www.djangoproject.com/)
  - [ ] [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Completed following tasks:
  - [ ] Task 1, "Chessboard"
  - [ ] Task 2, "Envelope Analysis"
  - [ ] Task 3, "Sorting Triangles"
  - [ ] Task 4, "File Parser"
  - [ ] Task 5, "Number to a Word"
  - [ ] Task 6, "Lucky Tickets"
  - [ ] Task 7, "Number Sequence"
  - [ ] Task 8, "Fibonacci Series for a Range"

Additional software and services used during the development:
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Task description

Here is a full description of all tasks:

> Note that this text was roughly translated to english and thus may contain simple mistakes.

1. Chessboard  
  Display a chessboard with the specified dimensions of height and width, according to the principle:  
  \* * * * * *   
  &nbsp;* * * * * *  
  \* * * * * *   
  &nbsp;* * * * * *  
  The program is launched by calling the main class with parameters.

2. Envelope Analysis  
  There are two envelopes with sides (a, b) and (c, d) determine if one envelope can be inserted into
  another. The program must handle floating point input. The program asks
  custom envelope sizes one setting at a time. After each calculation, the program
  asks the user if he wants to continue. If the user answers “y” or “yes” (without
  register), the program continues to work from the beginning, otherwise it ends execution.

3. Sorting Triangles  
  Develop a console program that prints triangles in descending order
  their area. After adding each new triangle, the program asks if it wants
  user add another one. If the user answers “y” or “yes” (case insensitive),
  the program will ask you to enter data for one more triangle, otherwise it outputs
  the result to the console.
  - The area of the triangle should be calculated using Heron's formula.
  - Each triangle is identified by the name and the lengths of its sides.
  Input format (comma delimited):  
  \<name\>, \<side length\>, \<side length\>, \<side length\>
  - The application must handle floating point input.
  - Input must be case insensitive, spaces, tabs.
  - Data output should be the following example:  
    ============= Triangles list: ===============
    1. [Triangle first]: 17.23 сm
    2. [Triangle 22]: 13 cm
    3. [Triangle 1]: 1.5 cm

4. File Parser  
  You need to write a program that will have two modes:  
    1. Count the number of occurrences of a line in a text file.
    2. Replace the line with another in the specified file  
  The program should accept arguments as input at startup:  
    1. \<path to file\> \<string for counting\>
    2. \<path to file\> \<string for searching\> \<string for replaceing\>

5. Number to a Word  
  You need to convert an integer to a word: 12 - twelve. Program
  is launched by calling the main class with parameters.

6. Lucky Tickets  
  There are 2 ways to count lucky tickets:
    1. Moscow - if a six-digit number is printed on the bus ticket, and the sum of the first
      of three digits is equal to the sum of the last three, then this ticket is considered lucky.
    2. Leningrad, or St. Petersburg - if the sum of the even digits of the ticket is equal to the sum of the odd
      numbers on the ticket, then the ticket is considered lucky.
  Task:
    The ticket number is a six-digit number. One needs to write a console application that can
    count the number of lucky tickets. To select the calculation algorithm, a text file is read.
    The path to the text file is set in the console after starting the program. Algorithm indicators:
    1 - the word 'Moskow'
    2 - the word 'Piter'
    After setting all the necessary parameters, the program should display the number of
    lucky tickets for the specified counting method.

7. Number Sequence  
  The program displays a series of natural numbers separated by commas, the square of which is less than a given
  n. The program is launched by calling the main class with parameters.

8. Fibonacci Series for a Range  
  The program allows you to display all Fibonacci numbers that are in the specified range.
  The range is given by two arguments when calling the main class. Numbers are displayed separated by commas
  Ascending. 

### Dependencies

This project doesn't require any additional packages.
    
### Credentials
 
[<img src="https://avatars0.githubusercontent.com/u/49559296?s=460&v=4" width="16" height="16" />](https://github.com/gotoindex) [@gotoindex](https://github.com/gotoindex)
