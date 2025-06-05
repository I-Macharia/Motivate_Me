from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from typing import Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Define the data model for user information
class UserData(BaseModel):
    username: str
    civicPassId: Optional[str] = None
    email: str

# Create FastAPI app
app = FastAPI()

# Add CORS middleware to enable cross-origin requests from Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Simple file-based storage for demonstration
USER_DATA_FILE = "user_data.json"

def load_users():
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

@app.post("/api/saveUser")
async def save_user(user_data: UserData):
    users = load_users()
    
    # Create or update user
    users[user_data.username] = {
        "username": user_data.username,
        "civicPassId": user_data.civicPassId,
        "email": user_data.email,
        "user_id": f"user_{len(users) + 1}" if user_data.username not in users else users[user_data.username].get("user_id")
    }
    
    save_users(users)
    
    return {"message": "User saved successfully", "user_id": users[user_data.username]["user_id"]}

@app.get("/api/getUser/{username}")
async def get_user(username: str):
    users = load_users()
    if username in users:
        return users[username]
    raise HTTPException(status_code=404, detail="User not found")

# Add a root endpoint for testing
@app.get("/")
async def root():
    return {"message": "API is running"}

# Add a specific handler for the /login route to prevent 404 errors
@app.get("/login")
async def login_route():
    return {"message": "Login route is working"}

# Add a specific handler for the /profile route to prevent 404 errors
@app.get("/profile")
async def profile_route():
    return {"message": "Profile route is working"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
