CREATE TABLE comments(
    id serial PRIMARY KEY,
    name text NOT NULL,
    text text NOT NULL
);

INSERT INTO comments(name, text) VALUES('admin', 'Hi!'),('guest', 'Nice site!'),('other', 'anybody here?');
