from yt_dlp import YoutubeDL
import sys


def main():
    args = sys.argv
    if 2 == len(args):
        url = args[1]
        dl(url)
    else:
        print("Arguments are too short")


def dl(url):
    with YoutubeDL() as ydl:
        result = ydl.download([url])
        return result


if __name__ == "__main__":
    print(main())
