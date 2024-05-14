-- Selects the name and age of all female bears
select_all_female_bears_return_name_and_age = """
    SELECT name, age FROM bears WHERE sex = 'female';
"""

-- Selects the names of all bears and orders them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM bears ORDER BY name ASC;
"""

-- Selects the names and ages of bears that are alive and orders them from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

-- Selects the name and age of the oldest bear
select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

-- Selects the name and age of the youngest bear
select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;
"""
