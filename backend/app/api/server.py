from app.api.routes import router as api_router
from app.core import config, tasks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.close_db_connection(app))  # type: ignore

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()
