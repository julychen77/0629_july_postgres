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
