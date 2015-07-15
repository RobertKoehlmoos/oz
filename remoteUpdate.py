import subprocess, time

host = "ubuntu@52.3.79.67"
c1 = "git clone https://github.com/vz-risk/VCDB"
c2 = "echo '" + time.strftime("%c")+"' >> test.txt"
ssh = subprocess.Popen(["ssh", host, c1],
			shell=False,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
ssh = subprocess.Popen(["ssh", host,c2],
			shell=False,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
print "It worked!"
