#!/usr/bin/env python3


import httpx


class BaseRequest:
    def get(self, url):
        pass


class Request(BaseRequest):
    def __init__(self):
        pass

    def get(self, url):
        return httpx.get(url)


class RequestExecutor:
    def __init__(self, BaseRequest):
        self.BaseRequest = BaseRequest

    def my_func(self, name):
        print(name)
        return name

    def get_page(self, url):
        response = self.BaseRequest.get(url)
        return response


if __name__ == "__main__":
    request = Request()
    exec = RequestExecutor(request)
    print(exec.get_page("https://example.com"))
