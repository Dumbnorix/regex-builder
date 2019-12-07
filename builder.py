import re
import sys

from logger import Log

class RegexBuilder(object):

    @Log(skip=True) # example optional modifying skip paramater
    def run(self, lines, pattern):
        if pattern is None:
            raise TypeError('Please provide a pattern argument')

        matches = []
        regex = self.buildRegex(pattern)

        for line in lines:
            match = self.matchLine(line, regex)
            if (match): matches.append(match)
        
        return matches

    @Log(quiet=True) # example optional modifying quiet paramater
    def buildRegex(self, pattern):
        if pattern is None:
            return None
        
        # base the regex off the pattern because this allows capturing the exact whitespace provided between string literals
        regex = f'^{pattern}$'

        # replace all instances of basic token capture with regex ([a-zA-Z0-9-_]+ *)+
        regex = re.sub(r'%{(\d+)}', r'([a-zA-Z0-9-_]+ *)+', regex)

        # replace all instances of space limitation token capture with ([a-zA-Z0-9_]+ ){\1}([a-zA-Z0-9_]+)
        # here \1 indicates the number of spaces provided within the token using a capture group backreference
        regex = re.sub(r'%{[\d+][S](\d+)}', r'([a-zA-Z0-9_]+ ){\1}([a-zA-Z0-9_]+)', regex)

        # replace all instances of greedy tokens with ([a-zA-Z0-9-_]+ *)+
        regex = re.sub(r'%{[\d+][G]}', r'([a-zA-Z0-9-_]+ *)+', regex)

        return regex

    @Log()
    def matchLine(self, line, regex):
        if regex is None:
            return None
            
        match = re.search(regex, line)
        if (match):
            if __name__ == '__main__': sys.stdout.write(str(match.string) + '\n')
            return match.string

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')

    for pattern in sys.argv[1:]:
        RegexBuilder().run(lines, pattern)