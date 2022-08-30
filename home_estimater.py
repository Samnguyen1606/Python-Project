def estimate_home_value(size_in_sqft, number_of_bedrooms):
    #Assume all home are worth at least $50000
    value = 50000
    #Adjust value of the house based on the size of the house
    value = value + (size_in_sqft*92)
    #Adjust value of the house based on the number of bedrooms
    value = value + (number_of_bedrooms*10000)
    return value
# Estimate the value of our house
# 5 bedrooms
# 3800 sq ft
# Actual value: $450000

value = estimate_home_value(3800,5)
print ("estimeted_value")
print(value)