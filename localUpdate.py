import os, time

c1 = "git clone https://github.com/vz-risk/VCDB"
c2 = "echo '" + time.strftime("%c")+"' >> ~/updateLog.txt"
os.system("rm -rf VCDB")
os.system(c1)
os.system(c2)
