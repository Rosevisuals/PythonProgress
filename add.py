
temperature = 30.5  
unit = "C"  

if unit == "C":
    
    converted_temperature = (temperature * 9/5) + 32
    converted_unit = "F"
    original_unit = "C"
else:

    converted_temperature = (temperature - 32) * 5/9
    converted_unit = "C"
    original_unit = "F"


print(f"{temperature} degrees {original_unit} is equal to {converted_temperature} degrees {converted_unit}")

