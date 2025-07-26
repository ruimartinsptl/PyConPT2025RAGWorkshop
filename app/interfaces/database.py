from abc import ABC, abstractmethod


class DatabaseI(ABC):
    db: object

    @abstractmethod
    def add_text(self, text: str):
        pass

    @abstractmethod
    def get_context(self, question: str) -> list[str]:
        pass
