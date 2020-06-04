# Sudoku Solver
## Backtracking / AC-3 / MRV / Least Containing Value

## I] Requirements

- [Git](https://git-scm.com/downloads) to download the source code

- [python3](https://www.python.org/downloads/) to execute the code

- [pip3](https://pypi.org/project/pip/) to install dependencies

## II] Installation

Clone the project to your local machine:
```bash
git clone https://github.com/stressGC/python-backtracking-CSP-sudoku-solver.git
cd python-backtracking-CSP-sudoku-solver
```

You will need to install the following modules :
```bash
pip3 install argparse itertool 
```

## III] Execution

The following arguments are available:

- **--help** to get some informations about the script
```bash
python solver.py --help
```
- **--string** followed by a string representing one or more Sudokus. It will be parsed by the script. Accepted characters : [1,9], "#", "@", "X". A list of 20 sudokus can be found [data/20sudokus.txt](https://raw.githubusercontent.com/stressGC/python-backtracking-CSP-sudoku-solver/master/data/20sudokus.txt) .
```bash
python solver.py --string <my_sudoku(s)_as_string>
```
- **--level** followed by a level for the default sudoku. 
Accepted values : ["easy", "medium", "hard"], default : "medium".
```bash
python solver.py --level <level>
```

Note : **--string** and **--level** can't be specified at the same time as they are concurrent.

## IV] Result

All the current computing steps will be printed in console for each one of the sudokus.

![Screenshot of a result](https://github.com/stressGC/python-backtracking-CSP-sudoku-solver/blob/master/img/result.png "Screenshot of a result")

