import numpy as np

# Defining general categories and keywords for categorize common transactions

category_keywords = {
    'DINING OUT': ['BAR', 'RESTAURANT', 'CAFE', 'TIM HORTONS', 'STARBUCKS', 'EUREST CSA', 'MCDONALDS', 'CHIPOTLE', 'LOCAL LIBERTY'],
    'GROCERIES': ['NOFRILLS', 'NO FRILLS', 'JORDANS NF','LONGOS','WALMART', 'COSTCO', 'LOBLAWS', 'METRO', 'GROCERY', 'FOODLAND', 'FRESHCO'],
    'GAS': ['SHELL', 'PETRO', 'ESSO', 'GAS'],
    'SUBSCRIPTIONS': ['NETFLIX', 'PRIME MEMBER', 'PROTON', 'PRIME', 'PRIMEVIDEO', 'PATREON', 'APPLECOM', 'AUDIBLE'],
    'UBER RIDES' : ['UBER TRIP', 'UBERTRIP'],
    'PUBLIC TRANSIT' : ['PRESTO'],
    'UBER EATS' : ['UBER EATS', 'UBEREATS'],
    'ALCOHOL' : ['LCBO', 'WINE RACK'],
    'AMAZON' : ['AMAZON', 'AMZN'],
    'SHOPPERS/REXALL' : ['SHOPPERS DRUG', 'REXALL']
}

# Categorization function
# This takes a transaction description as an input and checks if it contains any of the keywords for a category.
# It will categorize the transaction based on the first keyword found and label it as 'Other' if no match is found.
def categorize(transaction_description):
    for category, keywords in category_keywords.items():
        if any(key in transaction_description for key in keywords):
            return category
    return 'Other'
