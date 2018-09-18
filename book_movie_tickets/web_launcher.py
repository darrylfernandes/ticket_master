from flask import Flask, request, render_template, redirect, url_for, jsonify
from book_movie_tickets.services.ticket_service import extract_movies, extract_cheapest_ticket_info


rester_app = Flask(__name__, static_folder='static')
rester_app.secret_key = '@123webjetapitest@321'


@rester_app.route('/', methods=['GET'])
def index():
    return redirect(url_for('home_page'))


@rester_app.route('/home_page', methods=['GET', 'POST'])
def home_page():
    return render_template('home_page.html')


@rester_app.route('/get_movies_list', methods=['GET', 'POST'])
def get_movies_list():
    unique_movie_dict = extract_movies()
    # extract_cheapest_ticket_info(unique_movie_dict)
    return render_template('movies_list.html', movie_choices=unique_movie_dict)


@rester_app.route('/get_cheap_price', methods=['GET', 'POST'])
def get_cheap_price():
    movie_details = extract_cheapest_ticket_info(unique_movie_dict)
    return jsonify(movie_details)


if __name__ == '__main__':
    rester_app.run()


