DROP TABLE IF EXISTS cards;

CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    suit TEXT NOT NULL,
    content TEXT NOT NULL
);