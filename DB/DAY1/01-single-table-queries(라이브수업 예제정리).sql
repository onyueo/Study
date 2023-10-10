-- 주석(--)
-- 문법위에 오른쪽마우스 해서 run selected query 하면 run됨 
-- run 에러 -> 거의 ; 안붙인것


-- 01. Querying data
-- SELECT : 테이블의 데이터를 조회 및 반환

-- SELECT 활용 1 : 테이블 employees 에서 LastName필드의 모든 데이터를 조회
SELECT
  LastName
FROM
  employees;

-- SELECT 활용 2 : 테이블 employees 에서 LastName, FirstName 필드의 모든 데이터를 조회
SELECT
  LastName, FirstName
FROM
  employees;

-- SELECT 활용 3 : 테이블 employees 에서 모든 데이터 필드 조회
SELECT
  *
FROM
  employees;

-- SELECT 활용 4 : 테이블 employees 에서 FirstName 필드의 모든 데이터 필드 조회
-- (단, 조회 시 FirstName이 아닌 '이름'으로 출력될 수 있도록 변경)
SELECT
  FirstName AS '이름'
FROM
  employees;

-- SELECT 활용 5 : 테이블 tracks 에서 Name, Milliseconds 필드의 모든 데이터 필드 조회
-- (단, 조회 시 Milliseconds 필드는 60000으로 나눠 분단위 값으로 출력

SELECT
  Name, 
  Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks;





-- 02. Sorting data
-- ORDER BY : 조회 결과의 레코드를 정렬

-- ORDER BY 활용 1 : 테이블 employees에서 FirstName 필드의 모든 데이터를 오름차순으로 조회
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

-- ORDER BY 활용 2 : 테이블 employees에서 FirstName 필드의 모든 데이터를 내림차순으로 조회
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

-- ORDER BY 활용 3 : 테이블 customers에서 Contry 필드를 기준으로 내림차순으로 정렬한 다음 City필드 기준으로 오름차순 정렬하여 조회
SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;
  
-- ORDER BY 활용 4 : 테이블 tracks에서 Milleseconds 필드를 기준으로 내림차순 정렬한 다음 Name, Milliseconds 필드의 모든 데이터를 조회
-- (단, Milliseconds 필드는 60000으로 나눠 분 단위로 출력)
SELECT
  Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;



-- NULL 정렬 예시
-- NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;




-- 03. Filtering data
-- DISTINCT : 조회결과에서 중복된 레코드를 제거 / SELECT키워드 바로 뒤에 작성해야 함 / 고유한 값을 선택하려는 하나 이상의 필드를 지정

-- DISTINCT 활용 1 : 테이블 customers에서 Country 필드의 모든 데이터를 오름차순 조회
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;



-- WHERE : 조회 시 특정 검색조건을 지정 / FROM 아래에 위치 / serch_condition은 비교연산자 및 논리연산자를 사용하는 구문이 사용됨

-- WHERE 활용 1 : 테이블 customers에서 City 필드 값이 'Prague'인 데이터의 LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';


-- WHERE 활용 2 : 테이블 customers에서 City 필드 값이 'Prague'가 아닌 데이터의 LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

-- WHERE 활용 3 : 테이블 customers에서 Company필드 값이 NULL이고 Contry필드 값이 USA인 데이터의 LastName, FirstName, Company, Contry 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company is NULL   -- Company = NULL 은 안됨!
  AND Country = 'USA';

-- WHERE 활용 4 : 테이블 customers에서 Company필드 값이 NULL이거나 Contry필드 값이 USA인 데이터의 LastName, FirstName, Company, Contry 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company is NULL   -- Company = NULL 은 안됨!
  OR Country = 'USA';

-- WHERE 활용 5 : 테이블 tracks에서 Bytes필드 값이 100000이상 500000이하인 데이터의 Name, Bytes조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;  --  10000 <= Bytes <= 500000 는 동작X

-- WHERE 활용 6 : 테이블 tracks에서 Bytes필드 값이 100000이상 500000이하인 데이터의 Name, Bytes을 Bytes기준으로 오름차순 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

-- WHERE 활용 7 : 테이블 customers에서 Contry 필드 값이 'Canada' 또는 'Germany' 또는 'France'인 데이터의 LastName, FistsName, Contry 조회
SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');

-- WHERE 활용 8 : 테이블 customers에서 Contry 필드 값이 'Canada' 또는 'Germany' 또는 'France' 가 아닌 데이터의 LastName, FistsName, Contry 조회
SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

-- WHERE 활용 9 : 테이블 Customers에서 LastName필드 값이 son으로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

-- WHERE 활용 10 : 테이블 Customers에서 LastName필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';


-- LIMIT : 하나 또는 두개의 인자를 사용 ( 0또는 양의 정수) / row_count는 조회하는 최대 레코드 수를 지정

-- LIMIT 활용 1 : 테이블 track에서 Trackld, Name, Bytes 필드 데이터를 Bytes기준 내림차순으로 7개만 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

-- LIMIT 활용 1 : 테이블 track에서 Trackld, Name, Bytes 필드 데이터를 Bytes기준 4번째 부터 7번째 데이터만 내림차순으로 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;




-- 04. Grouping data
-- GROUP BY : 레코드를 그룹화하여 요약본 생성 (집계함수 와 함께 사용) / From 및 Where 절 뒤에 배치 / Group by 절 뒤에 그룹화 할 필드 목록 작성

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;
 
-- GROUP BY 활용 1 : 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
SELECT
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

-- GROUP BY 활용 2 : 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10미만인 데이터 조회
-- (단, Milliseconds 필드는 60000으로 나눠 분 단위 평균으로 계산)

-- 에러 ( group by 와 where을 같이 쓸 때 나타남)
SELECT
  Composer, AVG(Milliseconds / 60000) as avg
FROM
  tracks
WHERE
  AVG < 10
GROUP BY
  Composer;


-- 에러 해결
SELECT
  Composer, AVG(Milliseconds / 60000) as avg
FROM
  tracks
GROUP BY
  Composer
HAVING
 avg < 10;