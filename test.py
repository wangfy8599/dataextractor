import subprocess

for i in range(255):
    ip = "192.168.38.{}".format(i)
    command = "ping -n 1 {}".format(ip)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = p.communicate()
    # print(out)
    res = p.wait()
    if p.returncode == 0:
        print("{} is connected.".format(ip))
    else:
        print("{} is not able to connect.".format(ip))

