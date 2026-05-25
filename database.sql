DROP TABLE IF EXISTS urls CASCADE;
DROP TABLE IF EXISTS url_checks CASCADE;

CREATE TABLE urls (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name varchar(255) NOT NULL,
  created_at timestamp
);

CREATE TABLE url_checks (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  url_id bigint NOT NULL REFERENCES urls (id),
  status_code integer,
  h1 varchar(255),
  title varchar(255),
  description varchar(255),
  created_at timestamp NOT NULL
);