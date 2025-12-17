#
#  Import LIBRARIES
import flet as ft
import flet.fastapi
from fastapi import FastAPI

#  Import FILES
from app.api import register_routes
from app.ui import build_ui

#  ______________________


def main(page: ft.Page) -> None:
    build_ui(page=page)


app = FastAPI()
register_routes(app=app)
flet_app = flet.fastapi.app(main=main, before_main=None)
app.mount(path="/", app=flet_app)

# @app.get(path="/")
# def main() -> dict[str, str]:
#     return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    # for development, set reload=True
    # uvicorn.run(app=app, host="0.0.0.0", port=8550)
    uvicorn.run(app="main:app", host="0.0.0.0", port=8550, reload=True)


#
#  Import LIBRARIES
#  Import FILES
#  ______________________
