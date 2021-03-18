-- the task manager is the SQL side of our program, it established what the database looks like and what rows it contains. Only needed if there is not already a pre-established SQL database.
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  duration INT,
  completed BOOLEAN,
  user_id INT REFERENCES users(id)
);
