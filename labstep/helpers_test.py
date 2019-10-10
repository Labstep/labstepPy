from .helpers import url_join

class TestHelpers:
    def test_url_join(self):
        assert url_join("http://api.labstep.com", "/public-api/user/login") == "http://api.labstep.com/public-api/user/login"
