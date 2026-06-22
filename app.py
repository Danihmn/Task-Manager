from fastapi import FastAPI

from root import router as root_router

app = FastAPI(title='Task Manager API', version='1.0.0')


app.include_router(root_router)
