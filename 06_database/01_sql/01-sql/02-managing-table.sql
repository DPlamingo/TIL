CREATE TABLE example (
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('example');

ALTER TABLE 
  example
ADD COLUMN
  Country VARCHAR(100) NOT NULL;

ALTER TABLE
  example
ADD COLUMN
  Age INTEGER NOT NULL;

ALTER TABLE
  example
ADD COLUMN
  Address VARCHAR(100) NOT NULL;

ALTER TABLE
  example
RENAME COLUMN Address TO PostCode;


ALTER TABLE
  example
DROP COLUMN
  PostCode;

ALTER TABLE
  example
RENAME TO
  new_examples;


DROP TABLE
  example;