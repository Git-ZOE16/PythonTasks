#Pseudocode

#Step1 Customer's total spending
#step2 Tiered Dicounts
#Step3 enter total purchase amount 
#Step4 if purshase is 1,000 to 10,000
#Step5 print 5% discount
#Step6 elif purchase is 10,000 and 50,000
#Step7 print 10% discount
#Step8 elif purchase is 50,000
#Step9 print 20% discount
#Step10 if print no discount

#CODE

customer_spending = float(input("Enter total purchase amount: "))
if customer_spending < 1000:
   print("no discount")
elif    customer_spending <= 10000:
   discount = customer_spending * 0.05
   print("Discount: ", discount)
elif customer_spending <= 50000:
   discount = customer_spending * 0.10
   print("Discount: ", discount)   
elif customer_spending > 50000:
   discount = customer_spending * 0.20

    


