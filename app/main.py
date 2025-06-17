from fastapi import FastAPI
import logging

# app/main.py

from fastapi import FastAPI
import logging

# Configure a basic logger for now. We'll set up a proper one later.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI application instance
app = FastAPI(
    title="User and Media Management API",
    description="A containerized CRUD application with user management and media services.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the User and Media Management API!"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Used to verify if the API is running.
    """
    logger.info("Health check endpoint accessed.")
    return {"status": "ok", "message": "API is healthy"}

# We will add more endpoints and include routers here later