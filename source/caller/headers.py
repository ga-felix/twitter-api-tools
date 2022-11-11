from abc import ABC, abstractmethod


class Paginator(ABC):

    @abstractmethod
    def get(self, url: str, request: dict) -> dict:
        pass

    @abstractmethod
    def get_pages(self, url: str, request: dict) -> dict:
        pass
