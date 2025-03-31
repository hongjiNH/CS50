SELECT
    "city",
    COUNT("types") type
FROM
    "schools"
WHERE
    "type" = "Public School"
GROUP BY
    "city"
ORDER BY
    "type" DESC,
    "city" ASC
LIMIT
    10;
