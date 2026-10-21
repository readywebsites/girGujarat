-- ==============================================================================
-- POSTGRESQL PRODUCTION SETUP SCRIPT FOR TRAVEL FIRST HOLIDAYS (girGujarat)
-- Target Server: Ubuntu 24.04 LTS (PostgreSQL 16)
-- Database: girgujarat_db
-- User: girgujarat_user
-- ==============================================================================
-- SAFETY GUARANTEES:
-- 1. NEVER drops or resets existing databases, roles, or data.
-- 2. Checks if the user and database already exist before creating.
-- 3. Grants least-privilege access restricted to girgujarat_db and public schema.
-- ==============================================================================

-- Step 1: Safely create user if it doesn't already exist
DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'girgujarat_user') THEN
      CREATE ROLE girgujarat_user WITH LOGIN PASSWORD 'REPLACE_WITH_STRONG_PASSWORD';
      RAISE NOTICE 'Role girgujarat_user created successfully.';
   ELSE
      RAISE NOTICE 'Role girgujarat_user already exists, skipping creation.';
   END IF;
END
$do$;

-- Step 2: Configure standard Django database role optimizations
ALTER ROLE girgujarat_user SET client_encoding TO 'utf8';
ALTER ROLE girgujarat_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE girgujarat_user SET timezone TO 'Asia/Kolkata';

-- Step 3: Safely create database if it doesn't already exist
-- (Run this block in psql; \gexec conditionally executes the statement)
SELECT 'CREATE DATABASE girgujarat_db OWNER girgujarat_user'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'girgujarat_db')\gexec

-- Step 4: Grant database privileges
GRANT ALL PRIVILEGES ON DATABASE girgujarat_db TO girgujarat_user;

-- Step 5: Connect to the database and grant public schema permissions
\c girgujarat_db

GRANT ALL ON SCHEMA public TO girgujarat_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO girgujarat_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO girgujarat_user;
