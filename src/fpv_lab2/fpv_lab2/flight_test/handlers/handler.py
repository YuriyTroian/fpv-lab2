from abc import ABC, abstractmethod


class FlightStateHandler(ABC):
    @abstractmethod
    def handle(self, node) -> None:
        pass
