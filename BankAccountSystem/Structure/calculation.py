# Get Rates online
import pandas as pd
import html5lib

# Interest Rate
def getIntRates():
    # From TD bank
    data = pd.read_html("https://www.td.com/ca/en/personal-banking/products/bank-accounts/account-rates/") 
    
    # all saving amount with same i
    i = float(data[0]['Interest Rate'][0].split('%')[0])/100 
    
    return i

# Exchange Rate
def getEXRates():
    # From canadian web
    data = pd.read_html("https://www.x-rates.com/table/?from=CAD&amount=1") 
    extable = data[1].set_index('Canadian Dollar')
    
    # CAD -> TWD
    EXT = extable.loc['Taiwan New Dollar'][0]
    
    return EXT


# Interest Calculation: simple interest
def interest(balance):
    i = getIntRates()
    r = balance * i
    return r

# while withdraw money, deduct CAD 3 for service fee
def service(x):
    x = x + 3
    return x