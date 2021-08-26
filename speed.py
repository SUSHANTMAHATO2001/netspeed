import sys,os
import time
try:
      import pyspeedtest
except ImportError:
       os.system('python2 -m pip install pyspeedtest')


os.system('clear')

import pyspeedtest

class color:
        r = '\x1b[;33m'
        g = '\x1b[;32m'


def susan(s):
  for a in s + '\n':
      sys.stdout.write(a)
      sys.stdout.flush()
      time.sleep(1./12)

susan(color.r + "Program By Sushant Mahato")

susan("Devlop By Nepal")

time.sleep(1)
os.system('clear')





a = raw_input('inter url:- ')

st = pyspeedtest.SpeedTest(a)
a = st.ping()
print(color.g)
print(a)
