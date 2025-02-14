# CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript code that 
# communicates with a backend, and the backend is in a different "origin" than the frontend.

# Origin¶
# An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS Middleware is a piece of software that's added to the backend to relax the security restrictions.
origins = [ # List of origins that should be allowed to make requests to the backend. use '*' to allow all origins.
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
] # List of origins that should be allowed to make requests to the backend. 


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # List of HTTP methods that should be allowed for CORS.
    allow_headers=["*"], # List of HTTP headers that should be allowed for CORS.
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)