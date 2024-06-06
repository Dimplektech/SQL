-- Create Student Table
CREATE TABLE IF NOT EXISTS Student(
  student_id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email VARCHAR(200) NOT NULL UNIQUE,
  date_of_birth DATE,
  course_code VARCHAR(5),
  FOREIGN KEY (course_code) REFERENCES Course(course_code));