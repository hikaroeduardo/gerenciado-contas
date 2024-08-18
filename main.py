from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from app.core.database import engine
from fastapi.exceptions import RequestValidationError

from app.routes.user_router import user_routes

app = FastAPI()

app.include_router(user_routes)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: RequestValidationError):
    details = exception.errors()

    for error in details:
        if error.get("type") == "missing":
            return JSONResponse(
                content={ "Message_error": "Todos os dados são necessários." },
                status_code=status.HTTP_400_BAD_REQUEST
            )
        else:
            return JSONResponse(
                content={ "Message_error": "Dados inválidos, verificar tipos de dados." },
                status_code=status.HTTP_400_BAD_REQUEST
            )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=3333, reload=True)