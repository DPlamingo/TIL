CREATE TABLE example (
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('example')

ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;
