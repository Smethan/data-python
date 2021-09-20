import matplotlib.pyplot as plt
import numpy as np
file = open("CupcakeInvoices.csv")
big_total = 0
st_income = 0
vn_income = 0
ch_income = 0


# Setting plot defaults
plt.rcdefaults()
fig, ax = plt.subplots()

# Looping over file
for line in file:
    
    print(line)
    line = line.strip('\n').split(',')
    print(line[2])
    small_total = round(float(line[3]) * float(line[4]), 2)
    
    # Add income for graphing
    if line[2] == "Chocolate":
        ch_income += small_total
    elif line[2] == "Strawberry":
        st_income += small_total
    elif line[2] == "Vanilla":
        vn_income += small_total
    print(f'invoice total: ${small_total}')
    big_total += small_total

flavors = ('Strawberry', 'Chocolate', 'Vanilla')
y_pos = np.arange(len(flavors))
money = [st_income, ch_income, vn_income]

ax.barh(y_pos, money, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(flavors)
ax.invert_yaxis()
ax.set_xlabel('Income')
ax.set_title('Cupcake income')

print(f'Strawberry income: {st_income}')
print(f'Chocolate income: {ch_income}')
print(f'Vanilla income: {vn_income}')

print(f'Final total: ${round(big_total, 2)}')

plt.show()
