from invidious_api_client import InvidiousClient



def test_comments():
    CLIENT = InvidiousClient(additional_parameters={'hl': 'de'})
    comments = CLIENT.get_comments('9bZkp7q19f0')
    assert comments.video_id == '9bZkp7q19f0'



if __name__ == "__main__":
    test_comments()
