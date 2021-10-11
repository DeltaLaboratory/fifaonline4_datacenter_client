from dataclasses import dataclass as _dataclass


@_dataclass(frozen=True)
class Player:
    price: int
    max_price: int
    min_price: int
