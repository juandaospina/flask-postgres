from app.database.db import get_connection
from app.entities.movie import Movie


class MovieModel():
    @classmethod
    def get_movies(self):
        try:
            conn = get_connection()
            movies = []

            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT id, title, duration, released FROM movie ORDER BY title ASC')
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_json())
            conn.close()
            return movies
        except Exception as exc:
            raise Exception(exc)
        
    @classmethod
    def get_movie(self, id):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT id, title, duration, released FROM movie WHERE id = %s',(id,))
                result = cursor.fetchone()

                movie = None
                if result is not None:
                    movie = Movie(result[0], result[1], result[2], result[3])
                    movie = movie.to_json()
            conn.close()
            return movie
        except Exception as exc:
            raise Exception(exc)
        
    @classmethod
    def create_movie(self, movie):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute(
                    '''INSERT INTO movie (id, title, duration, released) 
                    VALUES (%s, %s, %s, %s)''', 
                    (movie.id, movie.title, movie.duration, movie.released))
                
                affected_rows = cursor.rowcount
                if affected_rows == 1:
                    conn.commit()
                    return True
                elif affected_rows != 1:
                    conn.rollback() 
                    return False
            conn.close()
        except Exception as exc:
            raise Exception(exc)
        
    @classmethod
    def update_movie(self, movie):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute(
                    '''
                    UPDATE movie 
                    SET title = %s, duration = %s, released = %s 
                    WHERE id = %s''', 
                    (movie.title, movie.duration, movie.released, movie.id))
                
                affected_rows = cursor.rowcount
                if affected_rows == 1:
                    conn.commit()
                    return True
                elif affected_rows != 1:
                    conn.rollback() 
                    return False
            conn.close()
        except Exception as exc:
            raise Exception(exc)
        
    @classmethod
    def delete_movie(self, id):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM movie WHERE id = %s',(id,))
                result = cursor.rowcount
                if result == 1:
                    conn.commit()
                    return True
                elif result != 1:
                    conn.rollback() 
                    return False
            conn.close()
            return False
        except Exception as exc:
            raise Exception(exc)