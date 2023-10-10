-- 01. Querying data
SELECT LastName
From employees;

SELECT
  LastName,
  FirstName
FROM
  employees;

SELECT
  Name, 
  Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks;

SELECT
  FirstName AS '이름'
FROM
  employees;
-- 02. Sorting data

SELECT  
  FirstName
FROM
  employees
ORDER BY -- 기본 대상에 대한 내림차순
  FirstName;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC; -- 오름차순

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC, City;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

SELECT
  
-- NULL 정렬 예시


-- 03. Filtering data


-- 04. Grouping data


-- 에러


-- 에러 해결
