# System check
# Package version check
# Database version check
# Log system
# Gui interface

from platform import system
from service.version.prereqsCheck import version_precheck,PreCheckMessage,PreCheckException
from start_optparse import start_cmd
import datetime
import os
import sys
import config


# 命令行启动参数配置
parser = start_cmd()
(options, args) = parser.parse_args()

if __name__=='__main__':
    try:
        # 版本效验，提示弹窗
        version_precheck()
    except PreCheckException as ex:
        PreCheckMessage(str(ex))
        sys.exit()


    import wx
    from logbook import Logger

    winptoollog = Logger(__name__)
    from gui.error.errorDialog import ErrorHandler
    #配置自定义错误捕获
    sys.excepthook = ErrorHandler.HandleException

    if options.rootsavedata is True:
        config.saveInRoot = True
        

    config.debug = options.debug
    
    # 日志等级
    config.loggingLevel = config.LOGLEVEL_MAP.get(options.logginglevel.lower(), config.LOGLEVEL_MAP['error'])



