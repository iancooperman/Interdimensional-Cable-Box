from pathlib import Path
from pytube import YouTube
from reddit import RedditSkimmer


class CableBox:
    def __init__(self):
        self.videos = []
        self.reddit = RedditSkimmer()

        self.get_videos()

        for video in self.videos:
            print(video.title)


    def get_videos(self, num=10):
        for i in range(num):
            vid = (next(self.reddit.post_generator))

            video = Video(title=vid.title, url=vid.url)

            self.videos.append(video)


class Video:
    def __init__(self, title, url, path=Path.cwd()/Path("Videos"), downloaded=False):
        self.title = title
        self.url = url
        self.path = path
        self.downloaded = downloaded

    def download_video(self, quality='720p'):
        yt = YouTube(self.url)
        streams = yt.streams.filter(adaptive=False, resolution=quality).all()
        print(streams)

        if len(streams) > 0:
            streams[0].download(self.path)

            self.downloaded = True

    def play_video(self):
        pass


if __name__ == "__main__":
    cable_box = CableBox()
