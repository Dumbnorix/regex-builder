# Regex builder

## Getting started

Clone the repo and navigate to it

```
git clone https://github.com/Dumbnorix/regex-builder.git
cd /your-workspace/regex-builder
```

## Run via command line

The specification outlines that the program should allow command line usage.

`cat input.txt | python builder.py "foo %{0} is a %{1S2}" > output.txt`

## Run via module import

The specification outlines that the program should be a reusable module.

`$ python import.py`

## Running the tests

`python -m unittest tests.py`

## Built with

* [python3.7](https://www.python.org/downloads/release/python-370/)
* [unittest](https://docs.python.org/3/library/unittest.html)
* [re](https://docs.python.org/3/library/re.html) - Regular expression operations
* [logging](https://docs.python.org/3/library/logging.html)