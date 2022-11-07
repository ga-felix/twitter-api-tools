import unittest
from source.parser import ParserV2, MetricsParserV2


class AuthorParserV2Test(unittest.TestCase):

    def setUp(self):
        self.sample_author = {
            'id': '123',
            'username': 'juanzin',
            'description': None,
            'public_metrics': {
                'followers_count': '123',
                'following_count': 123,
                'tweet_count': '123',
                'listed_count': '123'
            },
            'verified': 'true',
            'created_at': '2013-12-14T04:35:55.000Z'}
        self.author_parser = ParserV2(
            [MetricsParserV2()])

    def test_parse(self):
        found_author = self.author_parser.parse(self.sample_author)
        expected_author = {
            'id': '123',
            'username': 'juanzin',
            'description': None,
            'followers_count': '123',
            'following_count': 123,
            'tweet_count': '123',
            'listed_count': '123',
            'verified': 'true',
            'created_at': '2013-12-14T04:35:55.000Z'
        }
        self.assertEquals(found_author, expected_author)

    def test_parse_filtered(self):
        found_author = self.author_parser.parse(
            self.sample_author, exclude=['id', 'followers_count'])
        expected_author = {
            'username': 'juanzin',
            'description': None,
            'following_count': 123,
            'tweet_count': '123',
            'listed_count': '123',
            'verified': 'true',
            'created_at': '2013-12-14T04:35:55.000Z'
        }
        self.assertEquals(found_author, expected_author)

    def test_parse_missing_author(self):
        self.assertRaises(KeyError, self.author_parser.parse, dict())

    def test_parse_missing_public_metrics(self):
        missing_metrics_author = {'author': {'id': '123'}}
        self.assertRaises(
            KeyError, self.author_parser.parse, missing_metrics_author)

    def test_parse_all(self):
        author = self.author_parser.parse_all(self.sample_author)
        nested_fields = [field for field in author if type(
            author[field]) == dict()]
        self.assertTrue(len(nested_fields) == 0)

    def test_exclude_fields(self):
        fields_to_exclude = ['id', 'followers_count']
        author = self.author_parser.exclude_fields(
            self.sample_author, exclude=fields_to_exclude)
        self.assertTrue('id' not in author and 'followers_count' not in author)
