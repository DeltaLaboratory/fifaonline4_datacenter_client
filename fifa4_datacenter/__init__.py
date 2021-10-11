import random
import random as _random

import httpx as _httpx
import bs4 as _bs4

from . import model as _model
from .statics import URL as _URL
from .statics import USER_AGENT as _USER_AGENT


class Client:
    def __init__(self) -> None:
        self.client: _httpx.AsyncClient = _httpx.AsyncClient(base_url=_URL.BASE_URL)

    async def get_player_info(self, spid: str) -> _model.Player:
        parser = _bs4.BeautifulSoup(
            markup=(await self.client.post(
                url=_URL.PRICE_GRAPH,
                headers={
                    "User-Agent": _USER_AGENT,
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                },
                data={
                    "spid": spid,
                    "n1strong": 1,
                    "rd": f"{random.random()}"
                }
            )).text
            , features="lxml")
        return _model.Player(
            price=int(
                parser.select("body > div.header > div.add_info > div > strong ")[0].string.strip()
                    .replace("BP", "")
                    .replace(",", "")
            )
        )
