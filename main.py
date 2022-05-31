import video_edition as ve
import threads as th
import os, time


def work(video):
        ve.video_to_shorter(video)
        print(th.start_thread(os.listdir('videos')))


if __name__ == '__main__':
    work('test.mp4')
