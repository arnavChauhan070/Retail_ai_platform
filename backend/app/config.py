import os
from dotenv import load_dotenv


# config.py reads .env file and provides all settings


# Load .env file
load_dotenv()

class Settings:
    # Project Info
    PROJECT_NAME: str = "Retail AI Platform"
    VERSION: str      = "1.0.0"
    AUTHOR: str       = "Arnav Chauhan - Left Shift 2026"

    # MongoDB Settings
    MONGODB_URL: str        = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DB_NAME: str    = os.getenv("MONGODB_DB_NAME", "retail_ai_db")

    # MongoDB Collections
    SALES_COLLECTION: str   = "live_sales"
    LOGS_COLLECTION: str    = "conversation_logs"

    # Azure OpenAI Settings
    AZURE_OPENAI_KEY: str        = os.getenv("AZURE_OPENAI_KEY", "")
    AZURE_OPENAI_ENDPOINT: str   = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT: str = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    AZURE_OPENAI_VERSION: str    = os.getenv("AZURE_OPENAI_VERSION", "2024-02-01")

    # Model Paths
    DEMAND_MODEL_PATH: str  = "ml_engine/models/demand_model.pkl"
    ANOMALY_MODEL_PATH: str = "ml_engine/models/anomaly_model.pkl"

    # Data Paths
    RAW_DATA_PATH: str      = "data/raw/"
    STAGED_DATA_PATH: str   = "data/staged/sales_staged.parquet"
    CURATED_DATA_PATH: str  = "data/curated/sales_analytics.parquet"
    ANOMALY_DATA_PATH: str  = "data/curated/anomalies.parquet"

    # FAISS Vector Store Path
    FAISS_INDEX_PATH: str   = "backend/agents/faiss_index"

    # PDF Knowledge Base Path
    KNOWLEDGE_BASE_PATH: str = "docs/knowledge_base/"

# Single instance used across all files
settings = Settings()