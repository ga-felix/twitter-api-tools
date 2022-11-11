from source.parser import TwitterParser, TwitterMetricsParser, TwitterAuthorParser


tparser = TwitterMetricsParser()
metric_parser = TwitterParser(tparser)
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
author_parser = TwitterAuthorParser()
print(author_parser.parse_field(author))