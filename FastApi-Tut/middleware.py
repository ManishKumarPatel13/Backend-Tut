""" You can add middleware to FastAPI applications.

A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

It takes each request that comes to your application.
It can then do something to that request or run any needed code.
Then it passes the request to be processed by the rest of the application (by some path operation).
It then takes the response generated by the application (by some path operation).
It can do something to that response or run any needed code.
Then it returns the response. """

import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http") # Middleware for all routes
async def add_process_time_header(request: Request, call_next): # Middleware function
    start_time = time.perf_counter() # Start time
    response = await call_next(request) # Call the next middleware or the path operation if there is no middleware left to call.
    process_time = time.perf_counter() - start_time # Process time
    response.headers["X-Process-Time"] = str(process_time) # Add a custom header with the process time for the request. 
    return response # Return the response with the added header.