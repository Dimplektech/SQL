create table if not exists Marks(
  student_id INTEGER,
  course_code CHAR(5),
  marks Integer,
  FOREIGN key (student_id) REFERENCES Student(student_id),
  FOREIGN key (course_code) REFERENCES Course(course_code)
  );