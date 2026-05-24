from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from backend.app.config import settings
from backend.app.database import retail_db

# Arnav Chauhan - Left Shift 2026 - Smart Retail Platform

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Step 1: Connect MongoDB on startup, disconnect on shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    retail_db.connect()
    yield
    retail_db.disconnect()

# Step 2: Create FastAPI app
app = FastAPI(
    title="Retail AI Platform",
    version="1.0.0",
    lifespan=lifespan
)

# Step 3: Allow anyone to call our API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Step 4: Register all 4 routes
from backend.app.api.ingest  import router as ingest_router
from backend.app.api.predict import router as predict_router
from backend.app.api.search  import router as search_router
from backend.app.api.agent   import router as agent_router

app.include_router(ingest_router)
app.include_router(predict_router)
app.include_router(search_router)
app.include_router(agent_router)

# Step 5: Health check
@app.get("/")
def home():
    return {
        "status"  : "running",
        "platform": "Retail AI Platform",
        "author"  : "Arnav Chauhan - Left Shift 2026",
        "routes"  : [
            "POST /api/ingest",
            "POST /api/predict",
            "POST /api/search",
            "POST /api/agent"
        ]
    }