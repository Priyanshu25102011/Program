import pandas as pd
import matplotlib.pyplot as plt

data_records = [
    {'month_number': 1, 'facecream': 2500, 'facewash': 1500, 'toothpaste': 5200, 'bathingsoap': 9200, 'shampoo': 1200, 'moisturizer': 1500, 'total_units': 21100, 'total_profit': 211000},
    {'month_number': 2, 'facecream': 2630, 'facewash': 1200, 'toothpaste': 5100, 'bathingsoap': 6100, 'shampoo': 2100, 'moisturizer': 1200, 'total_units': 18330, 'total_profit': 183300},
    {'month_number': 3, 'facecream': 2140, 'facewash': 1340, 'toothpaste': 4550, 'bathingsoap': 9550, 'shampoo': 3550, 'moisturizer': 1340, 'total_units': 22470, 'total_profit': 224700},
    {'month_number': 4, 'facecream': 3400, 'facewash': 1130, 'toothpaste': 5870, 'bathingsoap': 8870, 'shampoo': 1870, 'moisturizer': 1130, 'total_units': 22270, 'total_profit': 222700},
    {'month_number': 5, 'facecream': 3600, 'facewash': 1740, 'toothpaste': 4560, 'bathingsoap': 7760, 'shampoo': 1560, 'moisturizer': 1740, 'total_units': 20960, 'total_profit': 209600},
    {'month_number': 6, 'facecream': 2760, 'facewash': 1555, 'toothpaste': 4890, 'bathingsoap': 7490, 'shampoo': 1890, 'moisturizer': 1555, 'total_units': 20140, 'total_profit': 201400},
    {'month_number': 7, 'facecream': 2980, 'facewash': 1120, 'toothpaste': 4780, 'bathingsoap': 8980, 'shampoo': 1780, 'moisturizer': 1120, 'total_units': 29550, 'total_profit': 295500},
    {'month_number': 8, 'facecream': 3700, 'facewash': 1400, 'toothpaste': 5860, 'bathingsoap': 9960, 'shampoo': 2860, 'moisturizer': 1400, 'total_units': 36140, 'total_profit': 361400},
    {'month_number': 9, 'facecream': 3540, 'facewash': 1780, 'toothpaste': 6100, 'bathingsoap': 8100, 'shampoo': 2100, 'moisturizer': 1780, 'total_units': 23400, 'total_profit': 234000},
    {'month_number': 10, 'facecream': 1990, 'facewash': 1890, 'toothpaste': 8300, 'bathingsoap': 10300, 'shampoo': 2300, 'moisturizer': 1890, 'total_units': 26670, 'total_profit': 266700},
    {'month_number': 11, 'facecream': 2340, 'facewash': 2100, 'toothpaste': 7300, 'bathingsoap': 13300, 'shampoo': 2400, 'moisturizer': 2100, 'total_units': 41280, 'total_profit': 412800},
    {'month_number': 12, 'facecream': 2900, 'facewash': 1760, 'toothpaste': 7400, 'bathingsoap': 14400, 'shampoo': 1800, 'moisturizer': 1760, 'total_units': 30020, 'total_profit': 300200}
]

# Convert the list of dicts to a DataFrame
df = pd.DataFrame(data_records)

# ----------------------------------------------------
# 1. Monthly Company Profit Comparison (Line Plot)
# ----------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(
    df['month_number'],
    df['total_profit'],
    label='Company Profit Data',
    linestyle='dotted', # Customized line style
    marker='o',         # Added circle marker
    color='r',          # Line color red
    linewidth=3,        # Line width should be 3
    markerfacecolor='k' # Marker color as black
)
plt.title('1. Monthly Company Profit Comparison')
plt.xlabel('Month Number')
plt.ylabel('Total Profit ($\\times 1000$)')
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('monthly_profit_comparison.png')
plt.show()

# ----------------------------------------------------
# 2. Monthly Sales Data for All Products (Multi-Line Plot)
# ----------------------------------------------------
product_columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

plt.figure(figsize=(12, 7))
for column in product_columns:
    plt.plot(
        df['month_number'],
        df[column],
        marker='o',     # Added circle marker
        linewidth=3,    # Line width equal to 3
        label=column.replace('_', ' ').title() + ' Sales' # Added legend
    )

plt.title('2. Monthly Sales Data for All Products')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(df['month_number'])
plt.savefig('monthly_product_sales_comparison.png')
plt.show()

# ----------------------------------------------------
# 3. Monthly Sales Comparison: Face Cream vs. Face Wash (Bar Plot)
# ----------------------------------------------------
bar_width = 0.35
x = df['month_number']

fig, ax = plt.subplots(figsize=(12, 7))

r1 = x - bar_width/2
r2 = x + bar_width/2

ax.bar(r1, df['facecream'], color='skyblue', width=bar_width, edgecolor='grey', label='Face Cream Sales')
ax.bar(r2, df['facewash'], color='salmon', width=bar_width, edgecolor='grey', label='Face Wash Sales')

ax.set_title('3. Monthly Sales Comparison: Face Cream vs. Face Wash')
ax.set_xlabel('Month Number')
ax.set_ylabel('Sales Units')
ax.set_xticks(x)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.savefig('face_cream_face_wash_bar_plot.png')
plt.show()