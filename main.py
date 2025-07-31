from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
    "line1": "This is a new test of the complete pipeline.",
    "line2": "Code pushed to GitHub triggers the build.",
    "line3": "The deployment is running on Amazon EKS.",
    "line4": "Success!"
}