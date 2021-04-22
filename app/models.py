from flask_login import UserMixin
from .firestore_service import get_user


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data: UserData) -> None:
        """
        :param user_data: UserData
        """
        if user_data == None:
            self.id = None
            self.password = None

        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id: str) -> UserMixin:

        if user_id == None or not isinstance(user_id, str):
            return UserModel(None)

        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()["password"],
        )

        return UserModel(user_data)
