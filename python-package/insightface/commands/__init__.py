from abc import ABC, abstractmethod
from argparse import ArgumentParser, _SubParsersAction


class BaseInsightFaceCLICommand(ABC):
    @staticmethod
    @abstractmethod
    def register_subcommand(parser: _SubParsersAction[ArgumentParser]):
        raise NotImplementedError()

    @abstractmethod
    def run(self):
        raise NotImplementedError()
