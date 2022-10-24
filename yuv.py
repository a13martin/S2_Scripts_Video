import os
import subprocess


def yuv_histogram(inv, outv):
    if os.path.exists(outv):
        os.remove(outv)

    if isinstance(inv, str) and isinstance(outv, str):
        subprocess.call(
            'ffmpeg -i ' + inv + ' -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" ' + outv)
    else:
        pass


if __name__ == '__main__':
    yuv_histogram("bbb_trim.mp4", "bbb_histo.mp4")
