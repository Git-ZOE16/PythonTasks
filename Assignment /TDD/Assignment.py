
## Task 1: Email Validation

def validate_email(email):
    # Check if the total length is at least 8 characters
    if len(email) < 8:
        return False
    
    # Check if '@' is in the string
    if "@" not in email:
        return False
    
    # Check if it starts or ends with '@'
    if email.startswith("@") or email.endswith("@"):
        return False
    
    # If all checks pass, it is valid
    return True



## Task 2: Calculate Balance

def calculate_balance(transactions):
    # Start the balance at 0
    balance = 0
    
    # Loop through every number in the list
    for amount in transactions:
        # Add the amount (positive adds, negative subtracts)
        balance = balance + amount
        
    return balance



## Task 3: Strong Password Check

def is_strong_password(password):
    # Check if the length is 8 or more
    if len(password) >= 8:
        return True
    else:
        return False



## Task 4: Apply Interest

def apply_interest(balance, rate, years):
    # Check for invalid rate or years
    if rate < 0 or years < 1:
        raise ValueError("Rate cannot be negative and years must be at least 1")
    
    # Calculate interest: balance * (1 + rate) ^ years
    final_balance = balance * ((1 + rate) ** years)
    
    # Return the result rounded to 2 decimal places
    return round(final_balance, 2)



## Task 5: Transaction Summary

def get_transaction_summary(transactions):
    credits = 0
    debits = 0
    count = len(transactions)
    
    for item in transactions:
        # item[0] is the label ("credit" or "debit"), item[1] is the amount
        label = item[0]
        amount = item[1]
        
        if label == "credit":
            credits += amount
        elif label == "debit":
            debits += amount
            
    # Calculate net balance
    net_balance = credits - debits
    
    # Create the list of lists for the output
    summary = [
        ["total_credits", credits],
        ["total_debits", debits],
        ["net_balance", net_balance],
        ["transaction_count", count]
    ]
    
    return summary



