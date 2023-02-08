from os import getenv
import mysql.connector as mysql


database = mysql.connect(
    user         = getenv("SQL_USER"),
    password     = getenv("SQL_PASSWORD"),
    host         = getenv("DATABASE_HOST"),
    port         = int(getenv("DATABASE_PORT")),  # type: ignore
    db           = getenv("DATABASE"),
    autocommit   = True
)

cursor = database.cursor(dictionary=True)