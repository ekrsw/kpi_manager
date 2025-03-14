from db.user import User
from db.operator import Operator
from db.group import Group
from db.KPI import KPI
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
    name_plural = "User"
    column_list = "__all__"
    column_searchable_list = [User.username]

    def is_valible(self, request: Request) -> bool:
        return True
    
    def is_accessible(self, request: Request) -> bool:
        return True

class OperatorAdmin(ModelView, model=Operator):
    name_plural = "Operator"
    column_list = "__all__"
    column_searchable_list = [Operator.name]
    column_sortable_list = [Operator.group_id, Operator.is_sv, Operator.is_active]
    form_columns = ["name", "ctstage_name", "sweet_name", "group_id", "is_sv", "is_active"]
    form_include_pk = True

    def is_valible(self, request: Request) -> bool:
        return True
    
    def is_accessible(self, request: Request) -> bool:
        return True
    
class GroupAdmin(ModelView, model=Group):
    name_plural = "グループ"
    column_list = [Group.id, Group.group_name]
    column_searchable_list = [Group.group_name]
    column_sortable_list = [Group.id]

    def is_valible(self, request: Request) -> bool:
        return True
    
    def is_accessible(self, request: Request) -> bool:
        return True

class KPIAdmin(ModelView, model=KPI):
    name_plural = "KPI"
    column_list = [KPI.created_at, KPI.total_calls]
    column_searchable_list = [KPI.created_at]
    column_sortable_list = [KPI.created_at]

    def is_valible(self, request: Request) -> bool:
        return True
    
    def is_accessible(self, request: Request) -> bool:
        return True
