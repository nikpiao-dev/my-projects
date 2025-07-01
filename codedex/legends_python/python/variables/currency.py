"""
Instructions
We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates for pesos, soles, and reais!



The output should look something like this, but with slightly different results:

What do you have left in pesos? 5600
What do you have left in soles? 105
What do you have left in reais? 280
413.0

The sequence should be:

Currency code example

Cha-ching! Now you have the total in USD. 💰

"""

# Current exchange rates (as of today):
pesos_to_usd = 4000  # 1 USD = 4000 COP
soles_to_usd = 3.75  # 1 USD = 3.75 PEN
reais_to_usd = 5.2  # 1 USD = 5.2 BRL

# Input amounts in each currency
amount_pesos = int(input("What do you have left in pesos (COP)? "))  # e.g., 5600
amount_soles = int(input("What do you have left in soles (PEN)? "))  # e.g., 105
amount_reais = int(input("What do you have left in reais (BRL)? "))  # e.g., 280

# Convert amounts to USD, rounding to the nearest integer
usd_from_pesos = amount_pesos / pesos_to_usd  # pesos to USD
usd_from_soles = int(amount_soles / soles_to_usd)  # Convert soles to USD
usd_from_reais = int(amount_reais / reais_to_usd)  # Convert reais to USD

# Calculate total in USD
total_usd = usd_from_pesos + usd_from_soles + usd_from_reais

# Out
print(total_usd)
