import requests,warnings,os
warnings.filterwarnings('ignore')

version = '1.0'
serverurl = 'https://huangzherui.github.io/Download/'

def urldownload(url,path):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(path):
        file = open(path,'a')
        file.close()
    with open(path,'wb') as file:
        file.write(down_res.content)

def cmd(cmd):
    os.system(cmd)

if not os.path.exists('Download.ini'):
    with open('Download.ini','a') as file:
        file.write(version)
else:
    with open('Download.ini','r') as file:
        if not version == file.read():
            urldownload(f'{serverurl}main.py','main.py')
            cmd('start cmd python main.py')
            quit()
