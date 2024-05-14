-- Create a table to store country information
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY,
    country_code VARCHAR(2) UNIQUE NOT NULL,
    country_name VARCHAR(100) NOT NULL,
    population INTEGER,
    continent VARCHAR(50),
    language VARCHAR(50)
);
