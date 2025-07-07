from __future__ import print_function
import psutil
for x in range(3):
    print(psutil.cpu_percent())
    print(psutil.virtual_memory()) 