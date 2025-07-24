from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import router

app = FastAPI()

# 💡 Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # 👈 Your React/Next.js URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Include your routers
app.include_router(router)
