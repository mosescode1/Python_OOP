# there are many packages devlopers have created and you can access it from pypi.org
# A prettyTable in adcci
from prettytable import PrettyTable

table = PrettyTable()
table.add_column('pokeman', ['pikachu', 'Squirtle', 'charmander'])
table.add_column('type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table.align)
print(table)