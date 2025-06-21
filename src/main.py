import os
import sys
from fastapi import FastAPI
from src.presentation.controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router)
