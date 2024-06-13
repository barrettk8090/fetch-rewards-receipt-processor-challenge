import math

# Award 1 point for each alphaneumeric character in the receipts retailer's name.
def calculate_retailer_points(receipt):
    points = 0
    retailer = receipt.get("retailer")
    for char in retailer:
        if char.isalnum():
            points += 1
    return points

# If the total of the receipt is a round dollar amount with no cents, award 50 points. 
def calculate_round_dollar_amount_points(receipt):
    points = 0
    receipt_total = float(receipt.get("total"))  # Turn string "receipt[total]"" into type float 
    
    if receipt_total % 1 == 0:
        points += 50
    return points

# If the total of the receipt is a multiple of 0.25, award 25 points. 
def calculate_total_multiples_points(receipt):
    points = 0
    receipt_total = float(receipt.get("total"))  # Turn string "receipt[total]"" into type float 

    if receipt_total % 0.25 == 0:
        points += 25
    return points

# For every 2 items on the receipt, award 5 points 
def calculate_two_items_points(receipt):
    points = 0
    receipt_items = receipt.get("items")

    total_items = len(receipt_items)
    num_of_item_pairs = total_items // 2
    points = num_of_item_pairs * 5
    return points

# If an items shortDescription length is a mulitiple of 3, multiply the items price by 0.2 and round up to nearest int. Award that # of points. 
def calculate_trimmed_length_multiples_points(receipt):
    points = 0 
    receipt_items = receipt.get("items")
    
    for item in receipt_items:
        item_trimmed_short_desc = (item.get("shortDescription", "")).strip()
        item_price = float(item.get("price", "0"))
        if len(item_trimmed_short_desc) % 3 == 0 and len(item_trimmed_short_desc) > 0:
            points += math.ceil(item_price*0.2)
    return points

# If a receipts purchaseDate is an odd number, award 6 points.
def calculate_odd_purchase_date_points(receipt):
    points = 0
    receipt_date = receipt.get("purchaseDate")
    day_of_month = float(receipt_date[-2] + receipt_date[-1])

    if day_of_month % 2 == 0: # Check even dates - no points
        return points
    elif day_of_month % 2 != 0: # Check odd dates - 6 points
        points += 6
        return points
    else: # Other extraneous scenarios - no points
        return points  

# If a receipts purchaseTime is between 2:00pm and 3:59pm (14:00 - 15:59), award 10 points.
def calculate_time_of_purchase_points(receipt):
    points = 0
    receipt_time = receipt.get("purchaseTime")

    if receipt_time: 
        # Split purchaseTime into HH:MM (hours, minutes)
        hour, minute = map(int, receipt_time.split(":"))

        if 14 <= hour < 16:
            points += 10
        return points     

# Calculate the total number of points for a receipt
def calculate_total_receipt_points(receipt):
    total_points = 0
    
    total_points += calculate_retailer_points(receipt)
    total_points += calculate_round_dollar_amount_points(receipt)
    total_points += calculate_total_multiples_points(receipt)
    total_points += calculate_two_items_points(receipt)
    total_points += calculate_trimmed_length_multiples_points(receipt)
    total_points += calculate_odd_purchase_date_points(receipt)
    total_points += calculate_time_of_purchase_points(receipt)
    
    return total_points
