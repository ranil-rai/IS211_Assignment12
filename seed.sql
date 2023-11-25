
-- Insert a student
INSERT INTO students (first_name, last_name) VALUES ('John', 'Smith');

-- Insert a quiz
INSERT INTO quizzes (subject, question_count, date_given) VALUES ('Python Basics', 5, '2015-02-05');

-- Assuming the INSERT statements above will give us id = 1 for both student and quiz.
-- Insert a result
INSERT INTO results (student_id, quiz_id, score) VALUES (1, 1, 85);
