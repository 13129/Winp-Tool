from optparse import AmbiguousOptionError, BadOptionError, OptionParser

class PassThroughOptionParser(OptionParser):
    def _process_args(self, largs, rargs, values):
        while rargs:
            try:
                OptionParser._process_args(self, largs, rargs, values)
            except (BadOptionError, AmbiguousOptionError) as e:
                # pyfalog.error("Bad startup option passed.")
                largs.append(e.opt_str)


# Parse command line options
usage = "usage: %prog [--root]"
parser = PassThroughOptionParser(usage=usage)