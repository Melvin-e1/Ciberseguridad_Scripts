import subprocess
import pyautogui
import datetime
import os

path = 'C:/shh'


if not os.path.exists(path):
    os.makedirs(path)

#fotito
i = 1
img = pyautogui.screenshot()
date = datetime.datetime.now()
ddate = str(date.strftime('%Y%m%d_%H%M%S'))
name = f'Sc{i}'
name += ddate
name += '.png'
a = os.path.join(path, name)
img.save(a)

#procesos
File = f'Process{i}_{ddate}.txt'
path2 = os.path.join(path,File)
proccess = subprocess.run('tasklist', shell=True, capture_output=True, text=True)
with open(path2, 'w') as file:
    file.write(proccess.stdout)










