CREATE TABLE IF NOT EXISTS hospital_covid_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collection_week DATE,
    hospital_name VARCHAR(255),
    state VARCHAR(50),
    total_beds_avg FLOAT,
    inpatient_beds_used_avg FLOAT,
    icu_beds_used_avg FLOAT,
    covid_patients_avg FLOAT,
    staffing_shortage VARCHAR(10),
    etl_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
