from source.parser import ParserV2, MetricsParserV2, AuthorParserV2


tparser = MetricsParserV2()
metric_parser = ParserV2(tparser)
author = {'author': {
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
author_parser = AuthorParserV2()
print(author_parser.parse_field(author))