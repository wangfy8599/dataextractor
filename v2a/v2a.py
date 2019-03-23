import os
import subprocess
import threading
import datetime


base_dir = r"D:\xuebing\ffmpeg\samples"
app_name = os.path.join(base_dir, "ffmpeg.exe")


class ConvertThread(threading.Thread):
    def __init__(self, index, in_file, out_file):
        super(ConvertThread, self).__init__()
        self.index = index
        self.in_file = os.path.join(base_dir, in_file)
        out_dir = os.path.join(base_dir, "results", index)
        os.makedirs(out_dir, exist_ok=True)
        self.out_file = os.path.join(out_dir, out_file)

    def run(self):
        subprocess.run("{} -y -i {} -ac 1 -ab 8000 {}".format(app_name, self.in_file, self.out_file).split(" "))


print(datetime.datetime.now())
thread_list = []
for i in range(1, 334):
    ct = ConvertThread(str(i), "SampleVideo_1280x720_30mb.mp4", "SampleVideo_1280x720_30mb.mp3")
    ct.start()  # This actually causes the thread to run
    thread_list.append(ct)

for t in thread_list:
    ct.join()  # This waits until the thread has completed

print(datetime.datetime.now())
