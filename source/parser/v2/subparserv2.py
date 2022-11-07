from ..headers import SubParser


class MetricsParserV2(SubParser):

    def parse_field(self, entity: dict()) -> dict:
        if 'public_metrics' not in entity:
            raise KeyError('\'public_metrics\' does not exist.')
        entity = self.add_public_metrics_values(entity)
        del entity['public_metrics']
        return entity

    def add_public_metrics_values(self, entity: dict) -> dict:
        for key in entity['public_metrics']:
            entity[key] = entity['public_metrics'][key]
        return entity

    def get_parsed_field(self) -> str:
        return 'public_metrics'
