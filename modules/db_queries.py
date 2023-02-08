SELECT_USER_BY_EMAIL = "SELECT * FROM `user` WHERE email=%s"

INSERT_NEW_USER = """
INSERT INTO `user` (
    name,
    surname,
    email,
    password
) VALUES (
    %(name)s,
    %(surname)s,
    %(email)s,
    %(password)s
);
SELECT * FROM `user` WHERE email=%(email)s;"""

INSERT_NEW_REFRESH_TOKEN = """
INSERT INTO `refresh_token` (
    owner,
    token
) VALUES (
    %s, %s
)"""