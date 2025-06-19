CREATE DATABASE IF NOT EXISTS electrical_calculator;
USE electrical_calculator;

CREATE TABLE IF NOT EXISTS calculation_category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    calculation_type VARCHAR(255) NOT NULL,
    voltage DECIMAL(10, 2),
    current DECIMAL(10, 2),
    resistance DECIMAL(10, 2),
    power DECIMAL(10, 2),
    time DECIMAL(10,2),
    result VARCHAR(255),
    input_currents VARCHAR(255),
    output_currents VARCHAR(255),
    value DECIMAL(10, 2),
    from_unit VARCHAR(50),
    to_unit VARCHAR(50),
    calculation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES calculation_category(category_id)
);

CREATE TABLE IF NOT EXISTS saved_calculation (
    saved_id INT AUTO_INCREMENT PRIMARY KEY,
    history_id INT NOT NULL,
    saved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (history_id) REFERENCES history(history_id)
);
