class ScanPath:
    def __init__(self,keyval={}):
        self.id = keyval['id']
        self.path = keyval['path']
        self.pathtype = keyval['pathtype']
        self.username = keyval['username']
        self.password = keyval['password']

        self.globexclusion_name = keyval['globexclusion_name']
        self.regexexclusion_name = keyval['regexexclusion_name']
        self.globexclusion_path = keyval['globexclusion_path']
        self.regexexclusion_path = keyval['regexexclusion_path']

    def Display(self):
        buf = ''
        s = "Scan path " + str(self.id) + " configuration\n"
        buf += s
        s = "Path:"+self.path + "\n"
        buf += s
        s = "Type:"+self.pathtype + "\n"
        buf += s
        s = "User:" + self.username + "\n"
        buf += s
        s = "Password:" + self.password + "\n"
        buf += s

        nameglobs = self.globexclusion_name.split('\r')
        s = "Name exclude globs:" + ','.join(nameglobs) + "\n"
        buf += s

        nameregex = self.regexexclusion_name.split('\r')
        s = "Name exclude regex:" + ','.join(nameregex) + "\n"
        buf += s

        pathglobs = self.globexclusion_path.split('\r')
        s = "Path exclude globs:" + ','.join(pathglobs) + "\n"
        buf += s

        pathregex = self.regexexclusion_path.split('\r')
        s = "Path exclude regex:" + ','.join(pathregex)
        buf += s

        print buf

