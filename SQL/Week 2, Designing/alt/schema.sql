CREATE TABLE IF NOT EXISTS "passengers"(
    "id" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" INTEGER
);

CREATE TABLE IF NOT EXISTS "check-ins"(
    "date" TEXT,
    "flight_id" INTEGER,
    "passengers_id" INTEGER,
    FOREIGN KEY ("flight_id") REFERENCES "flights"("id"),
    FOREIGN KEY ("passengers_id") REFERENCES "passengers"("id")
);

CREATE TABLE IF NOT EXISTS "airlines"(
    "id" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "name" TEXT,
    "section" TEXT
);

CREATE TABLE IF NOT EXISTS "flights"(
    "id" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "flight_number" INTEGER,
    "operated" TEXT,
    "departing_code" TEXT,
    "destinating_code" TEXT,
    "departure_datetime" TEXT,
    "arrival_datetime" TEXT,
    "airline_id" INTEGER,
    FOREIGN KEY ("airline_id") REFERENCES "airlines"("id")
);
