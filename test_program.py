import json
import os

# Step 1: Write request file
request_data = {
    "total_budget": 2000,
    "categories": {
        "Rent": 50,
        "Food": 30,
        "Gym": 10
    }
}

with open("request.json", "w") as f:
    json.dump(request_data, f, indent=4)

print("Request written to request.json")

# Step 2: Tells the  user to run microservice
print("Now run budget_microservice.py to process the request.")

# Step 3: Checks for response
if os.path.exists("response.json"):
    with open("response.json", "r") as f:
        response = json.load(f)
        print("Response received:")
        print(json.dumps(response, indent=4))
else:
    print("No response found yet.")