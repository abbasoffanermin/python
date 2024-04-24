import subprocess
import datetime as dt
import time
program_path = "C:\\Program Files (x86)\\Narminator Beta v2.0\\shscs.pyw"
saat_path = "C:\\Program Files (x86)\\Narminator Beta v2.0\\saat.pyw"


startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

subprocess.Popen(['python', program_path], startupinfo=startupinfo)

counter = 0

while True:
    t_stamp = str(dt.datetime.now())

    if counter == 5:
        break

    else:
        time.sleep(3600)
        subprocess.Popen(['python', saat_path], startupinfo=startupinfo)
        counter += 1
