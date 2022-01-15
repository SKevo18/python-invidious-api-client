import typing as t

from requests import Session


from .models import BaseInvidiousData, RYDData
from .models.instances import Instance, choose_instance

from .models.videos import YoutubeVideo
from .models.comments import Comments



_RCLS = t.TypeVar('_RCLS', bound=t.Type[BaseInvidiousData])



class InvidiousClient:
    def __init__(self, instance: t.Union[Instance, str, bytes]=choose_instance(), session_object: t.Type[Session] = Session(), additional_parameters: t.Optional[t.Dict[str, t.Any]]=None) -> None:
        """
            Initializes a new Invidious API Client.

            ### Parameters:
            - `instance` - the instance URL or object to use.
            - `session` - the session object to use.
            - `**additional_parameters` - additional parameters to pass to every API request.

            ### Warning:

            You can't access the API of some instances!

            By default, the client will use the first instance that is available (`choose_instance(only_accessible=True)`).
            This slows down initialization, as it has to check all instances until it finds one that is accessible.

            ### Tip:
            You can pass additional `hl` parameter to the API request to change the language of the response:

            ```python
            InvidiousClient(additional_parameters={'hl': 'de'})
            ```

            List of available `language_code`s for `additional_parameters` (`hl`):

            - `en` - English
            - `de` - German
            - `el` - Greek
            - `en-US` - English (United States)
            - `eo` - Esperanto
            - `es` - Spanish
            - `eu` - Basque
            - `fr` - French
            - `is` - Icelandic
            - `it` - Italian
            - `nb_NO` - Norwegian (Bokmål)
            - `nl` - Dutch
            - `pl` - Polish
            - `ru` - Russian
            - `uk` - Ukrainian
            - `zh-CN` - Chinese (Traditional)

            You can see a list of all parameters [here](https://github.com/iv-org/documentation/blob/7ddae352a392b7bde9477d60e38c841003e5204e/List-of-URL-parameters.md).
        """

        _to_strip = instance.uri if hasattr(instance, 'uri') else instance
        self.instance_url = _to_strip.strip('/') # remove trailing slash from the URL

        self.session = session_object

        # Requires to have Tor installed & proxies must be running (note: untested).
        # (https://www.torproject.org/download/)
        if instance.type == 'onion':
            self.session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

        self.additional_parameters = additional_parameters


    def _get_json(self, uri: str, append_to_api: bool=True, return_class: t.Optional[_RCLS] = BaseInvidiousData, **requests_kwargs) -> t.Union[t.List, t.Dict[str, t.Any], _RCLS]:
        """
            Gets the JSON response from the given URI.

            ### Parameters:
            - `uri` - the API URI to get the JSON response from.
            - `append_to_api` - whether to append `uri` to the instance API URL (e. g.: `https://invidious.instance.tld/api/v1/{uri}`).
            - `return_class` - the class to use to parse the JSON response. If `None`, the JSON response will be returned as a `dict`/`list`.
            - `**parameters` - search parameters to pass to the request.
        """

        _kwargs = requests_kwargs.copy()

        if self.additional_parameters:
            _kwargs['params'] = {**_kwargs.get('params', {}), **self.additional_parameters}

        response = self.session.get(f"{self.instance_url}/api/v1/{uri}" if append_to_api else uri, **_kwargs)
        response.raise_for_status()

        json: t.Dict[str, t.Any] = response.json()

        if return_class is not None:
            return return_class(json)


        return json


    def get_video(self, id: str, **requests_kwargs) -> YoutubeVideo:
        """
            Obtain video data.

            ### Parameters:
            - `id_or_url` - the video ID (part after `?watch=` in YouTube URL).

            ### Tip:
            Use the following RegEx to extract the video ID from a YouTube URL:
    
            ```python
            r'''(?:https?:)?(?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*?[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['"][^<>]*>|<\/a>))[?=&+%\w.-]*'''
            ```

            (from [https://regex101.com/r/OY96XI/1](https://regex101.com/r/OY96XI/1))
        """

        return self._get_json(f"videos/{id}", return_class=YoutubeVideo, **requests_kwargs)


    def get_comments(self, video: t.Union[str, YoutubeVideo], **requests_kwargs) -> Comments:
        """
            Obtains first page of comments for a video.

            ### Tip:

            Use `InvidiousClient.yield_all_comments(video_id)` to yield all comments of a video.

            ### Parameters:
            - `video` - Either a `str` of video ID or `YoutubeVideo` instance.
        """

        return self._get_json(f"comments/{video.video_id if hasattr(video, 'video_id') else video}", return_class=Comments, **requests_kwargs)


    def yield_all_comments(self, video: t.Union[str, YoutubeVideo]) -> t.Generator[Comments, None, None]:
        """
            Yields all comments of a video, until there are none left.

            ### Parameters:
            - `video` - Either a `str` of video ID or `YoutubeVideo` instance.

            ### Note:
            This yields `Comments`, not `Comment`. So, to get just the comments, you need to do a double-loop:

            ```
            for comments in InvidiousClient.yield_all_comments(video):
                for comment in comments:
                    ...
            ```
        """

        comments = self.get_comments(video)

        while comments.continuation is not None:
            yield comments

            comments = self.get_comments(video, params={'continuation': comments.continuation})



    def get_dislike_count(self, video: t.Union[str, YoutubeVideo]) -> RYDData:
        """
            Will make a request to https://returnyoutubedislikeapi.com to fetch dislike count data.

            See https://returnyoutubedislike.com/ for more information about how to return
            dislikes to YouTube.

            Use `InvidiousClient.get_dislike_count(video_id).dislikes` to get just the dislike count of a video.

            ### Parameters:
            - `video` - Either a `str` of video ID or `YoutubeVideo` instance.

            ### Note:
            There are per client rate limits in place of 100 per minute and 10 000 per day.
            This will return a 429 status code indicating that your application should back off.
            (see also https://github.com/Anarios/return-youtube-dislike#api-documentation)
        """

        return self._get_json(f"https://returnyoutubedislikeapi.com/Votes?videoId={video.video_id if hasattr(video, 'video_id') else video}", return_class=RYDData, append_to_api=False)
