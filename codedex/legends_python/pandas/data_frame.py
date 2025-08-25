
"""
Instructions
First thing first, import pandas at the top of the file.

Then, create a DataFrame named contacts containing information about your friends, family, or fictional characters. Your DataFrame should have at least 3 columns and 4 rows.

Feel free to be creative about what columns to include. If you need inspiration, you could consider columns like name, age, phone_number, astrological_sign. 💫

For example:

name	age	phone_number	astrological_sign
Bart	10	939-555-0113	Taurus
Lisa	8	939-555-0114	Virgo
Homer	39	939-555-0115	Taurus
Marge	36	939-555-0116	Pisces
Create the DataFrame using either the dictionary method or the list-of-lists method.

Don't forget to display the table after creating it!


"""
import pandas as pd 

data = {
  'name': ['Bart', 'Lisa', 'Homer', 'Marge'],
  'age': [10, 8, 39, 36],
  'phone_number': ['', '', '', ''],
  'astrological_sign': ['', '', '', '']
}

contacts = pd.DataFrame(data)

print(contacts)
