import fileFilter

def createFiltersForScanpath(scanpath):
    glob_name = scanpath.globexclusion_name.split('\r')
    regex_name = scanpath.regexexclusion_name.split('\r')
    namefilter=fileFilter.createFilter(glob_name,regex_name)

    glob_path = scanpath.globexclusion_path.split('\r')
    regex_path = scanpath.regexexclusion_path.split('\r')

    pathfilter=fileFilter.createFilter(glob_path,regex_path)

    return (namefilter,pathfilter)

