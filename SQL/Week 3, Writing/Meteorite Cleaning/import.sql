.mode csv
.import meteorites.csv "temp"

Update
    "temp"
SET
    "mass" = COALESCE(NULLIF(ROUND("mass",2),""), NULL),
    "year" = COALESCE(NULLIF("year", ""), NULL),
    "lat" = COALESCE(NULLIF(ROUND("lat",2), ""), NULL),
    "long" = COALESCE(NULLIF(ROUND("long",2), ""), NULL);

--> Delete rows with nametype 'Relict'
DELETE FROM
    "temp"
WHERE
    "nametype" = "Relict";

--> Create the 'meteorites' table with new_order column
CREATE TABLE "meteorites" AS
SELECT
	ROW_NUMBER() OVER (
		ORDER BY
			"year",
			"name"
	) AS "id",
	"name",
	"class",
	"mass",
	"discovery",
	"year",
	"lat",
	"long"
FROM
	"temp";

--> Drop the temporary table
DROP TABLE "temp";
