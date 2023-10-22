-- Check if the database exists and create it if not
SELECT 'CREATE DATABASE todo_app' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'todo_app');

-- Connect to the database
\c todo_app;

-- Create the todo table (if it doesn't exist)
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    task VARCHAR(120) NOT NULL,
    done BOOLEAN
);

-- Check if the user exists and create it if not
DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_user WHERE usename = 'todo_user') THEN
    CREATE USER todo_user WITH ENCRYPTED PASSWORD 'todo_pass';
  END IF;
END $$;

-- Grant necessary privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE todo_app TO todo_user;

-- Grant privileges on the todo table
GRANT ALL PRIVILEGES ON TABLE todo TO todo_user;
