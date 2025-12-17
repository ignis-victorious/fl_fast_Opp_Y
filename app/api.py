#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from app.models import AddRequest

#  ______________________


def register_routes(app: FastAPI) -> None:
    @app.get(path="/api/health")
    def health() -> dict[str, str]:  # type: ignore
        return {"status": "ok"}

    # curl -X POST http://localhost:8550/api/add -H "Content-Type: application/json" -d '{"a": 66, "b": 3}'
    @app.post(path="/api/add")
    def add(request: AddRequest) -> dict[str, int]:  # type: ignore
        result: int = request.a + request.b
        return {"result": result}
