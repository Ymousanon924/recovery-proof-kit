-- Run only against the isolated restore target.
SELECT current_database() AS database_name;
SELECT current_timestamp AS checked_at;
SELECT COUNT(*) AS table_count
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');

-- Replace this with an application-specific check, for example:
-- SELECT COUNT(*) FROM public.users;

