import re
import sys

from logger import Log

class RegexBuilder(object):

    @Log(skip=True) # example optional modifying skip paramater
    def run(self, lines, pattern):
        if pattern is None:
            raise TypeError

        matches = []
        regex = self.buildRegex(pattern)

        for line in lines:
            match = self.matchLine(line, regex)
            if (match): matches.append(match)
        
        return matches

    @Log(quiet=True) # example optional modifying quiet paramater
    def buildRegex(self, pattern):
        regex = f'^{pattern}$'
        regex = re.sub(r'%{(\d+)}', r'([a-zA-Z0-9-_]+ *)+', regex)
        regex = re.sub(r'%{[\d+][S](\d+)}', r'([a-zA-Z0-9_]+ ){\1}([a-zA-Z0-9_]+)', regex)
        return regex

    @Log()
    def matchLine(self, line, regex):
        match = re.search(regex, line)
        if (match):
            if __name__ == '__main__': print(match.string)
            return match.string

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
        RegexBuilder().run(lines, pattern)
        sys.stdout.flush()
    else:
        raise TypeError('pattern is None')