import psycopg2 as pg
import datetime as dt


def create_db():
    with pg.connect(database='netology', user='netology', password='netology', host='localhost',
                    port=5432) as conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE student, course, student_course;')
        cur.execute('''CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        gpa NUMERIC(10, 2),
        birth TIMESTAMP WITH TIME ZONE
        );''')

        cur.execute('''CREATE TABLE IF NOT EXISTS course (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
            );''')

        cur.execute('''CREATE TABLE IF NOT EXISTS student_course (
            student_id INT REFERENCES student(id),
            course_id INT REFERENCES course(id),
            CONSTRAINT student_course_pk PRIMARY KEY(student_id, course_id)
            );''')


def get_students(course_id):
    with pg.connect(database='netology', user='netology', password='netology', host='localhost',
                    port=5432) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM student_course WHERE course_id = %s;', (course_id,))
        return cur.fetchall


def add_students(course_id, students):
    with pg.connect(database='netology', user='netology', password='netology', host='localhost',
                    port=5432) as conn:
        cur = conn.cursor()
        for student in students:
            cur.execute('''INSERT INTO student_course(student_id, course_id) VALUES(%s,%s);''',
                        (student['id'], course_id))

            cur.execute('SELECT * from student_course')
            print(cur.fetchall)


def add_student(student):
    with pg.connect(database='netology', user='netology', password='netology', host='localhost',
                    port=5432) as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO student(name, gpa, birth) VALUES(%s, %s, %s);',
                    (student['name'], student['gpa'], student['birth']))
        cur.execute('SELECT * from student')
        print(cur.fetchall)


def get_student(student_id):
    with pg.connect(database='netology', user='netology', password='netology', host='localhost',
                    port=5432) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM student WHERE id = %s;', (student_id,))
        return cur.fetchall()



create_db()
student = {
    'name': 'Gleb',
    'gpa': 3,
    'birth': dt.datetime(1998, 8, 14)
}
add_student(student)
print(get_student(1))
print(get_students(0))

