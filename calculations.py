import data_analysis
#  original data
data=[3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]

# Run the functions and print results
avg = data_analysis.mean(data)
med = data_analysis.median(data)
std=data_analysis.standard_deviation(data)
print(f"The Mean (Average) is: {avg:.2f}")
print(f"The Median (Middle) is: {med}")
print(f"Standard Deviation: {std:.2f}")
