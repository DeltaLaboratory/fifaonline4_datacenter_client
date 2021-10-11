import typing as _typing


USER_AGENT: _typing.Final[str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                                 "Chrome/94.0.4606.71 Safari/537.36"


class URL:
    SCHEME: str = "https"
    HOST: str = "fifaonline4.nexon.com"
    BASE_URL: str = f"{SCHEME}://{HOST}/datacenter/"
    PRICE_GRAPH: str = "PlayerPriceGraph"
