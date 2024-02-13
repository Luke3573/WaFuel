import subprocess
import os

filename = 'WaFuel/WaFuel.py'

while True:
    p = subprocess.Popen('python3 '+filename, shell=True).wait()

    if p != 0:
        continue
    
    else:
        os.system('clear')
        break
