CREATE TABLE IF NOT EXISTS "ingredients"(
    "id" SERIAL PRIMARY KEY,
    "ingredient" TEXT,
    "price_per_unit" INTEGER
);

CREATE TABLE IF NOT EXISTS "donuts"(
    "id" SERIAL PRIMARY KEY,
    "name" TEXT,
    "price_per_donuts" INTEGER,
    "glueten_free" INTEGER,
    "ingredient_id" INTEGER,
    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients" ("id")
);

CREATE TABLE IF NOT EXISTS "orders"(
    "id" SERIAL PRIMARY KEY,
    "donut_id" INTEGER,
    "customer_id" INTEGER,
    FOREIGN KEY ("donut_id") REFERENCES "donuts" ("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id")
);

CREATE TABLE IF NOT EXISTS "customers"(
    "id" SERIAL PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT
);

CREATE TABLE IF NOT EXISTS "customer_order_history"(
    "customer_id" INTEGER,
    "order_id" INTEGER,
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id"),
	FOREIGN KEY ("order_id")    REFERENCES "orders" ("id")

);
