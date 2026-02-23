import json
def process_budget(data):
    total_budget = data["total_budget"]
    categories = data["categories"]

    total_pct = sum(categories.values())
    breakdown = {}

    for name, pct in categories.items():
        amount = round(total_budget * pct / 100, 2)
        breakdown[name] = {
            "percentage": pct,
            "amount": amount
        }

    response = {
        "total_percentage": total_pct,
        "breakdown": breakdown
    }

    if total_pct < 100:
        remaining_pct = 100 - total_pct
        remaining_amt = round(total_budget * remaining_pct / 100, 2)
        response["unassigned"] = {
            "percentage": remaining_pct,
            "amount": remaining_amt
        }
        response["status"] = "incomplete"

    elif total_pct == 100:
        response["status"] = "valid"

    else:
        response["status"] = "invalid"

    return response


if __name__ == "__main__":
    with open("request.json", "r") as f:
        request_data = json.load(f)

    result = process_budget(request_data)

    with open("response.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Response written to response.json")