CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

ALTER TABLE examples
ADD COLUMN
  Country VARCBAR(100) NOT NULL default '';

ALTER TABLE examples
ADD COLUMN
  Address VARCBAR(100) NOT NULL default '';

-- 설계단계에서 쓰고, 중간단계에서는 잘 안씀
-- 기능이 추가/확장 되어 설계가 바뀔때에도 씀 (많이는 안씀)
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;

-- 테이블 필드 삭제 (드롭 오류남,,)
ALTER TABLE examples
DROP COLUMN PostCode;


-- 테이블을 백업? 으로 옮겨놓을 때나 데이터량이 많아서 데이터를 옮겨야 할 경우에 사용
ALTER TABLE
  examples
RENAME TO
  onyu_examples;


-- 테이블 보이게 함
PRAGMA table_info('onyu_examples');