from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import offer, stats

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(offer.router, prefix="/api")
app.include_router(stats.router, prefix="/api") 