# 0x00. AirBnB clone - The console Alx Project

## Table of Contents

* [Introduction](#introduction)
* [Environment](#environment)
* [Installation](#installation)
* [Testing](#testing)
* [Usage](#usage)
* [Authors](#authors)

## Introduction

This project is a collaborative effort to create a clone of [AirBnB](https://www.airbnb.com/), implementing a console as a command interpreter. The console manages object abstraction, their interactions, and storage methodologies.

To understand the foundational background of the project, visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The primary tasks of the console include:

* Creating a new object
* Retrieving an object from a file
* Performing operations on objects
* Destroying an object

### Storage

The `Storage` engine handles all classes through the `FileStorage` class.

## Environment

* Operating System:
  * [Ubuntu](https://ubuntu.com/)
* Command Line Interface:
  * [GNU Bash](https://www.gnu.org/software/bash/)
* Programming Language:
  * [Python](https://www.python.org)
* Editors:
  * VIM [Vim](https://www.vim.org/)
  * Visual Studio Code [Visual Studio Code](https://code.visualstudio.com/)
  * Atom [Atom](https://atom.io/)
* Version Control:
  * Git [Git](https://git-scm.com/)
* Other tools:
  * Style guidelines:
    * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
    * [PEP8](https://pep8.org/)

The development and testing were conducted on an operating system running Ubuntu 20.04 LTS using Python 3.8.3. The editors employed were VIM 8.1.2269, VSCode 1.6.1, and Atom 1.58.0. Version control was managed via Git 2.25.1.

## Installation

```
git clone https://github.com/ZakariaArc/AirBnB_clone.git
cd AirBnB_clone
./console.py
```

### Execution

**Interactive Mode**

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

**Non-interactive Mode**

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Testing

All tests are located in the `tests` folder.

### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

* Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

And

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests

* Module: unittest
* File extension: `.py`
* Naming convention: Files and folders start with `test_`
* Organization: For `models/base.py`, unit tests reside in `tests/test_models/test_base.py`
* Execution command: 
```
python3 -m unittest discover tests
```
or
```
python3 -m unittest tests/test_models/test_base.py
```

### Run Test in Interactive Mode

```
echo "python3 -m unittest discover tests" | bash
```

### Run Test in Non-Interactive Mode

For non-interactive mode and to discover all tests, use:
```
python3 -m unittest discover tests
```

## Usage

* Start the console in interactive mode:

```
$ ./console.py
(hbnb)
```

* Use help to see available commands:

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```
(hbnb) quit
$
```

### Commands

Commands are displayed in the following format: *Command / usage / example with output*

**Create**

```
create <class>
```

Example:

```
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

**Show**

```
show <class> <id>
```

Example:

```
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

**Destroy**

```
destroy <class> <id>
```

Example:

```
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

**All**

```
all <class>
```

Example:

```
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19,
