import pytest
from httpx import Response

from myapp.main import BaseRequest, RequestExecutor


class MockRequest(BaseRequest):
    def get(self, url):
        response = Response(status_code=200, text="<title>Something</title>")
        return response


# def test_myfunc():
#     output = my_func("Kevin")
#     assert output == "Kevin"
#


def test_request():
    request = MockRequest()
    exec = RequestExecutor(request)
    output = exec.get_page("https://example.com")
    assert output.text == "<title>Something</title>"
    assert output.status_code == 200
