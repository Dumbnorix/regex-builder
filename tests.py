import unittest

# under test
from builder import RegexBuilder

class Tests(unittest.TestCase):

    regexBuilder = RegexBuilder()

    def test_buildRegex_withBasicToken(self):
        pattern = 'my name is %{0}'
        expected = r'^my name is ([a-zA-Z0-9-_]+ *)+$'
        self.assertEqual(self.regexBuilder.buildRegex(pattern), expected)

    def test_buildRegex_withLimitationToken(self):
        pattern = 'my name is %{0S2}'
        expected = r'^my name is ([a-zA-Z0-9_]+ ){2}([a-zA-Z0-9_]+)$'
        self.assertEqual(self.regexBuilder.buildRegex(pattern), expected)

    def test_buildRegex_withBasicAndLimitationToken(self):
        pattern = 'my %{0} is %{1S2}'
        expected = r'^my ([a-zA-Z0-9-_]+ *)+ is ([a-zA-Z0-9_]+ ){2}([a-zA-Z0-9_]+)$'
        self.assertEqual(self.regexBuilder.buildRegex(pattern), expected)

    def test_matchLine_correctlyMatches(self):
        line = 'my name is alexander bush'
        regex = r'^my name is ([a-zA-Z0-9-_]+ *)+$'
        self.assertEqual(self.regexBuilder.matchLine(line, regex), line)
    
    def test_matchLine_correctlyIgnoresNonMatches(self):
        line = 'my name is'
        regex = r'^my name is ([a-zA-Z0-9-_]+ *)+$'
        self.assertEqual(self.regexBuilder.matchLine(line, regex), None)

    def test_run_returnsMatchedLines(self):
        lines = ['my name is alexander', 'my name is alexander bush']
        pattern = 'my name is %{0S1}'
        self.assertEqual(self.regexBuilder.run(lines, pattern), ['my name is alexander bush'])

    def test_run_withNoPattern(self):
        with self.assertRaises(TypeError):
            self.regexBuilder.run([], None)

if __name__ == '__main__':
    unittest.main()