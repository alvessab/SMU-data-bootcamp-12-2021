drop table if exists departments cascade;
drop table if exists dept_emp cascade;
drop table if exists dept_manager cascade;
drop table if exists employees cascade;
drop table if exists salaries cascade;
drop table if exists titles cascade;


CREATE TABLE "departments" (
    "ID" SERIAL   NOT NULL,
    "dept_no" VARCHAR(10)   NOT NULL,
    "dept_name" VARCHAR(30)   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "ID"
     ),
    CONSTRAINT "uc_departments_dept_no" UNIQUE (
        "dept_no"
    )
);

SELECT *
FROM DEPARTMENTS;

CREATE TABLE "dept_emp" (
    "ID" SERIAL   NOT NULL,
    "emp_no" INT   NOT NULL,
    "dept_no" VARCHAR(10)   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "ID"
     )
);

SELECT *
FROM DEPT_EMP;

CREATE TABLE "dept_manager" (
    "ID" SERIAL   NOT NULL,
    "dept_no" VARCHAR(10)   NOT NULL,
    "emp_no" INT   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "ID"
     )
);

SELECT *
FROM DEPT_MANAGER;

CREATE TABLE "employees" (
    "ID" SERIAL   NOT NULL,
    "emp_no" INT  NOT NULL,
    "emp_title_id" VARCHAR(15)   NOT NULL,
    "birth_date" DATE   NOT NULL,
    "first_name" VARCHAR(30)   NOT NULL,
    "last_name" VARCHAR(30)   NOT NULL,
    "sex" VARCHAR(5)   NOT NULL,
    "hire_date" DATE   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "ID"
     ),
    CONSTRAINT "uc_employees_emp_no" UNIQUE (
        "emp_no"
    )
);

SELECT *
FROM employees;

CREATE TABLE "salaries" (
    "ID" SERIAL   NOT NULL,
    "emp_no" INT   NOT NULL,
    "salary" INT   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "ID"
     )
);

SELECT *
FROM salaries;

CREATE TABLE "titles" (
    "ID" SERIAL   NOT NULL,
    "title_id" VARCHAR(30) Unique  NOT NULL,
    "title" VARCHAR(50)   NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "ID"
     )
);

SELECT *
FROM titles;

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "titles" ("title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");