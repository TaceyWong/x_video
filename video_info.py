# coding:utf-8

"""
video_info.py
:
by tacey@AtomPai on 18-7-2
"""

import sys
import json
import subprocess


def video_info(video_path):
    args = ['ffprobe', '-show_format', '-show_streams', '-of', 'json', video_path]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('ffprobe', out, err)
    probe = json.loads(out.decode('utf-8'))
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found')
        sys.exit(1)

    print(video_stream)


if __name__ == "__main__":
    video_info("./test.mp4")
