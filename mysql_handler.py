import mysql.connector
import logging

class MySQLHandler:
    def __init__(self, config):
        self.conn = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, table_name, data_list):
        if not data_list:
            logging.info("No data to insert.")
            return

        insert_sql = f"""
        INSERT INTO {table_name} (
            collection_week,
            hospital_name,
            state,
            total_beds_avg,
            inpatient_beds_used_avg,
            icu_beds_used_avg,
            covid_patients_avg,
            staffing_shortage
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = [
            (
                record.get('collection_week'),
                record.get('hospital_name'),
                record.get('state'),
                record.get('total_beds_7_day_avg'),
                record.get('inpatient_beds_used_7_day_avg'),
                record.get('icu_beds_used_7_day_avg'),
                record.get('total_adult_patients_hospitalized_confirmed_covid_7_day_avg'),
                record.get('critical_staffing_shortage_today_yes')
            )
            for record in data_list
        ]

        self.cursor.executemany(insert_sql, values)
        self.conn.commit()
        logging.info(f"Inserted {self.cursor.rowcount} records into {table_name}.")

    def list_tables(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor.fetchall()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS hospital_covid_stats;")
        self.conn.commit()
    
    def run_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    

    def close(self):
        self.cursor.close()
        self.conn.close()
