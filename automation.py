# Practice Exmaple

import psutil
import shutil


def disk_usage(disk):
    d = shutil.disk_usage(disk)

    f = d.free/d.total*100

    return f >50

def cpu_usage():
    d = psutil.cpu_percent(0.1)

    return d >50

if not disk_usage('/') or cpu_usage():
    print('Disk is full')
else:
    print("!Error")