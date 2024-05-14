#!/usr/bin/env python3

import sqlite3
import sql_queries  # Assuming this file contains the SQL queries

class TestQueries:
    '''Tests for SQL queries'''

    def setup_method(self, method):
        '''Setup method executed before each test method.'''
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        with open("lib/create.sql") as create_file:
            create_as_string = create_file.read()
        self.cursor.executescript(create_as_string)

        with open("lib/seed.sql") as insert_file:
            insert_as_string = insert_file.read()
        self.cursor.executescript(insert_as_string)

    def teardown_method(self, method):
        '''Teardown method executed after each test method.'''
        self.connection.close()

class TestSelectAllFemaleBearsReturnNameAndAge(TestQueries):
    '''Tests for select_all_female_bears_return_name_and_age'''

    def test_selects_females_and_returns_name_and_age(self):
        '''Test if females are selected and their names and ages are returned.'''
        result = self.cursor.execute(sql_queries.select_all_female_bears_return_name_and_age)
        assert result.fetchall() == [("Tabitha", 6), ("Melissa", 13), ("Wendy", 6)], "Incorrect female bears data"

class TestSelectAllBearsNamesAndOrdersInAlphabeticalOrder(TestQueries):
    '''Tests for select_all_bears_names_and_orders_in_alphabetical_order'''

    def test_selects_all_bears_names_and_orders_alphabetically(self):
        '''Test if all bears names are selected and ordered alphabetically.'''
        result = self.cursor.execute(sql_queries.select_all_bears_names_and_orders_in_alphabetical_order)
        expected_result = [
            (None,),
            ("Grinch",),
            ("Melissa",),
            ("Mr. Chocolate",),
            ("Rowdy",),
            ("Sergeant Brown",),
            ("Tabitha",),
            ("Wendy",)
        ]
        assert result.fetchall() == expected_result, "Incorrect alphabetical ordering of bear names"

# Similarly, implement other test classes for each query

if __name__ == "__main__":
    # Run the tests if the script is executed directly
    import pytest
    pytest.main()
