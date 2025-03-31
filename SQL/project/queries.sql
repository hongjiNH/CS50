--Add new client
INSERT INTO
    "Clients" ("name","email","phone","company","notes")
VALUES
    ("Jeff","jeff@gmail.com","6567221818","WX designing","NIL");

--Update client info
UPDATE "Clients"
SET
    "email" = "Wxdesigning@gmail.com"
WHERE
    "name" = "Jeff";

--Search client by name
SELECT
    *
FROM
    "clients"
WHERE
    "name" = "Jeff";

--Create new project for client
INSERT INTO
    "Projects" ("client_id","title", "description", "start_date" "deadline", "status")
VALUES
    ((SELECT "client_id"FROM"clients"WHERE"name" = "Jeff"),"Website design", "design the company website for better UX.", "2025-04-01", "2025-05-15","Pending");

--Update project
UPDATE "Projects"
SET
    "description" = "Website Redesign"
WHERE
    "client_id" =(
        SELECT
            *
        FROM
            "clients"
        WHERE
            "name" = "Jeff"
        );

--List all project for a specific client
SELECT
    *
FROM
    "Projects"
WHERE
    "client_id" =(
        SELECT
            *
        FROM
            "clients"
        WHERE
            "name" = "Jeff"
        );

--Delete Project
DELETE FROM
    "Projects"
WHERE
    "client_id" =(
        SELECT
            *
        FROM
            "clients"
        WHERE
            "name" = "Jeff"
        );

-- Generate invoice link to project
SELECT
    *
FROM
    "Invoices"
WHERE
    "project_id" =(
        SELECT
            *
        FROM
            "Projects"
        WHERE
            "project_id" = 1
        );

-- Filter status
SELECT
    *
FROM
    "Invoices"
WHERE
    "paid_status" = "Unpaid";

-- List of overdue invoices
SELECT
    *
FROM
    "Invoices"
WHERE
    "paid_status" = "Overdue";

-- Generate completed project per client
SELECT * FROM "Completed_Projects_Report";
