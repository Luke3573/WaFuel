import subprocess

filename = 'Desktop/stripper1.py'
while True:
    """However, you should be careful with the '.wait()'"""
    p = subprocess.Popen('python3.8 '+filename, shell=True).wait()

    """#if your there is an error from running 'monitor/monitor.py',
    the while loop will be repeated,
    otherwise the program will break from the loop"""
    if p != 0:
        continue
    else:
        break

