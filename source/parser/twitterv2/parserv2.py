from ..headers import Parser


class TwitterParser(Parser):

    def parse(self, entity: dict) -> dict:
        if not entity:
            raise KeyError('\'Entity\' is empty and cannot be retrieved.')
        return self.parse_all(entity)

    def parse_all(self, entity: dict) -> dict:
        for parser in self.parsers:
            entity = parser.parse_field(entity)
        return entity
