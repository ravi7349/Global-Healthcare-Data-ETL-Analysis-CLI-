import requests

url = "https://healthdata.gov/resource/g62h-syeh.json?$limit=20"
data = requests.get(url).json()

print("Total Records Fetched:", len(data))
print("Sample Record:")
print(data[0])
