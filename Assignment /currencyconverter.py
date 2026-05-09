 #The Pseudocode
     #Step1 Start
     #Step1Define the function* that accepts a dollar_amount.
     #Step1Check the input:* Ensure the user didn't enter a negative number (since you can't convert negative money).
     #Step1Set the rate:* Define a variable for the exchange rate (1550).
     #Step1Calculate:* Multiply the dollar amount by the exchange rate.
     #Step1Round the result:* Use a rounding function to keep it to 2 decimal places (standard for currency).
     #Step1Return the result.*
     #Step1End
 

def convert_usd_to_ngn(dollar_amount):
                                          # 1. Define the exchange rate
    exchange_rate = 1550
    
                                          # 2. Check for potential issues (like negative numbers)
    if dollar_amount < 0:
        return "Error: Amount cannot be negative."
    
    try:
                                           # 3. Perform the calculation
        naira_amount = dollar_amount * exchange_rate
        
                                            # 4. Handle rounding to 2 decimal places to avoid floating point errors
        final_amount = round(naira_amount, 2)
        
        return final_amount
        
    except Exception as e:
                                           # 5. Handle any other unexpected issues
        return f"An error occurred: {e}"

# --- Testing the function ---

dollars = 50
naira = convert_usd_to_ngn(dollars)

print(f"${dollars} is equal to ₦{naira}")



