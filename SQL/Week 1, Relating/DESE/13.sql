SELECT
    "name" AS "name of the school",
    "expenditures"."pupils"
FROM
    "schools"
JOIN
    "expenditures"
ON
    "expenditures"."district_id" = "schools"."district_id";
