import argparse
import configparser
from api_client import APIClient
from data_transformer import DataTransformer
from mysql_handler import MySQLHandler

def main():
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    db_config = config['mysql']
    api_config = config['api']

    # Initialize components
    api = APIClient(api_config['base_url'])
    transformer = DataTransformer()
    db = MySQLHandler(db_config)

    # Setup CLI
    parser = argparse.ArgumentParser(description="Hospital COVID Data ETL CLI")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('fetch_data')
    subparsers.add_parser('list_tables')
    subparsers.add_parser('drop_tables')

    # Add new CLI command for query_data
    query_parser = subparsers.add_parser('query_data')
    query_parser.add_argument('query_type', help='Type of query to run (e.g., total_cases)')

    args = parser.parse_args()

    if args.command == 'fetch_data':
        print("Fetching hospital data from API...")
        raw = api.fetch_data(limit=1000)
        transformed = transformer.clean_and_transform(raw)
        db.insert_data("hospital_covid_stats", transformed)
        print("ETL process completed.")

    elif args.command == 'list_tables':
        tables = db.list_tables()
        print("Tables:", [t[0] for t in tables])

    elif args.command == 'drop_tables':
        db.drop_tables()
        print("All tables dropped.")

    elif args.command == 'query_data':
        if args.query_type == 'total_cases':
            print("Running query for total hospital metrics...\n")
            result = db.run_query("""
                SELECT
                    SUM(total_beds_avg),
                    SUM(inpatient_beds_used_avg),
                    SUM(icu_beds_used_avg),
                    SUM(covid_patients_avg)
                FROM hospital_covid_stats;
            """)
            for row in result:
                print(f" Total Beds: {row[0]}")
                print(f" Inpatients: {row[1]}")
                print(f" ICU Beds Used: {row[2]}")
                print(f" COVID Patients: {row[3]}")
        else:
            print("Unknown query type. Try: total_cases")

    else:
        parser.print_help()

    db.close()

if __name__ == "__main__":
    main()
