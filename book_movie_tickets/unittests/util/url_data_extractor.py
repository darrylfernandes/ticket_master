"""
    File Name   : unittests/util/url_data_extractor.py
    Author      : Darryl Fernandes
    Description : Unit test script to validate the utility methods to extract different formats of data from URL
    Source File : util/url_data_extractor.py
"""

import unittest
from unittest import mock
from book_movie_tickets.util.url_data_extractor import extract_data


class TestUrlDataExtractor(unittest.TestCase):

    def setUp(self):
        self.baseurl = 'unittest://mocking.com/'

    def test_extract_data_having_correct_json_format(self):
        """
            Handles the case wherein if the source url has correct json format data,
            then the extract_data method returns a json data
        """
        startendpoint = '/api/provider/movies'
        url = '{}{}'.format(self.baseurl, startendpoint)

        with mock.patch('urllib.request.urlopen') as mock_request:
            mock_response = mock_request.return_value
            mock_response_read = mock_response.read.return_value
            mock_response_read.decode.return_value = '{"a":20, "b":[ {"x": "doll"}, {"x": "hotwheels"} ]}'
            json_data = extract_data(url)
            self.assertEqual(json_data, {"a": 20, "b": [{"x": "doll"}, {"x": "hotwheels"}]},
                             msg="Received unexpected json response")

    def test_extract_data_having_incorrect_json_format(self):
        """
            Handles the case wherein if the source url has incorrect json format data,
            then the extract_data method throws an error
        """
        startendpoint = '/api/provider/movies'
        url = '{}{}'.format(self.baseurl, startendpoint)
        with mock.patch('urllib.request.urlopen') as mock_request:
            mock_response = mock_request.return_value
            mock_response_read = mock_response.read.return_value
            mock_response_read.decode.return_value = 'Some incorrect non-json data format '
            self.assertRaises(Exception, extract_data, url)


if __name__ == '__main__':
    unittest.main()
