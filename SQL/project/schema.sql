CREATE TABLE IF NOT EXISTS "Clients"(
    "client_id" INT AUTO_INCREMENT PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) UNIQUE NOT NULL,
    "phone" VARCHAR(20),
    "company" VARCHAR(255) NOT NULL,
    "notes" TEXT
);

CREATE TABLE IF NOT EXISTS "Projects"(
    "project_id" INT AUTO_INCREMENT PRIMARY KEY,
    "client_id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "start_date" DATE NOT NULL,
    "deadline"  DATE NOT NULL,
    "company" VARCHAR(255) NOT NULL,
    "description" TEXT
    "status" VARCHAR(50) CHECK ("status" IN ('Pending', 'In Progress', 'Completed', 'On Hold')),
    FOREIGN KEY ("client_id") REFERENCES "Clients"("client_id")
);

CREATE TABLE IF NOT EXISTS "Invoices" (
    "invoice_id" INT AUTO_INCREMENT PRIMARY KEY,
    "project_id" INT NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "due_date" DATE NOT NULL,
    "paid_status" VARCHAR(50) CHECK ("paid_status" IN ('Unpaid', 'Paid', 'Overdue')),
    FOREIGN KEY ("project_id") REFERENCES "Projects"("project_id")
);
-- view for
CREATE VIEW "Completed_Projects_Report" AS
SELECT
    "Clients"."client_id",
    "Clients"."name" AS "client_name",
    "Projects"."project_id",
    "Projects"."title" AS "project_title",
    "Projects"."start_date",
    "Projects"."deadline"
FROM
    "Projects"
JOIN
    "Clients" ON "Projects"."client_id" = "Clients"."client_id"
WHERE
    "Projects"."status" = "Completed"
ORDER BY
    "Clients"."client_id",
    "Projects"."deadline";

-- index for searching name or email or company
CREATE INDEX
    "idx_clients_search" ON "Clients" ("name", "email", "company");

-- index for searching invoices by paid_status
CREATE INDEX
    "idx_invoices_paid_status" ON "Invoices" ("paid_status");


