# Regex builder

## Getting started

Clone the repo and navigate to it

```
git clone https://github.com/Dumbnorix/regex-builder.git
cd /your-workspace/regex-builder
```

## Run via command line

The specification outlines that the program should allow command line usage.

`cat input.txt | python3 builder.py "foo %{0} is a %{1S2}" > output.txt`

The specification outlines that the program should accept 1 or more patterns.

`cat input.txt | python3 builder.py "foo %{0} is a %{1S2}" "the big %{0} fox ran away" > output.txt`

## Run via module import

The specification outlines that the program should be a reusable module.

The file `import.py` imports the program class and re-uses it as a module.

`$ python3 import.py`

## Running the tests

`python3 -m unittest tests.py`

## Built with

* [python3.7](https://www.python.org/downloads/release/python-370/)
* [unittest](https://docs.python.org/3/library/unittest.html)
* [re](https://docs.python.org/3/library/re.html) - Regular expression operations
* [logging](https://docs.python.org/3/library/logging.html)