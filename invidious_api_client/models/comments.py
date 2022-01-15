import typing as t

from datetime import datetime

from invidious_api_client.models import BaseInvidiousData



class Comments(BaseInvidiousData):
    """
        Data of comments for a video.
    """

    @property
    def continuation(self) -> str:
        """
            The unique continuation token.
        """

        return self.data.get('continuation')


    @property
    def comment_count(self) -> int:
        """
            The number of comments.
        """

        return self.data.get('commentCount')


    @property
    def video_id(self) -> str:
        """
            The video ID where are the comments from.
        """

        return self.data.get('videoId')


    class Comment(BaseInvidiousData):
        @property
        def author(self) -> str:
            """
                The comment author's channel name.
            """

            return self.data.get('author')



        class CommentAuthorThumbnail(BaseInvidiousData):
            """
                Data of the comment author's profile picture/thumbnail.
            """

            @property
            def url(self) -> str:
                """
                    URL of the thumbnail.
                """

                return self.data.get('url')


            @property
            def width(self) -> int:
                """
                    Width of the thumbnail (in pixels).
                """

                return self.data.get('width')


            @property
            def height(self) -> int:
                """
                    Height of the thumbnail (in pixels).
                """

                return self.data.get('height')



        @property
        def author_thumbnails(self) -> t.List[CommentAuthorThumbnail]:
            """
                The comment author's thumbnails.
            """

            return [self.CommentAuthorThumbnail(data=thumbnail) for thumbnail in self.data.get('authorThumbnails')]



        @property
        def author_id(self) -> str:
            """
                The comment author's channel ID.
            """

            return self.data.get('authorId')


        @property
        def author_url(self) -> str:
            """
                The comment author's channel URI.
            """

            return self.data.get('authorUrl')


        @property
        def is_edited(self) -> bool:
            """
                Whether the comment was edited.
            """

            return self.data.get('isEdited')


        @property
        def content(self) -> t.Text:
            """
                The comment's plaintext content/the comment itself.
            """

            return self.data.get('content')


        @property
        def content_html(self) -> t.Text:
            """
                The comment's content (as HTML)
            """

            return self.data.get('contentHtml')


        @property
        def published(self) -> datetime:
            """
                The date and time when the comment was published.
            """

            return datetime.fromtimestamp(self.data.get('published'))


        @property
        def published_text(self) -> str:
            """
                The date and time when the comment was published (as text).

                ### Note:
                Localizable, if you pass the `hl` parameter to `additional_parameters` of the `InvidiousClient` class.
            """

            return self.data.get('publishedText')



        @property
        def like_count(self) -> int:
            """
                The number of likes the comment has.
            """

            return self.data.get('likeCount')


        @property
        def comment_id(self) -> str:
            """
                The comment's ID.
            """

            return self.data.get('commentId')


        @property
        def author_is_channel_owner(self) -> bool:
            """
                Whether the comment author is also the owner of the channel.
            """

            return self.data.get('authorIsChannelOwner')



        class CommentCreatorHeart(BaseInvidiousData):
            """
                Data of the comment creator's heart (when someone hearts your comment).
            """

            @property
            def creator_thumbnail(self) -> str:
                """
                    URL to the profile picture of the channel that hearted the comment.
                """

                return self.data.get('creatorThumbnail')


            @property
            def creator_name(self) -> str:
                """
                    Name of the channel that hearted the comment.
                """

                return self.data.get('creatorName')



        @property
        def creator_heart(self) -> CommentCreatorHeart:
            """
                The comment's creator heart.
            """

            return self.CommentCreatorHeart(data=self.data.get('creatorHeart'))


        @property
        def replies_data(self) -> t.Optional[t.Dict[str, t.Union[str, int]]]:
            """
                Raw data of the replies.
            """

            return self.data.get('replies')


        @property
        def reply_count(self) -> int:
            """
                The number of replies the comment has.
            """

            return self.replies_data.get('replyCount') if self.replies_data else 0


        @property
        def reply_continuation(self) -> t.Optional[str]:
            """
                The unique continuation token for the replies.
                
                You can then pass this to `InvidiousClient.get_comments(continuation=...)` to get the replies.
            """

            return self.replies_data.get('replyContinuation') if self.replies_data else None



    @property
    def comments(self) -> t.List[Comment]:
        """
            The comments.
        """

        return [self.Comment(data=comment) for comment in self.data.get('comments')]


    def __iter__(self) -> t.Iterator[Comment]:
        """
            Iterates over all comments.
        """

        for comment in self.comments:
            yield comment
