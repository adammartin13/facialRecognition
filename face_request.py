import requests
import json

# This code doesn't work, need to adjust the request string
api_key = "jQKW91WJG8YuxJETOFn51w"
r = requests.get('https://api.generated.photos/api/v1/faces?api_key='+api_key+'&faces?per_page=1')
output = json.loads(r.json())
print(output)
print(r)
