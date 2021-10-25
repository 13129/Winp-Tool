# coding:utf-8
# author:Twobox

import wx
import wx.lib.mixins.listctrl as listmix
from wx.core import Panel
# from ObjectListView import ObjectListView, ColumnDefn, OLVEvent
from wx.lib.agw import ultimatelistctrl as ULC
from wx.lib.embeddedimage import PyEmbeddedImage
import img


class Results(object):
    """"""

    def __init__(self, tin, zip_code, plus4, name, address):
        """Constructor"""
        self.tin = tin
        self.zip_code = zip_code
        self.plus4 = plus4
        self.name = name
        self.address = address


class Mywin(wx.Frame, listmix.ColumnSorterMixin):
    t_col1 =['1','2','3']
    t_col4 = ['1', '1', '3', '5', '5', '1', '2']
    colhead = ["选择", "文件名称", "文件格式", "文件大小", "上传时间", "删除", "下载"]
    colwidth = [50, 200, 60, 100, 140, 90, 95]
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title, style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.InitUI()

    def InitUI(self):
        self.initUIMenuBar()  # 初始化 菜单栏
        self.initUIToolsBar()
        self.initUIStatusBar()  # 初始化 状态栏
        self.initUIMainWindow()  # 构建 窗口面板
        self.creatList()
        self.adjustmentWin()  # 调整 窗口框体参数

    def initUIMenuBar(self):
        '''实例化一个菜单对象'''
        menuBar = wx.MenuBar()
        ftpMenu = wx.Menu()
        newItem = wx.MenuItem(ftpMenu, id = 100, text = "新建FTP", kind = wx.ITEM_NORMAL)
        ftpMenu.Append(newItem)
        editMenu = wx.Menu()
        editItem = wx.MenuItem(editMenu, id = 101, text = "修改FTP", kind = wx.ITEM_NORMAL)
        ftpMenu.Append(editItem)
        quit = wx.MenuItem(ftpMenu, id = wx.ID_EXIT, text = "Quit\tCtrl+Q", kind = wx.ITEM_NORMAL)
        ftpMenu.Append(quit)
        menuBar.Append(ftpMenu, 'FTP连接')
        self.SetMenuBar(menuBar)
        # self.Bind(wx.EVT_MENU, self.menuHandler)

    def initUIToolsBar(self):
        tb = wx.ToolBar(self,wx.ID_ANY)
        self.ToolBar = tb
        tsize = (25, 25)
        # 创建4个Bitmap图标
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, tsize)
        search_bmp =wx.ArtProvider.GetBitmap(wx.ART_FIND,wx.ART_TOOLBAR,tsize)
        install_bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_TOOLBAR, tsize)
        del_bmp = wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_TOOLBAR, tsize)


        # 将这4个图标放入工具栏
        tb.AddTool(200, '新建', new_bmp, '新建FTP')
        tb.AddTool(201, '打开', open_bmp, '打开FTP')
        tb.AddTool(202, '复制', copy_bmp, '复制当前FTP')
        tb.AddTool(203, '粘贴', paste_bmp, '粘贴当前FTP')
        tb.AddTool(204, '查找',search_bmp,'查找文件')
        tb.AddTool(205, '下载', install_bmp, '下载文件')
        tb.AddTool(206, '删除', del_bmp, '删除文件')
        # tb.AddTool(207, '刷新', left_page_bmp, '刷新页面')
        # 分割
        tb.AddSeparator()
        # 放入2个自己提供的图标
        tb.AddTool(207, '刷新', wx.Bitmap(PyEmbeddedImage(img.ref).GetBitmap()), '刷新页面')
        tb.AddTool(208, '上一页', wx.Bitmap(PyEmbeddedImage(img.left_page).GetBitmap()), '上一页工具')
        tb.AddTool(209, '下一页', wx.Bitmap(PyEmbeddedImage(img.right_page).GetBitmap()), '下一页工具')
        tb.AddTool(210, '浏览器', wx.Bitmap(PyEmbeddedImage(img.intel_net).GetBitmap()), '浏览器')
        # 为这6个图标绑定事件处理
        # self.Bind(wx.EVT_MENU, self.on_click_tool, id = 200, id2 = 205)
        tb.Realize()



    def initUIStatusBar(self):
        '''实例化一个状态栏对象'''
        self.statusBar = wx.StatusBar(parent = self, id = -1)
        self.statusBar.SetFieldsCount(4)
        self.statusBar.SetStatusWidths([-2,-3, -2,-0.8])
        self.statusBar.SetStatusText("鼠标位置:  第 1 行 , 第 1 列", 0)
        self.statusBar.SetStatusText("", 1)
        self.statusBar.SetStatusText("", 2)
        self.statusBar.SetStatusText("", 3)
        self.SetStatusBar(self.statusBar)
        self.statusBar.Show(True)

    def initUIMainWindow(self):
        '''构建窗体面板实例'''
        panel = wx.Panel(self, -1, size = (780, 600))
        panel.SetBackgroundColour('White')

        self.FTPList = wx.ComboBox(panel, -1)
        self.ConnBtn = wx.ToggleButton(panel, -1, label = '连接')
        self.FileName = wx.TextCtrl(panel, style = wx.TE_LEFT)
        self.SelBtn = wx.Button(panel, -1, label = '选择文件')
        self.OkBtn = wx.Button(panel, -1, label = '上传')

        self.operateBox = wx.BoxSizer(wx.HORIZONTAL)  # 定义第一行横向的按钮
        self.operateBox.Add(self.FTPList, 1, wx.ALL, 5)
        self.operateBox.Add(self.ConnBtn, 1, wx.ALL, 5)
        self.operateBox.Add(self.FileName, 1, wx.ALL, 5)
        self.operateBox.Add(self.SelBtn, 1, wx.ALL, 5)
        self.operateBox.Add(self.OkBtn, 1, wx.ALL, 5)


        self.listBox = wx.BoxSizer()  # 定义横向列表
        self.list_results = ULC.UltimateListCtrl(panel, agwStyle = ULC.ULC_REPORT
                                                                        # |ULC.ULC_NO_HIGHLIGHT
                                                                        |ULC.ULC_BORDER_SELECT
                                                                    |ULC.ULC_STICKY_HIGHLIGHT
                                                                   |ULC.ULC_HAS_VARIABLE_ROW_HEIGHT
                                                                   |ULC.ULC_HOT_TRACKING)
        #设定表头
        for x in range(0, len(self.colhead)):
                self.list_results.InsertColumn(x, self.colhead[x], width=self.colwidth[x],format=ULC.ULC_FORMAT_CENTRE)
        self.listBox.Add(self.list_results, 1, wx.EXPAND | wx.CENTER, 5)


        self.verticalBox = wx.BoxSizer(wx.VERTICAL)  # 定义垂直
        self.verticalBox.Add(self.operateBox, 1, wx.EXPAND, 5)
        self.verticalBox.Add(self.listBox, 9, wx.EXPAND, 5)

        self.SetSizer(self.verticalBox)

    def creatList(self):
        rb_list = ["1", "2", "3", "4", "5"]
        for x in range(0, len(self.t_col1)):
            self.list_results.InsertStringItem(x, '')
            cBox = wx.CheckBox(self.list_results,-1)
            self.list_results.SetItemWindow(x, 0, cBox)

            self.list_results.SetStringItem(x, 1, self.t_col1[x])

            self.list_results.SetStringItem(x, 2, '.jpg')
            self.list_results.SetStringItem(x, 3, '23MB')

            delBox=wx.Button(self.list_results,-1,'删除',size=(90,30))
            downloadBox = wx.Button(self.list_results, -1, '下载',size=(95,30))
            self.list_results.SetStringItem(x, 4, '2021-07-12 22:00:22')
            self.list_results.SetItemWindow(x, 5, delBox)
            self.list_results.SetItemWindow(x, 6, downloadBox)


    def adjustmentWin(self):
        '''构建窗体参数'''
        self.SetSize((780, 600))
        self.Center()
        self.Show()


if __name__ == "__main__":
    ex = wx.App()
    Mywin(None, 'CFTP-UP')
    ex.MainLoop()