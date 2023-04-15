DROP TABLE supply;
DROP TABLE sale;
DROP TABLE auth_group;
DROP TABLE auth_group_permissions;
DROP TABLE auth_permissions;
DROP TABLE auth_user;
DROP TABLE auth_user_groups;
DROP TABLE auth_user_user_permissions;
DROP TABLE django_admin_log;
DROP TABLE django_content_type;
DROP TABLE django_migrations;
DROP TABLE django_session;
DROP TABLE my_cache_table;

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

DELETE FROM supply;
DELETE FROM sale;