from fastapi import FastAPI, Header

app = FastAPI()


@app.post("/")
def say_hi():
    return {"message": "Hello World with post"}


# POST http://localhost:8000/post/api/v1/authenticate/token
# Authorization=Token your_token_here
@app.post("/post/api/v1/authenticate/token")
def get_token(authorization: str = Header(None)):
    print(f"Authorization header: {authorization}")
    if authorization != "xyz":
        return {"message": "Invalid token"}
    return {
        "expire": "2025-08-09 11:15:12+07:00",
        "token": "your token here",
    }
