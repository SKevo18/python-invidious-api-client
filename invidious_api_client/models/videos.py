import typing as t

from datetime import datetime
from invidious_api_client.models import BaseInvidiousData


class YoutubeVideo(BaseInvidiousData):
    """
        A YouTube video.
    """

    @property
    def type(self) -> str:
        """
            The type of the data. This should be always `"video"`.
        """

        return self.data.get('type')


    @property
    def title(self) -> str:
        """
            The title of the video.
        """

        return self.data.get('title')


    @property
    def video_id(self) -> str:
        """
            The ID of the video.
        """

        return self.data.get('videoId')


    @property
    def youtube_url(self) -> str:
        """
            YouTube URL of the video.
        """

        return f"https://youtube.com/watch?v={self.video_id}"



    class Thumbnail(BaseInvidiousData):
        """
            Thumbnail data.
        """

        @property
        def quality(self) -> str:
            """
                The quality of the thumbnail.

                Possible values:
                - `"maxres"` (1280x720)
                - `"maxresdefault"` (1280x720)
                - `"sddefault"` (640x480)
                - `"high"` (480x360)
                - `"medium"` (320x180)
                - `"default"` (120x90)
                - `"start"` (120x90)
                - `"middle"` (120x90)
                - `"end"` (120x90)
            """

            return self.data.get('quality')


        @property
        def url(self) -> str:
            """
                The URL of the thumbnail.
            """

            return self.data.get('url')


        @property
        def width(self) -> int:
            """
                The width of the thumbnail (in pixels).
            """

            return self.data.get('width')


        @property
        def height(self) -> int:
            """
                The height of the thumbnail (in pixels).
            """

            return self.data.get('height')



    @property
    def video_thumbnails(self) -> t.List[Thumbnail]:
        """
            A list of thumbnails for the video.
        """

        return [self.Thumbnail(thumbnail) for thumbnail in self.data.get('videoThumbnails')]



    class Storyboard(BaseInvidiousData):
        """
            Storyboard data.

            Storyboard image is a series of images that are rendered on the
            timeline when you hover on the video at certain timestamp (YouTube only).
        """

        @property
        def url(self) -> str:
            """
                The URL of storyboard list. This is a plain text file with the following format:

                ```plaintext
                WEBVTT00:00:00.000 --> 00:00:00.000
                <URL of the storyboard image>

                00:00:05.000 --> 00:00:10.000
                <another URL>
                ```
            """

            return self.data.get('url')


        @property
        def template_url(self) -> str:
            """
                URL to storyboard's template. This often doesn't work(?).
            """

            return self.data.get('templateUrl')


        @property
        def width(self) -> int:
            """
                The width of the storyboard (in pixels).
            """

            return self.data.get('width')


        @property
        def height(self) -> int:
            """
                The height of the storyboard (in pixels).
            """

            return self.data.get('height')



    @property
    def storyboards(self) -> t.List[Storyboard]:
        """
            A `list` of video's storyboards.

            Storyboard image is a series of images that are rendered on the
            timeline when you hover on the video at certain timestamp (YouTube only).
        """

        return [self.Storyboard(storyboard) for storyboard in self.data.get('storyboards')]



    @property
    def description(self) -> t.Text:
        """
            The description of the video.
        """

        return self.data.get('description')
    

    @property
    def description_html(self) -> t.Text:
        """
            The HTML description of the video.
        """

        return self.data.get('descriptionHtml')


    @property
    def published(self) -> datetime:
        """
            The date and time when the video was published.
        """

        return datetime.fromtimestamp(self.data.get('published'))


    @property
    def published_text(self) -> str:
        """
            The date and time when the video was published, as text (e. g.: `2 weeks ago`).
        """

        return self.data.get('publishedText')
