import json
import urllib.request
import socket


class InvalidJsonException(Exception):
    pass


def extract_data(url, data=None, headers=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, return_data_type='json'):
    """

    :param url: resource locator
    :param data: data to be posted along with the Url
    :param headers: additional http request headers such as access token
    :param timeout: timeout for a url request. Defaulted to socket._GLOBAL_DEFAULT_TIMEOUT
    :param return_data_type: The data format type expected to be returned when request is made to the url (defaulted to json)
                      Options: json, text, xml. Currently only json is supported
    :return: data format specified by data_type input parameter
    """

    if data and type(data) == dict:
        data = urllib.parse.urlencode(data)

    req = urllib.request.Request(url, data, headers if headers and type(headers) == dict else dict())

    response = urllib.request.urlopen(req, timeout=timeout)

    if return_data_type == 'json':
        try:
            return json.loads(response.read().decode())
        except ValueError:
            raise InvalidJsonException('Resource data is not a valid Json format')


if __name__ == '__main__':
    # extract_data('http://webjetapitest.azurewebsites.net/api/filmworld/movie/cw0080684', data=None,
    #              headers={'x-access-token': 'sjd1HfkjU83ksdsm3802k'})

    print(extract_data('http://webjetapitest.azurewebsites.net/api/cinemaworld/movie/cw0120915', data=None,
                 headers={'x-access-token': 'sjd1HfkjU83ksdsm3802k'}))

    print(extract_data('http://webjetapitest.azurewebsites.net/api/filmworld/movie/fw0120915', data=None,
                 headers={'x-access-token': 'sjd1HfkjU83ksdsm3802k'}))
