import sqlite3

class WebsiteDataCollector:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._setup_database()

    def _setup_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS domains (id INTEGER PRIMARY KEY, category_id INTEGER, domain_name TEXT, FOREIGN KEY(category_id) REFERENCES categories(id))''')
        self.conn.commit()
    def insert_category(self, name):
        self.cursor.execute('''INSERT INTO categories (name) VALUES (?)''', (name,))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def insert_domain(self, category_id, domain_name):
        self.cursor.execute('''INSERT INTO domains (category_id, domain_name) VALUES (?, ?)''', (category_id, domain_name))
        self.conn.commit()
        return self.cursor.lastrowid
 