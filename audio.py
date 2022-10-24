import os
import subprocess


def stereo_to_mono(inv, outv):
    if os.path.exists(outv):
        os.remove(outv)
    subprocess.call("ffmpeg -i " + inv + " -ac 1 " + outv)


def mono_to_stereo(inv, outv):
    if os.path.exists(outv):
        os.remove(outv)
    subprocess.call("ffmpeg -i " + inv + " -ac 2 " + outv)


if __name__ == '__main__':
    print("Type 1 for stereo to mono conversion. \nType 2 for mono to stereo conversion. \nType 0 to exit.")
    option = int(input("Select an operation: "))
    print("Operation %s was selected." % option)

    match option:
        case 1:
            stereo_to_mono("bbb.mp4", "bbb_mono.mp4")
        case 2:
            mono_to_stereo("bbb_mono.mp4", "bbb_mono_to_stereo.mp4")
        case 0:
            print("Exiting... ")
        case other:
            print("Error: Wrong number")
