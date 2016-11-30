# Python Assembler Test Runner

## Setup
### Environment Variables
1. Export an environment variable called **`ASSEMBLER_TESTS`** that points to the `xmlpublisher/Xojo/Testing` directory

### Configs
1. In `configs/assembler.cfg`, under the `TESTFILES` section, set the:
    * `CHECK_DIRECTORY_EXISTS_PATH` option to a directory in the file system that will be tested for it's existence.
    * `CHECK_FILE_EXISTS_PATH` option to a file in the file system that will be tested for it's existence.

## Installation
### Python Virtual Environment
#### [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
> If not already set up, create a python virtualenv wrapper to quarantine this project's depedencies away from other projects.

1. Follow virtualenvwrapper installation steps [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).
1. Create the virtualenv: `mkvirtualenv <wrapper name>`
1. Activate the virtualenv: `workon <wrapper name>`
1. Install Python dependencies: `pip install -r requirements.txt`

## Test Execution

### [Nosetests](http://nose.readthedocs.io/en/latest/index.html)
> Nose is a test runner that extends Python's builtin [unittest](https://docs.python.org/2/library/unittest.html) package

#### Usage
* To run all tests simply enter the command `nosetests`. This will run every test in the suite.
> Note: normally `nosestests` affords a [rich set of options](http://nose.readthedocs.io/en/latest/usage.html#extended-usage) for running suites, specific modules, classes and even tests. However, it appears that the way the application is listening for incoming requests doesn't allow command line arguments to `nosetests` application. Doing so causes the application to hang due to wrong input going into the request parser.

### [Unittest](https://docs.python.org/2/library/unittest.html)
> "The Python unit testing framework, sometimes referred to as "PyUnit," is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent's Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language."

#### Usage
##### By module
* `python -m unittest <test_name>`
> Notice that there's no `.py` on the end of the module name. This is because when using the `-m` python command line option you are referencing a module instead of a file (similar to importing a module inside a python source file).

##### By file
* `python <test_name.py>`
> I've added<br><br>
> `if __name__ == '__main__':`<br>
> &nbsp;&nbsp;&nbsp;&nbsp;`unittest.main()`<br><br>
> to the bottom of each test file. Normally, you wouldn't do this in a unittest file, but since the TCP socket the assembler app is listening on reads any arguments to the test script as input to the assembler's api, only a single argument can be used, which is the file name. Since the `-m` option is not being used, the `.py` file extension needs to be included.
