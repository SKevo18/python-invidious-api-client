import typing as t

import requests

from datetime import datetime
from functools import lru_cache

from invidious_api_client.models import BaseInvidiousData



class Instance(BaseInvidiousData):
    """
        Invidious instance data.
    """


    class InstanceStats(BaseInvidiousData):
        """
            Invidious instance stats.
        """


        @property
        def version(self) -> str:
            """
                Returns the version of stats.
            """

            return self.data.get('version')


        @property
        def software_name(self) -> str:
            """
                The name of the software running on the instance. This should be `"invidious"`.
            """

            return self.data.get('software', {}).get('name')


        @property
        def software_version(self) -> str:
            """
                Returns the software version
            """

            return self.data.get('software', {}).get('version')


        @property
        def software_branch(self) -> str:
            """
                The repository branch of the software
            """

            return self.data.get('software', {}).get('branch')


        @property
        def open_registrations(self) -> bool:
            """
                Returns whether the instance is accepting new registrations.
            """

            return self.data.get('openRegistrations')


        @property
        def usage(self) -> t.Dict[str, t.Dict[str, int]]:
            """
                Returns the instance usage statistics in `dict` format.
            """

            return self.data.get('usage', {})


        @property
        def total_users(self) -> int:
            """
                Returns the total number of users.
            """

            return self.usage.get('users', {}).get('total')


        @property
        def users_active_half_year(self) -> int:
            """
                Returns the number of active users in the last 6 months.
            """

            return self.usage.get('users', {}).get('activeHalfyear')


        @property
        def users_active_month(self) -> int:
            """
                Returns the number of active users in the last month.
            """

            return self.usage.get('users', {}).get('activeMonth')


        @property
        def metadata(self) -> t.Dict[str, int]:
            """
                Returns the instance metadata.
            """

            return self.data.get('metadata', {})


        @property
        def updated_at(self) -> datetime:
            """
                When were stats updated at.
            """

            return datetime.fromtimestamp(self.metadata.get('updatedAt'))


        @property
        def last_channel_refreshed_at(self) -> datetime:
            """
                When was the last channel refreshed.
            """

            return datetime.fromtimestamp(self.metadata.get('lastChannelRefreshedAt'))



    @property
    def host(self) -> str:
        """
            Returns the instance's hostname/ID
        """

        return self.json[0]


    @property
    def json(self) -> t.Dict[str, t.Any]:
        """
            Returns the instance's JSON data
        """

        return self.data[1]


    @property
    def flag(self) -> str:
        """
            Returns the instance's flag
        """

        return self.json.get('flag')


    @property
    def region(self) -> str:
        """
            Returns the instance's region/country in ISO 3166-1 alpha-2 format
        """

        return self.json.get('region')


    @property
    def stats(self) -> t.Optional[InstanceStats]:
        """
            The instance's stats.
            Returns `None` if the instance does not have statistics enabled/available.
        """

        data: dict = self.json.get('stats', {})
        error: t.Optional[str] = data.get('error', None)

        if error is not None:
            return None

        return self.InstanceStats(data)


    @property
    def type(self) -> str:
        """
            Returns the instance's type (`"https"` or `"http"` or `"onion"`)
        """

        return self.json.get('type')


    @property
    def uri(self) -> str:
        """
            Returns the instance's URI
        """

        return self.json.get('uri')



    class Monitor(BaseInvidiousData):
        """
            Instance's UptimeRobot monitor data.
        """


        @property
        def monitor_id(self) -> str:
            """
                Returns the monitor's ID
            """

            return self.data.get('monitorId')
        

        @property
        def created_at(self) -> datetime:
            """
                When was this monitor created at.
            """

            return datetime.fromtimestamp(self.data.get('createdAt'))
        

        @property
        def status_class(self) -> str:
            """
                Returns the monitor's status class.
            """

            return self.data.get('statusClass')


        @property
        def name(self) -> str:
            """
                The monitor's name, usually the instance's hostname.
            """

            return self.data.get('name')


        @property
        def url(self) -> t.Optional[str]:
            """
                The monitor's URL, usually `None`
            """

            return self.data.get('url', None)


        @property
        def type(self) -> str:
            """
                The monitor's type, usually `"HTTP(s)"`
            """

            return self.data.get('type')



        class _Ratio(BaseInvidiousData):
            """
                Monitor's uptime ratio.
            """


            @property
            def ratio(self) -> t.Optional[float]:
                """
                    The uptime percentage ratio for specific time period.
                    E. g.: how many percent of the specific period was this instance up?

                    For example, if you want to know how many percent of the last 30 days was this instance up, use
                    `Monitor.two_month_ratio.ratio`
                """

                raw: t.Optional[str] = self.data.get('ratio', None)

                if raw is not None:
                    return float(raw)

                return None


            @property
            def label(self) -> str:
                """
                    Returns the ratio label. `"success"` or `"warning"`.
                """

                return self.data.get('label')



        @property
        def daily_ratios(self) -> t.List[_Ratio]:
            """
                Returns the monitor's daily ratios.
            """

            return [self._Ratio(data) for data in self.data.get('dailyRatios', [])]


        @property
        def two_month_ratio(self) -> _Ratio:
            """
                Returns the monitor's 2 months/90 days ratios.
            """

            return self._Ratio(self.data.get('90dRatio'))


        @property
        def month_ratio(self) -> _Ratio:
            """
                Returns the monitor's 1 month/30 days ratios.
            """

            return self._Ratio(self.data.get('30dRatio'))



    @property
    def monitor(self) -> t.Optional[Monitor]:
        """
            Returns the instance's UptimeRobot monitor data
        """

        raw_monitor = self.json.get('monitor', None)

        if raw_monitor is not None:
            return self.Monitor(raw_monitor)

        return None



class InstancesList(BaseInvidiousData):
    """
        Invidious API Instances List class.
    """


    def __iter__(self) -> t.Iterator[Instance]:
        """
            Returns an iterator over the instances.
        """

        return iter(self.instances)


    @property
    def instances(self) -> t.List[Instance]:
        """
            Get instances list.
        """

        return [Instance(raw_instance) for raw_instance in self.data]



def get_instances(*args, **kwargs) -> InstancesList:
    """
        Obtains all instances as `InstancesList`.

        `*args` and `**kwargs` are passed to `requests.get`.
    """

    response = requests.get('https://api.invidious.io/instances.json', *args, **kwargs)
    response.raise_for_status()

    return InstancesList(response.json())



@lru_cache(maxsize=3)
def choose_instance(prefer_country_codes: t.Optional[t.List[str]]=None, no_onions: bool=True, only_accessible: bool=True) -> Instance:
    """
        Chooses the first instance in the API to use.

        ### Warning:

        Not all instances allow access to their API!

        ### Parameters:
        - `no_onions` - If `True`, Tor instances will be excluded.
        - `prefer_country_codes` - A list of country codes to prefer (for lower ping). Common ones: `['NL', 'DE']`, `['US']`
        - `only_accessible` - If `True`, only instances with accessible API will be returned.
    """

    for instance in get_instances(params={'sort_by': 'health'}).instances:
        if only_accessible and requests.head(f"{instance.uri.strip('/')}/api/v1/videos/dQw4w9WgXcQ").status_code != 200:
            continue

        if no_onions and instance.type == 'onion':
            continue

        if (prefer_country_codes is not None) and (instance.region is not None) and (instance.region.lower() in prefer_country_codes):
            return instance

        return instance
