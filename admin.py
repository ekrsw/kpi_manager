from db.user import User
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import Response

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request)-> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Validate username and password
        # And update session
        request.session.update({"token": "fasdkjf;asldjf;asjdfa;lsdfj"})
        return True
    
    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True
    
    async def authenticate(self, request:Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False
        
        return True

authentication_backend = AdminAuth(secret_key="fasdkjf;asldjf;asjdfa;lsdfj")
    

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.created_at, User.updated_at]

    def is_valible(self, request: Request) -> bool:
        return True
    
    def is_accessible(self, request: Request) -> bool:
        return True
