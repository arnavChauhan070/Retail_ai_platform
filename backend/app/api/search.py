from fastapi import APIRouter

router = APIRouter()

@router.post("/api/search")
def search(query: str):
    return {"message": "Search coming soon", "query": query}