from dataclasses import dataclass as _dataclass


@_dataclass(frozen=True)
class Player:
    price: int
