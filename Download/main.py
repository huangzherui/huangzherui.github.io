import requests,warnings,os,wx
from tkinter import messagebox
warnings.filterwarnings('ignore')

def urldownload(url,path):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(path):
        file = open(path,'a')
        file.close()
    with open(path,'wb') as file:
        file.write(down_res.content)

def Calculate_the_location():#计算位置
    global posnum
    posnum += 1
    return ((posnum//20)*100,posnum%20*30)

def update(e,mark):
    messagebox.showinfo('提示','下载中……')
    urldownload(downloadprogramlist[mark]['url'],downloadprogramlist[mark]['filename'])
    openfile(e,mark)

def openfile(e,mark):
    global downloadprogramlist
    cmd(f"start {downloadprogramlist[mark]['filename']}")

def cmd(cmd):
    os.system(cmd)

with open('apps.cfg','r') as file:
    downloadprogramlist = eval(file.read())

with open('Download.ini','r') as file:
    programlist = eval(file.read())

app = wx.App()
window = wx.Frame(None, title = "下载", size = (400, 600))
panel = wx.Panel(window)

posnum = -1
buttonlist = []
for i in range(len(downloadprogramlist)):
    if int(downloadprogramlist[i]['ID']) not in programlist[1] or int(downloadprogramlist[i]['version']) > programlist[1][int(downloadprogramlist[i]['ID'])]:
        buttonlist.append(wx.Button(panel, label=downloadprogramlist[i]['name'], pos=Calculate_the_location()))
        buttonlist[-1].Bind(wx.EVT_BUTTON,lambda e,mark=i:update(e,mark))
    else:
        buttonlist.append(wx.Button(panel, label=f"打开{downloadprogramlist[i]['name']}", pos=Calculate_the_location()))
        buttonlist[-1].Bind(wx.EVT_BUTTON,lambda e,mark=i:openfile(e,mark))

window.Show(True) 
app.MainLoop()
