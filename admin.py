from db.user import User
from sqladmin import ModelView

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.created_at, User.updated_at]