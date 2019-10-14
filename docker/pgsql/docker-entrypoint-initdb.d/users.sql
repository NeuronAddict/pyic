-- noinspection SqlNoDataSourceInspectionForFile

CREATE TABLE "users"(
    username text,
    "pass" text
);

INSERT INTO "users"(username, "pass") VALUES('admin', 'secret');
