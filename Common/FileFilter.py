import fnmatch
import re

class FileFilter:
    def __init__(self,regex):
        self.regex=regex

    def IsMatching(self,fileStr):

        if self.regex is None:
            # no regex to match; return False (no match)
            return False

        m = self.regex.match(fileStr)
        return ( None != m )

def CreateFilter(globExclusionPatterns,regexExclusionPatterns):

    allInOneRegex=''

    globToRegex = map(lambda globPattern:fnmatch.translate(globPattern), globExclusionPatterns)

    regexExclusionPatterns += globToRegex

    for regexPattern in regexExclusionPatterns:
        if len(regexPattern) == 0:
            continue

        if len(allInOneRegex) > 0:
            allInOneRegex += '|'

        allInOneRegex += '(' + regexPattern + ')'

    if len(allInOneRegex) == 0:
        return FileFilter(None)

    # this should be compiled to be faster
    reObj = re.compile(allInOneRegex)

    return FileFilter(reObj)

