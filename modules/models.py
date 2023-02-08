from pydantic import BaseModel


class User(BaseModel):
    uid:           int | None = None
    name:          str | None = None
    surname:       str | None = None
    email:         str | None = None
    password:      str | None = None
    family:        str | None = None
    access_token:  str | None = None

class LogInUser(BaseModel):
    email:    str
    password: str

class SignUpUser(BaseModel):
    name:     str
    surname:  str
    email:    str
    password: str