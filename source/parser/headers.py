from abc import ABC, abstractmethod


class SubParser(ABC):

    @abstractmethod
    def parse_field(self, entity: dict()) -> dict:
        pass


class Parser(ABC):

    def __init__(self, parsers: list[SubParser]):
        self.parsers = parsers

    @abstractmethod
    def parse(self, entity: dict, exclude=list()) -> list:
        pass
