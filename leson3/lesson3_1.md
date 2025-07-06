## 建立資料表的語法```中間夾語法 ```結束


```sql
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```

##建立一個student的資料表

```sql
CREATE TABLE IF NOT EXISTS student(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE
);
```

##刪除一個student的資料表drop atble

```sql
DROP TABLE IF EXISTS student;
```

##新增1筆資料基本語法

```sql
INSERT INTO student (name, major)
VALUES ('呂育均', '歷史');
```
##table_name：目標資料表名稱

##column1, column2, ...：要插入資料的欄位名稱

##value1, value2, ...：對應欄位的值，數量與順序需一致

##新增多筆資料基本語法

```sql
INSERT INTO student (name, major)
VALUES ('小柱', '生物'),('信忠', '英語');

```
##取得資料基本語法
```sql
SELECT 
  select_list 
FROM 
  table_name 
WHERE 
  condition 
ORDER BY 
  sort_expression;
```  
```sql
SELECT student_id, name,major  
FROM student;

SELECT * 
FROM student
ORDER BY student_id ASC;

SELECT * 
FROM student
ORDER BY student_id DESC;


INSERT INTO student (name, major)
VALUES ('呂育均', '歷史');

INSERT INTO student (name, major)
VALUES ('小柱', '生物'),('信忠', '英語');

INSERT INTO student (name, major)
VALUES ('呂育君', '歷史');

SELECT student_id, name,major  
FROM student;

SELECT * 
FROM student
where name='信忠';

SELECT * 
FROM student
ORDER BY student_id ASC;

SELECT * 
FROM student
ORDER BY student_id DESC;

SELECT * 
FROM student
ORDER BY student_id desc
limit 3;
``` 