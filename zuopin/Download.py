import requests,warnings,os
warnings.filterwarnings('ignore')

version = 1.0

def urldownload(url,path):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(path):
        file = open(path,'a')
        file.close()
    with open(path,'wb') as file:
        file.write(down_res.content)

def cmd(cmd):
    os.system(cmd)

urldownload('http://huangzherui.github.io/Download/apps.cfg','apps.cfg')

if os.path.exists('Download.ini'):
    with open('Download.ini','r') as file:
        if not version == eval(file.read)[0]:
            urldownload('http://huangzherui.github.io/Download/main.py','main.py')
else:
    with open('Download.ini','a') as file:
        file.write('[%d,{}]'%version)
    urldownload('http://huangzherui.github.io/Download/main.py','main.py')
cmd('start python main.py')
quit()
