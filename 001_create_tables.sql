-- 001_create_tables.sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT,
  reset_token TEXT,
  reset_expires BIGINT,
  created_at BIGINT NOT NULL
);

CREATE TABLE IF NOT EXISTS listings (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
  title TEXT NOT NULL,
  description TEXT,
  price NUMERIC DEFAULT 0,
  currency TEXT DEFAULT 'CAD',
  category TEXT,
  location TEXT,
  images JSONB,
  created_at BIGINT NOT NULL
);
