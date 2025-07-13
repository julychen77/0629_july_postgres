DROP TABLE IF EXISTS employee CASCADE ;
DROP TABLE IF EXISTS branch CASCADE ;

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

CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manger_id INT,
 	PRIMARY KEY(branch_id),
 	FOREIGN KEY(manger_id) REFERENCES employee(emp_id) ON DELETE SET NULL  
);

ALTER TABLE employee ADD FOREIGN KEY(branch_id) 
REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee ADD FOREIGN KEY(sup_id) 
REFERENCES employee(emp_id) ON DELETE SET NULL;