import typing as t

from datetime import datetime



class BaseInvidiousData:
    """
        Base Invidious JSON data class.
    """

    def __init__(self, data: t.Union[dict, list] = {}) -> None:
        self.data = data
        """The data of the object."""



class RYDData(BaseInvidiousData):
        """
            https://returnyoutubedislike.com/ data.
        """

        @property
        def id(self) -> str:
            """
                The ID of the video.
            """

            return self.data.get('id')


        @property
        def date_created(self) -> datetime:
            """
                When was the dislike data created/updated.
            """

            return datetime.fromisoformat(self.data.get('dateCreated'))


        @property
        def likes(self) -> int:
            """
                The number of likes.
            """

            return self.data.get('likes')


        @property
        def dislikes(self) -> int:
            """
                The number of dislikes.
            """

            return self.data.get('dislikes')


        @property
        def rating(self) -> float:
            """
                A float of range `0.0` (lowest) to `5.0` (highest).
            """

            return self.data.get('rating')


        @property
        def view_count(self) -> int:
            """
                The number of views.
            """

            return self.data.get('viewCount')


        @property
        def deleted(self) -> bool:
            """
                Whether the video has been deleted or not.
            """

            return self.data.get('deleted')
