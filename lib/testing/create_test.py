#!/usr/bin/env python3

import sqlite3

class TestCreate:
    '''Tests for create.sql'''

    def setup_method(self, method):
        '''Setup method executed before each test method.'''
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        with open("lib/create.sql") as sql_file:
            self.sql_as_string = sql_file.read()
        self.cursor.executescript(self.sql_as_string)

    def teardown_method(self, method):
        '''Teardown method executed after each test method.'''
        self.connection.close()

    def test_table_creation(self):
        '''Test if the bears table is created.'''
        tables = [table[0] for table in self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")]
        assert "bears" in tables

    def test_column_existence(self):
        '''Test if all expected columns are created in the bears table.'''
        expected_columns = ["name", "age", "sex", "color", "temperament", "alive"]
        columns = [column[1] for column in self.cursor.execute("PRAGMA table_info(bears);")]
        assert all(column in expected_columns for column in columns)

    def test_primary_key(self):
        '''Test if the bears table has a primary key "id".'''
        columns = [column[1] for column in self.cursor.execute("PRAGMA table_info(bears);")]
        assert columns[0] == "id"
