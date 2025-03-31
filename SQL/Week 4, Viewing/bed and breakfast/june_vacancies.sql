CREATE VIEW "june_vacancies" AS
    SELECT
        "listings"."id",
        "listings"."property_type",
        "listings"."host_name",
        COUNT("availabilities"."date") AS "days_vacant"
    FROM
        "listings"
    JOIN
        "availabilities" ON "availabilities"."listing_id" = "listings"."id"
    WHERE
        "availabilities"."available" = "TRUE"
        AND
        "availabilities"."date" >= "2023-06-01"
        AND
        "availabilities"."date" <"2023-07-01"
    GROUP BY
        "listings"."id",
        "listings"."property_type",
        "listings"."host_name";



