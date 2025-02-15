from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import redis
import os

app = FastAPI(title="URL Redirect Service")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis connection
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0
)

@app.get("/{short_code}")
async def redirect_url(short_code: str):
    long_url = redis_client.get(short_code)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=long_url.decode()) 