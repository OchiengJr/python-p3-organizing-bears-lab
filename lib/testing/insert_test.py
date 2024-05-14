#!/usr/bin/env python3

import sqlite3

class TestInsert:
    '''Tests for insert.sql'''

    def setup_method(self, method):
        '''Setup method executed before each test method.'''
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        # Execute create.sql
        with open("lib/create.sql") as create_file:
            create_as_string = create_file.read()
        self.cursor.executescript(create_as_string)

        # Execute insert.sql
        with open("lib/insert.sql") as insert_file:
            insert_as_string = insert_file.read()
        self.cursor.executescript(insert_as_string)

    def teardown_method(self, method):
        '''Teardown method executed after each test method.'''
        self.connection.close()

    def test_inserts_eight_bears_into_table(self):
        '''Test if 8 bears are inserted into the bears table.'''
        result = self.cursor.execute("SELECT COUNT(*) FROM bears;")
        assert result.fetchone()[0] == 8, "Incorrect number of bears inserted"

    def test_has_unnamed_bear(self):
        '''Test if there is one unnamed bear in the bears table.'''
        result = self.cursor.execute("SELECT COUNT(*) FROM bears WHERE name IS NULL;")
        assert result.fetchone()[0] == 1, "No unnamed bear found"
