from fastapi import FastAPI
import logging
#instead of using print statements using a logger , reason idk cz they do it this way dont know why 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="User Media App coded via FastAPI and Docker containerized and all",
    description="Features include user management + i,ahe upload capability , a bit of AI",
    version="1",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    logger.info("Root endpoint called")
    return {"message": "User Media App coded via FastAPI and Docker containerized and all"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Used to verify if the API is running.
    """
    logger.info("Health check endpoint called.")
    return {"status": "ok", "message": "API is happy and healthy"}

# will add more crud parts to it later on 