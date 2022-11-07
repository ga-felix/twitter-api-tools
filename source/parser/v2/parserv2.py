from ..headers import Parser


class ParserV2(Parser):

    def parse(self, entity: dict, exclude=list()) -> dict:
        if not entity:
            raise KeyError('\'Entity\' is empty and cannot be retrieved.')
        entity = self.parse_all(entity)
        return self.exclude_fields(entity, exclude)

    def parse_all(self, entity: dict) -> dict:
        for parser in self.parsers:
            entity = parser.parse_field(entity)
        return entity

    def exclude_fields(self, entity: dict, exclude):
        for key in exclude:
            entity.pop(key, None)
        return entity
