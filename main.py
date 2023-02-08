from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from modules.auth import Auth
from modules.database import cursor
from modules.db_queries import SELECT_USER_BY_EMAIL
from modules.log import LOGGER
from modules.models import SignUpUser, User
from modules.resources import Resources


app = FastAPI()
auth = Auth(cursor)

RESOURCES_DIR = "resources/"
R = Resources(RESOURCES_DIR)
app.mount(
    "/resources",
    StaticFiles(directory=RESOURCES_DIR),
    name="resources"
)

# =================== APP ===================
@app.get("/", response_class=HTMLResponse)
async def main():
    return R.html["main.html"]

# =================== API ===================
@app.post("api/auth/signup", status_code=200)
async def api_signup(user: SignUpUser, response: Response) -> User:
    cursor.execute(SELECT_USER_BY_EMAIL, [user.email])

    if cursor.fetchone():
        response.status_code = status.HTTP_409_CONFLICT
        return {}

    new_user = auth.signup(user)
    response.set_cookie(
        "refresh_token", auth.new_refresh_token(new_user.uid),
        secure=True,
        samesite="strict"
    )

    return new_user
