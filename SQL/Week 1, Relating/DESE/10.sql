SELECT
    "name" As "names of the districts",
    "expenditures"."per_pupil_expenditure" AS "per-pupil expenditures"
FROM
    "districts"
JOIN
    "expenditures"
ON
    "districts"."id" = "expenditures"."district_id"
WHERE
    "type" = "Public School District"
ORDER BY
    "per-pupil expenditures" DESC
LIMIT
    10;
