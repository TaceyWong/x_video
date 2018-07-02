# coding:utf-8

"""
split_cut.py
:
by tacey@AtomPai on 18-7-2
"""

import subprocess
from utils import check_path


def split_by_time(in_video, out_video):
    check_path(out_video)
    start = '00:00:02'
    l = '3'
    # args = ['ffmpeg', '-i', in_video, '-c', 'copy', '-ss', start,  out_video]
    args = ['ffmpeg', '-i', in_video, '-vcodec', 'copy', '-acodec', 'copy', '-ss', start, '-t', l,'-sn', out_video]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('ffmpeg', out, err)
    print(out.decode('utf-8'))


if __name__ == "__main__":
    i = "/home/tacey/test.mp4"
    o = "./test.mp4"
    split_by_time(i,o)