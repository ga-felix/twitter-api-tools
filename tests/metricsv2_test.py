import unittest
from source.parser import MetricsParserV2


class MetricsParserV2Test(unittest.TestCase):

    def setUp(self):
        self.metrics_parser = MetricsParserV2()
        self.metrics = {
            'public_metrics': {
                'followers_count': '123',
                'following_count': 123,
                'tweet_count': '',
                'listed_count': None
                }}

    def test_add_public_metrics_value(self):
        metrics = self.metrics_parser.add_public_metrics_values(self.metrics)
        expected_output = {
            'public_metrics': {
                'followers_count': '123',
                'following_count': 123,
                'tweet_count': '',
                'listed_count': None
                },
            'followers_count': '123',
            'following_count': 123,
            'tweet_count': '',
            'listed_count': None
            }
        self.assertEquals(metrics, expected_output)

    def test_parse_field(self):
        parsed_metrics = self.metrics_parser.parse_field(self.metrics)
        expected_output = {
            'followers_count': '123',
            'following_count': 123,
            'tweet_count': '',
            'listed_count': None
            }
        self.assertEquals(parsed_metrics, expected_output)

    def test_parse_missing_metrics(self):
        self.assertRaises(KeyError, self.metrics_parser.parse_field, dict())
