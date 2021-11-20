import platform
import sys

version_block=''

class PreCheckException(Exception):
    pass


class PreCheckMessage:
    '''版本检查信息框'''
    def __init__(self,msg) -> None:
        try:
            import wx
            app=wx.App(False)
            wx.MessageBox(msg,'Error',wx.ICON_ERROR|wx.STAY_ON_TOP)
            app.MainLoop()
        except (KeyboardInterrupt,SystemExit):
            raise
        except :
            pass
        finally:
            print(msg)

def version_precheck():
    global version_block

    version_block += "\nOS version: {}".format(platform.platform())
    version_block += "\nPython version: {}".format(sys.version)

    if sys.version_info < (3, 6):
        msg = "Winp-Tool当前版本支持python 3.6"
        raise PreCheckException(msg)

    try:
        # the way that the version string is imported in wx is odd, causing us to have to split out the imports like this. :(
        from wx.__version__ import VERSION, VERSION_STRING

        if VERSION[0] < 4:
            raise Exception()
        if VERSION[3] != '':
            if VERSION[3][0] == 'b' and int(VERSION[3][-1]) < 2:
                raise Exception()

        import wx
        version_block += "\nwxPython 版本: {} ({})".format(VERSION_STRING, wx.wxWidgets_version)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        msg = "Winp-Tool当前版本支持wxPython 4.0.0b2以上. 您可以从以下位置下载  https://wxpython.org/pages/downloads/"
        raise PreCheckException(msg)

    try:
        import logbook
        logVersion = logbook.__version__.split('.')
        version_block += "\nLogbook 版本: {}".format(logbook.__version__)

        if int(logVersion[0]) < 1:
            raise Exception()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        raise PreCheckException("Winp-Tool当前版本支持Logbook 1.0.0以上. 您可以从以下位置下载  https://pypi.python.org/pypi/Logbook")