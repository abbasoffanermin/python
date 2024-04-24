import subprocess
import datetime as dt
import time
program_path = "C:\\Program Files (x86)\\Narminator Beta v2.0\\mart.pyw"


startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW


while True:
    t_stamp = str(dt.datetime.now())

    if '2024-03-08' in t_stamp[0:11] and '00:00' in t_stamp[11:16]:
        subprocess.Popen(['python', program_path], startupinfo=startupinfo)
        time.sleep(120)
        break

