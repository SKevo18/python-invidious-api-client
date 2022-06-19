# Python Invidious API Client

A client for [Invidious'](https://invidious.io/) JSON API. No Google API key is required.

Under minimal maintenance. Please, also see my [Piped API client](https://github.com/CWKevo/python-piped-api-client) for a maintained alternative.

## Installation

```bash
pip install invidious-api-client
```

## Basic Usage

```python
from invidious_api_client import InvidiousClient

CLIENT = InvidiousClient()
CLIENT.get_video('dQw4w9WgXcQ')
```

See more examples in the `tests/` or `examples/` folders.

## Warning

Mass scraping of instances will lead them to being blocked by Google relatively fast. Some instances may block their API access entirely
While this package tries to automatically find a working one, I do not encourage mass scraping nor support blocking these innocent instances.

But then again, being blocked is on responsibility of the instance admins. In other words, they should put a security measures in order to avoid being blocked.
Some instances probably use proxies to hide their IP address from Google, therefore their API access isn't limited and they can handle many connections in a
shorter period of time more than the ones that are at the risk of being blocked by Google.

I support the idea of every website with public content having an easy-to-access REST API. This project was made for people that want a cheap and quick way to access Google's API anonymously, without having to worry about all the API keys and other walls.

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via [PayPal](https://www.paypal.com/donate/?hosted_button_id=XDUWS5K6947HY).
