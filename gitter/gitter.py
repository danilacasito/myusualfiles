import os
import sys
if sys.argv[1] == "remote":
    os.system("git remote add origin git@github.com:"+sys.argv[2])

