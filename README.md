# Short Title

This repository contains a Python function that returns a short version of a title, given the maximum length of the title. The function has been implemented in `short_title.py`, and tested in `test_short_title.py`.

## Test Cases
The `test_short_title.py` file contains test cases that cover the following scenarios:
- Positive test cases, where the input title is short enough or needs to be shortened
- Negative test cases, where the length is less than or equal to 0 or less than or equal to 3
- Internationalization (i18n) test case, with a title containing non-ASCII characters
- Localization (l10n) test case, with a title containing characters from a different language/script
- Destructive test case, with a title that consists of only spaces

## Implementation Details
The `short_title` function takes two arguments: `title` and `length`. It returns a shortened version of the title, such that:
- The full title should be no longer than `length` symbols
- If the title is longer than `length` symbols, it should end with "..."
- The title should end on a full word

## Requirements
- Python 3
- virtualenv (recommended)

## Installation

### Python 3

If you do not have Python 3 installed on your system, you can download it from the official website: https://www.python.org/downloads/

### virtualenv

If you do not have virtualenv installed, you can install it using pip: 
```sh
pip install virtualenv
```

## Usage

1. Clone the repository:
```sh
git clone https://github.com/jmassapina/short-title.git
```

2. Create a virtual environment:
```sh
virtualenv venv
```

3. Activate the virtual environment:
```sh
source venv/bin/activate
```

4. Run the tests:
```sh
python test_short_title.py
```

## Conclusion
This repository contains a simple Python function and its accompanying tests, to shorten a given title to a given length. The code has been written to be compatible with Python 3 and has been tested using the virtual environment feature of Python 3. The code has also been uploaded to GitHub for reference.
