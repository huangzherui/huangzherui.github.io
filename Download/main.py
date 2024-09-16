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

def OnButton(e,mark):
    messagebox.showinfo('提示','下载中……')
    urldownload(programlist[mark]['url'],programlist[mark]['filename'])
    cmd(f"start {programlist[mark]['filename']}")

def cmd(cmd):
    os.system(cmd)

with open('apps.cfg','r') as file:
    programlist = eval(file.read())

app = wx.App()
window = wx.Frame(None, title = "下载", size = (400, 600))
panel = wx.Panel(window)

posnum = -1
buttonlist = []
for i in range(len(programlist)):
    buttonlist.append(wx.Button(panel, label=programlist[i]['name'], pos=Calculate_the_location()))
    buttonlist[-1].Bind(wx.EVT_BUTTON,lambda e,mark=i:OnButton(e,mark))

window.Show(True) 
app.MainLoop()
