import typing as t

from requests import Session

from .models import BaseInvidiousData
from .models.instances import Instance, choose_instance



class InvidiousAPIClient:
    def __init__(self, instance: t.Union[Instance, str, bytes]=choose_instance(), session_object: Session = Session()) -> None:
        """
            Initializes a new Invidious API Client.

            ### Parameters:
            - `instance` - the instance URL or object to use.
            - `session` - the session object to use.
        """

        self.instance_url = instance.uri if hasattr(instance, 'uri') else instance
        self.session = session_object

        # Requires to have Tor installed & running.
        # (https://www.torproject.org/download/)
        if instance.type == 'onion':
            self.session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}


    def _get_json(self, uri: str, return_class: t.Optional[t.Type[BaseInvidiousData]] = BaseInvidiousData, **parameters) -> t.Union[t.List, t.Dict[str, t.Any]]:
        """
            Gets the JSON response from the given URI.

            ### Parameters:
            - `uri` - the URI to get the JSON response from.
            - `return_class` - the class to use to parse the JSON response. If `None`, the JSON response will be returned as a `dict`/`list`.
            - `**parameters` - search parameters to pass to the request.
        """

        response = self.session.get(f"{self.instance_url}{uri}", params=parameters)
        response.raise_for_status()

        if return_class is not None:
            return return_class(response.json())


        return response.json()
