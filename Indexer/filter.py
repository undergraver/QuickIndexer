import fnmatch
import re

def createFilter(globExclusionPatterns,regexExclusionPatterns):

    allInOneRegex=''

    globToRegex = map(lambda globPattern:fnmatch.translate(globPattern), globExclusionPatterns)

    regexExclusionPatterns += globToRegex

    for regexPattern in regexExclusionPatterns:
        if len(allInOneRegex) > 0:
            allInOneRegex += '|'

        allInOneRegex += '(' + regexPattern + ')'

    # this should be compiled to be faster
    reObj = re.compile(allInOneRegex)

    return reObj

