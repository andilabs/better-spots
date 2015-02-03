psql << EOF
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'andispot'
  AND pid <> pg_backend_pid();
drop database andispot;
create database andispot;
\connect andispot
-- Enable PostGIS (includes raster)
CREATE EXTENSION postgis;
-- Enable Topology
CREATE EXTENSION postgis_topology;
-- fuzzy matching needed for Tiger
CREATE EXTENSION fuzzystrmatch;
-- Enable US Tiger Geocoder
CREATE EXTENSION postgis_tiger_geocoder;
EOF