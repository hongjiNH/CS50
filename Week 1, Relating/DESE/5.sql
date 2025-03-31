SELECT
    "city",
    COUNT("name") AS "number of Public School"
FROM
    "schools"
WHERE
    "type" = "Public School"
GROUP BY
    "city"
HAVING
    "number of Public School" <=3
ORDER BY
    "number of Public School" DESC,
    "ciyt" ASC;
