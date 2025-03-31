CREATE VIEW "frequently_reviewed" AS
    SELECT
        "listings"."id",
        "listings"."property_type",
        "listings"."host_name",
        "reviews"."id" AS "reviews"
    FROM
        "listings"
    JOIN
        "reviews" ON "reviews"."listing_id" = "listings"."id"
    GROUP BY
        "listings"."id",
        "listings"."property_type",
	    "listings"."host_name"
    ORDER BY
        COUNT("reviews"."id") DESC,
        "listings"."property_type" ASC,
        "listings"."host_name" ASC
    LIMIT
        100;



