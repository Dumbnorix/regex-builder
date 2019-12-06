'''
import.py

A sample file to show usage of importing the program as a module and using it
'''
from builder import RegexBuilder

regex = RegexBuilder()

testData = ['the big scary brown fox ran away', 'the big brown fox ran away']
pattern  = 'the %{0S0} brown %{1} ran away'

matches = regex.run(testData, pattern)

if(matches): print(matches)