import unittest
from unittest.mock import Mock

from source.caller import TwitterPaginator


class TwitterPaginatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.paginator = TwitterPaginator()
        self.request = {
            'header': '',
            'body': {
                'query': 'from:2244994945',
                'tweet.fields': 'id,text,created_at,author_id'
            }
        }
        self.api_response = [
            {
                'data': [
                    {
                        'id': '1307025659294674945',
                        'public_metrics': {
                            'retweet_count': 11,
                            'reply_count': 2,
                            'like_count': 70,
                            'quote_count': 1
                        },
                        'text': 'Sample tweet.',
                        'created_at': '2020-09-18T18:36:15.000Z',
                        'author_id': '2244994945',
                        'referenced_tweets': [
                            {
                                'type': 'replied_to',
                                'id': '1304102743196356610'
                            }
                        ],
                    }
                ],
                'meta': {
                    'result_count': '1',
                    'next_token': '123'
                }
            },
            {
                'data': [
                    {
                        'id': '1307025659294674946',
                        'public_metrics': {
                            'retweet_count': 0,
                            'reply_count': 0,
                            'like_count': 1,
                            'quote_count': 0
                        },
                        'text': 'Sample tweet.',
                        'created_at': '2020-09-18T18:36:15.000Z',
                        'author_id': '2244994945'
                    }
                ],
                'meta': {
                    'result_count': '1'
                }
            }
        ]

    def test_append_next_token(self):
        next_token, previous_request = '123', dict()
        request = self.paginator.append_next_token(
            previous_request, next_token)
        self.assertEquals(request['next_token'], '123')

    def test_get_pages(self):
        paginator = TwitterPaginator()
        paginator.get = Mock()
        paginator.get.side_effect = self.api_response
        pages = paginator.get_pages('https://api.twitter.com/2/',
                                    self.request)
        first_page, second_page = next(pages), next(pages)
        self.assertEquals([first_page, second_page], self.api_response)
