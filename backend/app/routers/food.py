from fastapi import APIRouter


router = APIRouter(prefix="/foods", tags=["Foods"])


@router.get("/")
async def get_foods():
    return "Hello, world!"
