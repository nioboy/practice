class Graphy(object):
    def __init__(self):
        self.depends = {}
        self.installed_pack = set()
        self.tracker = []

    def depend(self, items):
        items = items.split()
        num_items = len(items)
        for idx, key in enumerate(items):
            if num_items == (idx + 1):
                # all done
                continue
            value = self.depends.get(key, None)
            if value:
                if not any(items[idx + 1] in x for x in value):
                    value.append(items[idx + 1])
                    self.depends[key] = value
            else:
                self.depends[key] = [items[idx + 1],]

    def install(self, package):
        if isinstance(package, str) == True:
            self.tracker.append(package)
            depend = self.depends.get(package, None)
        elif len(package) == 1:
            self.tracker.append(package[0])
            depend = self.depends.get(package[0], None)
        elif len(package) > 1:
            for one in package:
                depend = self.depends.get(one, None)
                if depend is not None:
                    return self.install(depend)
                else:
                    self.tracker.append(one)
        if depend is None:
            for x in reversed(self.tracker):
                if x not in self.installed_pack:
                    print "Installing {}".format(x)
                    self.installed_pack.add(x)
            del self.tracker
            self.tracker = []
        else:
            return self.install(depend)

    def print_list(self):
        print self.installed_pack
        
    def remove(self, package):
        if self.depends.get(package, None):
            if package in self.installed_pack:
                print "Removing {}".format(package)
                self.installed_pack.remove(package)
            else:
                print "{} is not installed.".format(package)

graph = Graphy()
"""options = {"DEPEND": graph.depend,
           "INSTALL": graph.install,
           "REMOTE": graph.remove,
           "LIST": graph.list,
           "END": "all done"}"""
graph.depend("TELNET TCPIP NETCARD")
graph.depend("TCPIP NETCARD")
graph.depend("DNS TCPIP NETCARD")
graph.depend("BROWSER   TCPIP  HTML")

graph.install("NETCARD")
graph.install("TELNET")
graph.install("foo")
