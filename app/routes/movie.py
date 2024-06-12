from uuid import uuid4

from flask import Blueprint, jsonify, request

from ..models.movie import MovieModel
from ..entities.movie import Movie


movie_bp = Blueprint('movie', __name__)


@movie_bp.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@movie_bp.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie is not None:
            return jsonify(movie)
        else:
            return jsonify(movie), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@movie_bp.route('/', methods=['POST'])
def create_movie():
    try:
        movie = Movie(id=str(uuid4()), title=request.json['title'], 
                      duration=request.json['duration'], 
                      released=request.json['released'])
        result = MovieModel.create_movie(movie)

        if result:
            return jsonify({'statusCode': 200, 'id': movie.id})
        else: 
            return jsonify({'statusCode': 500, 'message': 'Error on insert movie'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@movie_bp.route('/<id>', methods=['PUT'])
def update_movie(id):
    try:
        movie = Movie(id=id, title=request.json['title'], 
                      duration=request.json['duration'], 
                      released=request.json['released'])
        result = MovieModel.update_movie(movie)

        if result:
            return jsonify({'statusCode': 200, 'id': movie.id})
        else: 
            return jsonify({'statusCode': 404, 'message': 'Error updating movie'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    

@movie_bp.route('/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = MovieModel.delete_movie(id)
        if movie:
            return jsonify(None), 204
        else:
            return jsonify({'message': 'Objecto no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500
