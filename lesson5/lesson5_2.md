##確認資料庫若有EMPLOYEE資料表則刪除，並先建立一個EMPLOYEE資料表

```sql
DROP TABLE IF EXISTS employee;

CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);
```
## 

