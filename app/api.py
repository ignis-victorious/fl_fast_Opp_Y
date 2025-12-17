#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES


#  ______________________


def register_routes(app: FastAPI) -> None:
    @app.get(path="/api/health")
    def health() -> dict[str, str]:  # type: ignore
        return {"status": "ok"}
