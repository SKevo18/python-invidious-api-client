# Python Invidious API Client

A client for [Invidious'](https://invidious.io/) JSON API. No Google API key is required.

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

I support the idea of every website with public content having an easy-to-access REST API, which YouTube doesn't. This project was made for people that want a cheap and quick way to access Google's API anonymously, without having to worry about all the API keys and paywall nonsense.

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

| Crypto            | Address                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Bitcoin           | [E-mail me](mailto:me@kevo.link)                                                                  |
| Ethereum          | `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`                                                      |
| Litecoin          | `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`                                                              |
| Dash              | `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`                                                              |
| Zcash:            | `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`                                                             |
| Dogecoin:         | `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`                                                              |
| Ripple:           | `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`                                                              |
| Monero:           | `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS` |
| Bitcoin Cash:     | `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`                                                      |
| Ethereum Classic: | `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`                                                      |

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
