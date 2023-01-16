CREATE TABLE Users (
	id_user integer PRIMARY KEY AUTOINCREMENT,
	FullName varchar,
	Login varchar,
	Password varchar,
	Admin boolean
);

CREATE TABLE Offices (
	id_office integer PRIMARY KEY AUTOINCREMENT,
	weekday varchar,
	startlesson time,
	endlesson time,
	officename varchar,
	lessonname varchar
);
CREATE TABLE IF NOT EXISTS mainmenu(
    id integer PRIMARY KEY AUTOINCREMENT ,
    title text NOT NULL,
    url   text NOT NULL
);


