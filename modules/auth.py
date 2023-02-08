from os import getenv
from mysql.connector.cursor import MySQLCursor
from modules.db_queries import INSERT_NEW_REFRESH_TOKEN, INSERT_NEW_USER, SELECT_USER_BY_EMAIL

from modules.models import LogInUser, SignUpUser, User
import jwt
import datetime as dt


class Auth:
    __cursor: MySQLCursor
    __secret: str

    def __init__(self, cursor: MySQLCursor) -> None:
        self.__cursor = cursor
        self.__secret = getenv("SECRET")  # type: ignore

        if not self.__secret:
            raise OSError("Enviroment variable SECRET doesn't exist")

    def __new_access_token(self, _id) -> str:

        return jwt.encode(
            {
                "id": _id,
                "exp": dt.datetime.now()
            },
            self.__secret
        )

    def new_refresh_token(self, _id) -> str:
        refresh_token = jwt.encode(
            {
                "id": _id
            },
            self.__secret
        )

        self.__cursor.execute(INSERT_NEW_REFRESH_TOKEN, [_id, refresh_token])

        return refresh_token

    def login(self, user: LogInUser) -> User:
        self.__cursor.execute(SELECT_USER_BY_EMAIL, user.email)
        _user = self.__cursor.fetchone()

    def signup(self, user: SignUpUser) -> User:
        fetches = self.__cursor.execute(INSERT_NEW_USER, user.dict(), multi=True)
        fetch = [fetch.fetchone() for fetch in fetches if fetch.with_rows][0]
        print(fetch)

        new_user = User(**fetch)
        new_user.access_token = self.__new_access_token(new_user.uid)

        return new_user
