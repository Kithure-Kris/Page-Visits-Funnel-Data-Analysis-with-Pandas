import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how='left')
print(len(visits_cart))

##How many of the timestamps are null for the column cart_time? What do these null rows mean?
null = visits_cart[visits_cart.cart_time.isnull()]
print(len(null))
#1652 null values

##What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print(float(len(null)) / len(visits_cart))
#0.81

##What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = cart.merge(checkout, how='left')
print(len(cart_checkout))
null2 = cart_checkout[cart_checkout.checkout_time.isnull()]
print(len(null2))
print(float(len(null2)) / len(cart_checkout))
#0.21

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')
print(all_data.head())

#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase = checkout.merge(purchase, how = 'left')
print(len(checkout_purchase))
null3 = checkout_purchase[checkout_purchase.purchase_time.isnull()]
print(len(null3))
print(float(len(null3)) / len(checkout_purchase))
#0.17

##Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
#Visit to cart is the weakest at approx. 80%

##Let’s calculate the average time from initial visit to final purchase.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)

##Calculate the average time to purchase
print(all_data.time_to_purchase.mean())

