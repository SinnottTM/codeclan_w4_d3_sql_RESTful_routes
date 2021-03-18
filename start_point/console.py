# console is where we add or remove data to the program via functions set up in the repo's. Establishes initial data etc. in the app. Only needed if a pre-established off site database does not exist.
import pdb
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

# delete tasks first as all tasks need a user key. If we delete users first, tasks will crash as it now lacks a value
task_repository.delete_all()
user_repository.delete_all()

# generate new users and save them to the data-base
user1 = User("Jack", "Jarvis")
user_repository.save(user1)

user2 = User("Victor", "McDade")
user_repository.save(user2)

# select all the users present in the data-base at the moment
user_repository.select_all()

# generate and save tasks. Note this needs users in order to be generated
task_1 = Task("Plant seeds", user1, 30)
task_repository.save(task_1)

task_2 = Task("Go for a run", user1, 30, True)
task_repository.save(task_2)

pdb.set_trace()
