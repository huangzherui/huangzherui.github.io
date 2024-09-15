import os,wx,warnings,requests
from tkinter import messagebox
warnings.filterwarnings('ignore')

versions = 1.0#版本1.0
isrunningexe = False
readytoupdatelist = [] 
readytoopenlist = []

def webdbget(user,password,tag):#获取数据库
    postdata = {'user':user,'secret':password,'action':'get','tag':tag}
    r = requests.post('http://tinywebdb.appinventor.space/api',data=postdata)
    temp = r.text
    temp1 = eval(temp)[tag]
    return temp1

def urldownload(url,filename):#下载文件
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)

def Download(mode,AID):#下载
    #os.makedirs(filename)
    messagebox.showinfo('提示','下载中……')
    os.system(('start python Downloadbs.py '+mode+' '+str(AID)))

def update():#更新
    if isrunningexe:
        urldownload(('http://github.com/huangzherui/Download/raw/main/version/exe/'+str(versions)+'/DownloadDownload.exe'),'./DownloadDownload.exe')
        os.system("start python DownloadDownload.exe")
    else: 
        urldownload(('http://github.com/huangzherui/Download/raw/main/version/python/'+str(versions)+'/DownloadDownload.py'),'./DownloadDownload.py')
        os.system("start python DownloadDownload.py")
    quit()

#图形化类
class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        self.InitUi()
    def InitUi(self):
        self.SetTitle("下载")
        self.SetSize(400, 600)
        panel = wx.Panel(self)
        buttonlist = []
        self.posnum = -1
        for i in range(len(programlist)):
            if programlist[i]['Programdeamon']:#如果是
                if programlist[0]["version"] > versions:
                    buttonlist.append(wx.Button(panel, label='有新版本，点我更新', pos=self.Calculate_the_location()))
                    buttonlist[-1].Bind(wx.EVT_BUTTON,lambda e,mode='update',mark='0000':self.OnButton(e,mode, mark))
            else:
                if not programlist[i]['InternalHide']:
                    label=(programlist[i]["name"]+('(可更新)'if i in readytoupdatelist else '打开' if i in readytoopenlist else ''))
                    buttonlist.append(wx.Button(panel, label=label, pos=self.Calculate_the_location()))
                    buttonlist[-1].Bind(wx.EVT_BUTTON,lambda e,mode=('update'if i in readytoupdatelist else 'open' if i in readytoopenlist else 'download'),mark=i:self.OnButton(e,mode,mark))
        self.Centre()
    def OnButton(self,e,mode,AID):#按下按钮后
        self.Destroy()
        if AID == '0000':
            update()
        else:
            Download(mode,AID)
    def Calculate_the_location(self):#计算位置
        self.posnum+=1
        return ((self.posnum//20)*100,self.posnum%20*30)
        
if not os.path.isfile('Downloadbs.py'):#是否有Downloadbs.py
    if isrunningexe:
        urldownload(('http://github.com/huangzherui/Download/raw/main/exe/'+str(versions)+'/Downloadbs.exe'),'./Downloadbs.exe')
    else:
        urldownload(('http://github.com/huangzherui/Download/raw/main/python/'+str(versions)+'/Downloadbs.py'),'./Downloadbs.py')
#打开marketmain.cfg
with open('marketmain.cfg','w',encoding='utf8') as file:
    programlist = webdbget('zhmarket','9d6ef697','marketapps')
    file.write(str(programlist))

if os.path.isfile('zhmarket.db'):
    with open('zhmarket.db','r',encoding='utf8') as file:
        alreadyprogramraw = file.read()
        if alreadyprogramraw == '':
            alreadyprogram = []
        else:
            alreadyprogram = eval(alreadyprogramraw)
            for i in alreadyprogram:
                AID = int(i['AID'])
                if programlist[AID]['version'] > i['version']:
                    readytoupdatelist.append(AID)
                elif programlist[AID]['version'] == i['version']:
                    readytoopenlist.append(AID)
else:
    file = open('zhmarket.db','w',encoding='utf8')
    file.close()

#运行图形程序
app = wx.App()
sample = MainWindow(None)
sample.Show()
app.MainLoop()