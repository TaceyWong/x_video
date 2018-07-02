# coding:utf-8

"""
water_mark.py
: 给视频添加文字&图片水印
by tacey on 18-7-2
"""

import subprocess
from utils import check_path


def text_watermark(in_video, out_video):
    check_path(out_video)
    text = "测试中文水印"
    x = 10
    y = 10
    fontf = "./hysjsJ.ttf"
    fontsize = 12
    fcolor = "white"
    sc = 'black'
    shadow_x = 5
    shadow_y = 5
    custom = "drawtext=text={text}:x=100:y=H-th-100:fontfile={fontf}:fontsize=38:fontcolor=red:shadowcolor=black:shadowx=5:shadowy=5 "
    custom = custom.format(text=text, fontf=fontf)
    args = ['ffmpeg', '-i', in_video, '-vf', custom, out_video]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('ffprobe', out, err)
    return out.decode('utf-8')


def img_watermark(in_video, out_video):
    check_path(out_video)
    img_path = "./logo.png"
    args = ['ffmpeg', '-i', in_video, '-i', img_path, '-filter_complex', 'overlay=10:main_h-overlay_h-10', out_video]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('ffprobe', out, err)
    return out.decode('utf-8')


if __name__ == "__main__":
    in_video = "/home/tacey/test.mp4"
    img_watermark(in_video, "a.mp4")
