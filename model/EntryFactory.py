from model import Changelog


class EntryFactory:

    @staticmethod
    def makeEntry(self, version, date, body, file) -> Changelog:
        return None