import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class MozilliansAPI(FunkLoadTestCase):

    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'url')

    def test_happy_path(self):
        server_url = self.server_url
        
        nb_time = 2
        for i in range(nb_time):
            http_response = self.get(server_url, description='Get url: ' + server_url)
            self.assert_(http_response.code == 200, "For " + server_url + "/nExpected a 200 but saw a " + str(http_response.code))

    def test_search_for_email(self):
        server_url = self.server_url + '&email=bsternthal@mozilla.com'

        nb_time = 2
        for i in range(nb_time):
            http_response = self.get(server_url, description='Get url: ' + server_url)
            self.assert_(http_response.code == 200, "For " + server_url + "/nExpected a 200 but saw a " + str(http_response.code))

    def test_get_max_results(self):
        server_url = self.server_url + '&limit=500'

        nb_time = self.conf_getInt('test_get_max_results', 'nb_time')
        for i in range(nb_time):
            http_response = self.get(server_url, description='Get url: ' + server_url)
            self.assert_(http_response.code == 200, "For " + server_url + "/nExpected a 200 but saw a " + str(http_response.code))


if __name__ in ('main', '__main__'):
    unittest.main()
