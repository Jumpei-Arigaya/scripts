from yt_dlp import YoutubeDL
from yt_dlp.utils import ExtractorError
import sys


def main():
    args = sys.argv
    if len(args) == 2:
        url = args[1]
        dl(url)
    else:
        print("Arguments are too short")


def dl(url):
    ydl_opts = {
        "cookiesfrombrowser:": "chrome",
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.download(url)
            return result
        except Exception as e:
            print("failed downloads:", e)


if __name__ == "__main__":
    main()
