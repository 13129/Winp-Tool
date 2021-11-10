import platform
import sys


print(platform.architecture())
print(platform.platform())
print(sys.version)
print(sys.platform)
print(sys.version_info) 

if sys.version_info == (3,7,2):
    print('es')
else:
    print('os')

class PreCheckException(Exception):
    pass


class PreCheckMessage:
    '''检查信息框'''
    def __init__(self,msg) -> None:
        import wx
        
        pass