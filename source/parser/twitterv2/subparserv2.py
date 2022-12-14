from ..headers import SubParser


class TwitterMetricsParser(SubParser):

    def parse_field(self, entity: dict) -> dict:
        if 'public_metrics' not in entity:
            raise KeyError('\'public_metrics\' does not exist.')
        entity = self.add_public_metrics_values(entity)
        del entity['public_metrics']
        return entity

    def add_public_metrics_values(self, entity: dict) -> dict:
        for key in entity['public_metrics']:
            entity[key] = entity['public_metrics'][key]
        return entity


class TwitterAuthorParser(SubParser):

    def __init__(self, metrics_parser: SubParser):
        self.metrics_parser = metrics_parser

    def parse_field(self, entity: dict) -> dict:
        if 'author' not in entity:
            raise KeyError('\'author\' does not exist.')
        entity = self.add_author_values(entity)
        del entity['author']
        if 'public_metrics' in entity:
            entity = self.metrics_parser.parse_field(entity)
        return entity

    def add_author_values(self, entity: dict) -> dict:
        for key in entity['author']:
            entity[key] = entity['author'][key]
        return entity
