from invidious_api_client import InvidiousClient



def test_video():
    CLIENT = InvidiousClient()
    video = CLIENT.get_video('dQw4w9WgXcQ')
    assert video.video_id == 'dQw4w9WgXcQ'



if __name__ == "__main__":
    test_video()
