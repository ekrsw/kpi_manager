from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from admin import UserAdmin, OperatorAdmin, authentication_backend
from db.database import database


app = FastAPI(
    title="KPI Management System",
    description="KPI管理システム",
    version="0.0.1")

@app.on_event("startup")
async def startup():
    await database.init()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# SQLAdminの初期化
admin = Admin(app=app, engine=database.engine, authentication_backend=authentication_backend, title="KPI Manager Admin")
admin.add_view(UserAdmin)
admin.add_view(OperatorAdmin)

# テスト用のルートエンドポイント
@app.get("/")
async def root():
    return {"message": "KPI Manager API is running"}
