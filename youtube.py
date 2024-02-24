from yt_dlp import YoutubeDL
from yt_dlp.utils import ExtractorError
import sys


def main():
    message = "ダウンロードURLを入力してください"
    url = input(message)
    dl(url)


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
