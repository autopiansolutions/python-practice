# This here is the description and price of the Lovely Loveseat sold at a furniture store.

lovely_lovessat_description = " Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "
lovely_loveseat_price = 254.00

# The inventory has been expanded to include a new piece of furniture - the Stylish Settee.

stylish_settee_description = " Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "
stylish_settee_price = 180.50

# A new piece of furniture has been added - the Luxurious Lamp.

luxurious_lamp_description = " Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "
luxurious_lamp_price = 52.15

# Sales tax on the items is 8.8%

sales_tax = 0.088

# The purchase of the first customer

customer_one_total = 254.00 + 52.15
customer_one_itemization = " Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "
customer_one_tax = customer_one_total * sales_tax
customer_one_total = lovely_loveseat_price + luxurious_lamp_price + customer_one_tax

# The receipt for the first customer's purchase

print ( " Customer One Items: ")
print ( customer_one_itemization )

print ( " Customer One Total: " )
print ( customer_one_total )




