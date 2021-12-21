import typing as t



class BaseInvidiousData:
    """
        Base Invidious JSON data class.
    """

    def __init__(self, data: t.Union[dict, list] = {}) -> None:
        self.data = data
