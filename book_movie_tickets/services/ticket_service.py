"""
    File Name   : services/ticket_service.py
    Author      : Darryl Fernandes
    Description : Service method to fetch all movies and its details from providers
    Unit test File : unittests/services/weight_calculator.py
"""

from book_movie_tickets.app_constants import BASE_URL, START_ENDPOINT_ALL_MOVIES, START_ENDPOINT_MOVIE_DETAILS, \
    MOVIE_TICKET_PROVIDERS, URL_HEADERS, TIMEOUT
from book_movie_tickets.util.url_data_extractor import extract_data, InvalidJsonException
import traceback
import socket
from urllib.error import HTTPError

def extract_movies():
    """

    :param url: resource locator
    :param data_type: The data format type expected to be returned when request is made to the url (defaulted to json)
                      Options: json, text, xml. Currently only json is supported
    :return: json
    """
    unique_movie_dict = {}

    for provider in MOVIE_TICKET_PROVIDERS:
        endpoint_all_movies_by_provider = START_ENDPOINT_ALL_MOVIES.format(provider)
        all_movies_provider_url = '{}{}'.format(BASE_URL, endpoint_all_movies_by_provider)

        try:
            all_movies_by_provider_json = extract_data(all_movies_provider_url, headers=URL_HEADERS, timeout=TIMEOUT,
                                                       return_data_type='json')

            if 'Movies' in all_movies_by_provider_json:
                for movie in all_movies_by_provider_json.get('Movies', []):
                    unique_movie_id = (movie.get('Title'), movie.get('Year'))
                    if unique_movie_id not in unique_movie_dict:
                        unique_movie_dict[unique_movie_id] = {k: movie.get(k, "") for k in ('Title', 'Year',
                                                                                            'Poster', 'Type')}

                    if 'Providers' not in unique_movie_dict[unique_movie_id]:
                        unique_movie_dict[unique_movie_id]['Providers'] = [{provider: movie.get('ID')}]
                    else:
                        unique_movie_dict[unique_movie_id]['Providers'].append({provider: movie.get('ID')})

        except (HTTPError, InvalidJsonException, socket.timeout):
            # Log this error for technical analysis since it is an issue from the provider end
            print(traceback.format_exc())

    return unique_movie_dict


def extract_cheapest_ticket_info(movie_details):
    cheapest_price = 'No Info. available'

    for provider_detail in movie_details.get('Providers', []):
        for provider, movie_id in provider_detail.items():

            endpoint_movie_details_by_provider = START_ENDPOINT_MOVIE_DETAILS.format(provider, movie_id)
            movie_details_by_provider_url = '{}{}'.format(BASE_URL, endpoint_movie_details_by_provider)

            try:
                movie_details_by_provider_json = extract_data(movie_details_by_provider_url,
                                                              headers=URL_HEADERS, timeout=TIMEOUT,
                                                              return_data_type='json')
                movie_price_by_provider = movie_details_by_provider_json.get('Price', 'No Info. available')

                if movie_price_by_provider != 'No Info. available':
                    try:
                        movie_price_by_provider = float(movie_price_by_provider)

                        if type(cheapest_price) != float or movie_price_by_provider < cheapest_price:
                            cheapest_price = movie_price_by_provider
                            movie_details['Details'] = movie_details_by_provider_json

                    except ValueError:
                        print('Ticket price ("{}") provided by "{}" for the movie "{}" is invalid'.format(
                            movie_price_by_provider, provider, movie_details.get('Title')))
            except (HTTPError, InvalidJsonException, socket.timeout):
                # Log this error for technical analysis since it is an issue from the provider end
                print(traceback.format_exc())

    movie_details['Price'] = cheapest_price
    return movie_details


if __name__ == '__main__':
    print('Execution Started...')
    print(extract_movies())
    print('Execution Completed...')
