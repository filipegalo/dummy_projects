from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
import redis
import hashlib
import os

app = FastAPI(title="URL Shortener Service")

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

class URLRequest(BaseModel):
    long_url: HttpUrl

class URLResponse(BaseModel):
    short_url: str
    long_url: str

def generate_short_url(url: str) -> str:
    # Generate a hash of the URL
    hash_object = hashlib.md5(url.encode())
    hash_str = hash_object.hexdigest()[:6]
    return hash_str

@app.post("/shorten", response_model=URLResponse)
async def shorten_url(url_request: URLRequest):
    long_url = str(url_request.long_url)
    short_code = generate_short_url(long_url)
    
    # Store in Redis
    redis_client.set(short_code, long_url)
    
    return URLResponse(
        short_url=short_code,
        long_url=long_url
    ) 