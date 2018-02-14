import os
import sys


try:
    os.system('cp myblog/settings.py-example myblog/settings.py')
    sys.exit()

except Exception as e:
    print(e)
