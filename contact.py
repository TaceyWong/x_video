# coding:utf-8

"""
contact.py
: 拼接
by tacey@AtomPai on 18-7-2
"""

"""
# Adds 3-sec fading out title image before video.
# What's going on here: We get title.png image, loop it for 3 sec video, create 3 sec silence, get video.mp4 (framerate 25). Next, we add fade out filter on looped image video, after that we concat our image video, audio silence and main video into one. Easy peasy.
ffmpeg -loop 1 -framerate 25 -t 3 -i title.png -t 3 -f lavfi -i aevalsrc=0 -i video.mp4 -filter_complex '[0:0]fade=out:50:25:alpha=1[title]; [title][1:0][2:0][2:1] concat=n=2:v=1:a=1' output.mp4
"""
