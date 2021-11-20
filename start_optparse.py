from optparse import AmbiguousOptionError, BadOptionError, OptionParser



class PassThroughOptionParser(OptionParser):
    """
    An unknown option pass-through implementation of OptionParser.

    OSX passes -psn_0_* argument, which is something that pyfa does not handle. See GH issue #423
    """

    def _process_args(self, largs, rargs, values):
        while rargs:
            try:
                OptionParser._process_args(self, largs, rargs, values)
            except (BadOptionError, AmbiguousOptionError) as e:
                # pyfalog.error("Bad startup option passed.")
                largs.append(e.opt_str)

def start_cmd():
    usage = "usage: %prog [--root]"
    parser = PassThroughOptionParser(usage=usage)
    parser.add_option("-r", "--root", action="store_true", dest="rootsavedata", help="if you want pyfa to store its data in root folder, use this option", default=False)
    parser.add_option("-d", "--debug", action="store_true", dest="debug", help="Set logger to debug level.", default=False)
    parser.add_option("-t", "--title", action="store", dest="title", help="Set Window Title", default=None)
    parser.add_option("-s", "--savepath", action="store", dest="savepath", help="Set the folder for savedata", default=None)
    parser.add_option("-l", "--logginglevel", action="store", dest="logginglevel", help="Set desired logging level [Critical|Error|Warning|Info|Debug]", default="Error")
    parser.add_option("-p", "--profile", action="store", dest="profile_path", help="Set location to save profileing.", default=None)
    parser.add_option("-i", "--language", action="store", dest="language", help="Sets the language for pyfa. Overrides user's saved settings. Format: xx_YY (eg: en_US). If translation doesn't exist, defaults to en_US", default=None)
    return parser