from ..headers import Paginator
from requests import request as req


class TwitterPaginator(Paginator):

    def get(self, url: str, request: dict) -> dict:
        response = req(
            "GET", url, headers=request['header'], params=request['body'])
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def get_pages(self, url: str, request: dict) -> dict:
        while True:
            response = self.get(url, request)
            yield response
            if not self.has_next_token(response):
                break
            next_token = response['meta']['next_token']
            request = self.append_next_token(request, next_token)

    def has_next_token(self, response: dict):
        return 'meta' in response and 'next_token' in response['meta']

    def append_next_token(self, request: dict, next_token: str) -> dict:
        request['next_token'] = next_token
        return request
