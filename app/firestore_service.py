import firebase_admin
from firebase_admin import credentials, firestore

# from .models import UserData

# project_id = "flask-to-do-310603"
credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(
    credentials,
    # {
    #     "projectId": project_id,
    # },
)

db = firestore.client()


def get_users():
    return db.collection("users").get()
    # return [1, 2, 3, 4]


def get_user(user_id):
    return db.collection("users").document(user_id).get()


def user_put(user_data) -> None:
    user_ref = db.collection("users").document(user_data.username)
    user_ref.set({"password": user_data.password})


def get_todos(user_id: str):  # try:
    return db.collection("users").document(user_id).collection("todos").get()


def put_todo(user_id: str, description: str):
    todos_collection_ref = db.collection("users").document(user_id).collection("todos")
    todos_collection_ref.add({"description": description, "done": False})


def delete_todo(user_id: str, todo_id: str):
    # print("todo_id type:", type(todo_id))
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()
    # todo_red = db.collection("users").document(user_id).collection("todos").document('todo_id')


def update_todo(user_id: str, todo_id: str, done: int):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({"done": not bool(done)})


def _get_todo_ref(user_id: str, todo_id: str):
    return db.document("users/{}/todos/{}".format(user_id, todo_id))