Create Table IF NOT EXISTS Course (
  course_code VARCHAR(5) PRIMARY KEY,
  course_name VARCHAR(200) NOT NULL,
  course_description TEXT,
  teacher_name TEXT,
  course_level INTEGER CHECK(course_level IN (1, 2, 3))
  );