import unittest
from source.parser import TwitterAuthorParser, TwitterMetricsParser


class TwitterAuthorParserTest(unittest.TestCase):

    def setUp(self):
        self.sample_author = {
            'author': {
                'id': '123',
                'username': 'juanzin',
                'description': '',
                'public_metrics': {
                    'followers_count': '123',
                    'following_count': '123',
                    'tweet_count': '123',
                    'listed_count': '123'
                },
                'verified': 'true',
                'created_at': '2013-12-14T04:35:55.000Z'
            }}
        self.author_parser = TwitterAuthorParser(TwitterMetricsParser())

    def test_parse(self):
        found_author = self.author_parser.parse_field(self.sample_author)
        expected_author = {
            'id': '123',
            'username': 'juanzin',
            'description': '',
            'followers_count': '123',
            'following_count': '123',
            'tweet_count': '123',
            'listed_count': '123',
            'verified': 'true',
            'created_at': '2013-12-14T04:35:55.000Z'
        }
        self.assertEquals(found_author, expected_author)

    def test_parse_missing_author(self):
        self.assertRaises(KeyError, self.author_parser.parse_field, dict())
