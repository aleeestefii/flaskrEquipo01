DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS fashion_article;
DROP TABLE IF EXISTS video_game;
DROP TABLE IF EXISTS star_info;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  selected_site TEXT NOT NULL
);

CREATE TABLE fashion_article (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  url TEXT NOT NULL,
  site_name TEXT,
  section TEXT,
  main_image_url TEXT
);

CREATE TABLE video_game (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  game_name TEXT NOT NULL,
  release_date TEXT,
  reason_url TEXT NOT NULL
);

CREATE TABLE star_info (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  image_url TEXT,
  category TEXT,
  learn_more TEXT
);
