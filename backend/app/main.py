from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import auth, admin, orchestrator

# FastAPI instance
app = FastAPI(title="AI Workspace Starter", version="0.1.0")

# CORS setup (frontend se connect karne ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: production me specific frontend domain allow karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Workspace Backend is running 🚀"}

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(orchestrator.router, prefix="/orchestrator", tags=["Tools"])
