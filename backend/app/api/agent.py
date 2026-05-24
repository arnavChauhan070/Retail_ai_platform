from fastapi import APIRouter

router = APIRouter()

@router.post("/api/agent")
def agent(query: str):
    return {"message": "Agent coming soon", "query": query}