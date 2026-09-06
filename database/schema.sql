-- Referential tables
CREATE TABLE IF NOT EXISTS heroes (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
	id BIGINT PRIMARY KEY,
	name TEXT NOT NULL,
	tier SMALLINT,
	cost BIGINT,
	slot_type TEXT
);

-- Match data
CREATE TABLE IF NOT EXISTS matches (
	match_id BIGINT PRIMARY KEY,
	start_time TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS match_picks (
	match_id BIGINT REFERENCES matches(match_id),
	hero_id SMALLINT REFERENCES heroes(id),
	won BOOLEAN NOT NULL,
	PRIMARY KEY (match_id, hero_id)
);

CREATE TABLE IF NOT EXISTS match_items (
	match_id BIGINT,
	hero_id SMALLINT,
	item_id BIGINT REFERENCES items(id),
	UNIQUE (match_id, hero_id, item_id),
	FOREIGN KEY (match_id, hero_id) REFERENCES match_picks(match_id, hero_id)
);