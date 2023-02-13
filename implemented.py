from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from service.director_ser import DirectorService
from service.genre_ser import GenreService
from service.movie_ser import MovieService
from service.user_ser import UserService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)