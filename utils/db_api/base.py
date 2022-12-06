import sqlite3


class Database:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False) -> object:
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREAT TABLE myfiles_teacher (
        id int NOT NULL,
        Name varchar(255) NOT NULL, 
        email varchar(255),
        language varchar(3)
        PRIMARY KEY (id) 
        );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO myfiles_teacher(id, Name, email, language) VALUES (?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM mufiles_teacher WHERE"
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_user(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_teacher;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_teacher SET email = ? WHERE id = ?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE", commit=True)

    def add_users(self, name: str, telegram_id: int, surname: str = None, username: str = None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
           INSERT INTO users(name, telegram_id, surname, username) VALUES (?, ?, ?, ?)
           """
        self.execute(sql, parameters=(name, telegram_id, surname, username), commit=True)

    def select_all_user(self):
        sql = """
           SELECT * FROM users
           """
        return self.execute(sql, fetchall=True)

    def add_line(self, name: str, tg_id: int, sections: str = None, banks: str = None, username: str = None,
                 line: int = None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO line(name, tg_id, username, line, sections, banks) VALUES (?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(name, tg_id, username, line, sections, banks), commit=True)

    def add_registration(self, id: int, tg_id: int, name: str, surname: str, region: str, school: str,
                         phone_number: int, date: str):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO myfiles_registration(id, tg_id, name, surname, school, region,phone_number, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, tg_id, name, surname, school, region, phone_number, date), commit=True)

    def count_registration(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_registration;", fetchone=True)

    def select_all_question(self):
        sql = """
        SELECT * FROM myfiles_question
        """
        return self.execute(sql, fetchall=True)

    def select_all_question_ru(self):
        sql = """
        SELECT * FROM myfiles_question_ru
        """
        return self.execute(sql, fetchall=True)

    def select_question(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_question WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_question_ru(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_question_ru WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def add_result(self, tg_id: int, name: str, username: str, quiz: int, time: str, answer_id: int = None,
                   answer: str = None, result: str = None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO myfiles_result(tg_id, name, username,quiz,answer_id,answer,result,time ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(tg_id, name, username, quiz, answer_id, answer, result, time), commit=True)

    def add_result_ru(self, tg_id: int, name: str, username: str, quiz: int, time: str, answer_id: int = None,
                   answer: str = None, result: str = None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, name, email) VALUES (1, 'John', 'John@gmail.com')"

        sql = """
             INSERT INTO myfiles_result_ru(tg_id, name, username,quiz,answer_id,answer,result,time ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
         """
        self.execute(sql, parameters=(tg_id, name, username, quiz, answer_id, answer, result, time), commit=True)

    def select_quiz(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_question WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_quiz_ru(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_question_ru WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_question(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_question;", fetchone=True)

    def count_question_ru(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_question_ru;", fetchone=True)

    def update_registration(self, test, tg_id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_registration SET test = ? WHERE tg_id = ?
        """
        return self.execute(sql, parameters=(test, tg_id), commit=True)

    def select_answers(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT result FROM myfiles_result WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_answers_ru(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT result FROM myfiles_result_ru WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_player(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_registration WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_regions(self):
        sql = """
        SELECT * FROM myfiles_region
        """
        return self.execute(sql, fetchall=True)

    def select_all_regions_ru(self):
        sql = """
           SELECT * FROM myfiles_region_ru
           """
        return self.execute(sql, fetchall=True)

    def select_worker(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_worker WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_region(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_region WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_region_ru(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT * FROM myfiles_region_ru WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_workers(self):
        sql = """
        SELECT * FROM myfiles_worker
        """
        return self.execute(sql, fetchall=True)

    def check_user(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT  COUNT(*) FROM myfiles_registration WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def check_user_quiz(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT  COUNT(*) FROM myfiles_result WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def check_user_quiz_ru(self, **kwargs):
        # SQL EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'
        sql = "SELECT  COUNT(*) FROM myfiles_result_ru WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def update_registration_pre(self, presentation, tg_id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
              UPDATE myfiles_registration SET presentation = ? WHERE tg_id = ?
              """
        return self.execute(sql, parameters=(presentation, tg_id), commit=True)

def logger(statement):
    print(f"""
    ______________________________________
    Executing:
    {statement}

    ______________________________________
    """)
