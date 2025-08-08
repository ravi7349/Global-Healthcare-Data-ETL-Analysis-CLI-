import pandas as pd

class DataTransformer:
    def clean_and_transform(self, raw_data):
        try:
            df = pd.DataFrame(raw_data)

            if df.empty:
                print("No data fetched from API.")
                return []

            # Rename the 'date' column to match your SQL schema
            df.rename(columns={
                'date': 'collection_week',
                'total_staffed_adult_icu_beds': 'total_beds_7_day_avg',
                'inpatient_beds_used': 'inpatient_beds_used_7_day_avg',
                'staffed_adult_icu_bed_occupancy': 'icu_beds_used_7_day_avg',
                'total_adult_patients_hospitalized_confirmed_covid': 'total_adult_patients_hospitalized_confirmed_covid_7_day_avg',
                'state': 'state',
                'critical_staffing_shortage_today_yes': 'critical_staffing_shortage_today_yes'
            }, inplace=True)

            # Fill dummy values for missing hospital_name
            df['hospital_name'] = "Unknown"

            required_columns = [
                'collection_week',
                'hospital_name',
                'state',
                'total_beds_7_day_avg',
                'inpatient_beds_used_7_day_avg',
                'icu_beds_used_7_day_avg',
                'total_adult_patients_hospitalized_confirmed_covid_7_day_avg',
                'critical_staffing_shortage_today_yes'
            ]

            for col in required_columns:
                if col not in df.columns:
                    df[col] = None

            df = df[required_columns]

            df['collection_week'] = pd.to_datetime(df['collection_week'], errors='coerce')
            df = df.dropna(subset=['collection_week'])

            df['total_beds_7_day_avg'] = pd.to_numeric(df['total_beds_7_day_avg'], errors='coerce').fillna(0)
            df['inpatient_beds_used_7_day_avg'] = pd.to_numeric(df['inpatient_beds_used_7_day_avg'], errors='coerce').fillna(0)
            df['icu_beds_used_7_day_avg'] = pd.to_numeric(df['icu_beds_used_7_day_avg'], errors='coerce').fillna(0)
            df['total_adult_patients_hospitalized_confirmed_covid_7_day_avg'] = pd.to_numeric(
                df['total_adult_patients_hospitalized_confirmed_covid_7_day_avg'], errors='coerce').fillna(0)

            df['critical_staffing_shortage_today_yes'] = df['critical_staffing_shortage_today_yes'].fillna("No")

            print(f" Transformed {len(df)} valid records.")
            return df.to_dict(orient='records')

        except Exception as e:
            print(f"Error in transformation: {e}")
            return []
