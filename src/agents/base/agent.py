from abc import ABC, abstractmethod

class IAgent(ABC):
    @abstractmethod
    def run(self, data):
        pass

    def fallback(self, data):
        print(f"[Fallback] {self.__class__.__name__}")
        return data
