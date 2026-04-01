from backend.library_app.repositories.users_repo import UsersRepo
from fastapi import HTTPException

class UsersService:
    def __init__(self, repo: UsersRepo):
        self.repo = repo

    def get_all_users(self):
        return self.repo.get_all()


    def search_by_id(self, user_id:int):
        result = self.repo.get_by_id(user_id)
        if result:
            return result
        raise HTTPException(status_code=404, detail="user not found")

    def search_by_name(self, user_name:str):
        result = self.repo.get_by_name(user_name)
        if result:
            return result
        raise HTTPException(status_code=404, detail="users nor found")


    def search_by_login(self, user_login:str):
        result = self.repo.get_by_login(user_login)
        if result:
            return result
        raise HTTPException(status_code=404, detail="user nor found")

    def create_user(self, user_data):
        if self.repo.login_exist(user_data.login):
            raise HTTPException(status_code=409, detail="that user is already exist")

        return self.repo.create(user_data)

    def update_user(self, user_id: int, user_data):
        if not self.repo.id_exist(user_id):
            raise HTTPException(status_code=404, detail="no right id")
        return self.repo.update(user_id, user_data)

    def delete_user(self, user_id: int):
        if not self.repo.id_exist(user_id):
            raise HTTPException(status_code=404, detail="no right id")
        return self.repo.delete(user_id)


