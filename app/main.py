from fastapi import FastAPI

app = FastAPI()

# Root endpoint (Only for debugging purposes)
@app.get('/')
def root():
    return {"message": "OK"}

