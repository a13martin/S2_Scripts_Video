import ffmpeg
import os

'''
This exercise was done by using the ffmpeg-python library,
which avoids using subprocesses for some ffmpeg functionalities.
'''


def trim(inf, outf, start, end):
    if os.path.exists(outf):  # Check if the video path already exists and removing if so
        os.remove(outf)

    input_video = ffmpeg.input(inf)

    pts = "PTS-STARTPTS"
    video = input_video.trim(start=start, end=end).setpts(pts)  # Trimming the video
    audio = (input_video
             .filter_("atrim", start=start, end=end)
             .filter_("asetpts", pts))  # Trimming the audio also
    vid_audio = ffmpeg.concat(video, audio, v=1, a=1)  # Concatenating both audio & video
    output = ffmpeg.output(vid_audio, outf, format='mp4')
    output.run()


if __name__ == '__main__':
    N = int(input("Type the duration of the trim (in seconds): "))
    trim("bbb.mp4", "bbb_trim.mp4", 0, 0 + N)
