import requests

response = requests.get('https://v6.exchangerate-api.com/v6/218fe26c10b9e704e29f8989/latest/USD')

In1 = input("Enter starting amount: ")
InSource = input("Enter the currency to convert from(i.e USD, JPY, EUR): ")
InTarget = input("Enter the currency to convert to(i.e USD,JPY,EUR): ")
In1 = float(In1)

InSource = InSource.upper()
InTarget = InTarget.upper()

def convert():
   amount1 = response.json()['conversion_rates'][InSource]
   amount2 = response.json()['conversion_rates'][InTarget]
   return (amount1 * In1) * (amount2)
        
print("The amount is", convert(), InTarget)
    


    

