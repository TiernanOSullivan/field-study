# Water temperature readings (celcius)

measurements =[16.0, 18.0, 19.0, 13.0]

def calculate_mean(values):
"""Return the arithmetic mean of a non-empty sequence of numbers"""
	return sum(values)/len(values)
print(f"Mean water temperature: {caluclate_mean(measurements)} C")
