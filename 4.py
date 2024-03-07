weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

additions = input("would you like to wear a hat or a boot")
print("you will be wearing "+clothing+" and "+additions)


if clothing == "sunglasses" :
    accessory = input("would you like to add a sunscreen?")
    if accessory == "yes" :accessory= "sunscreen"
if clothing == "sweater" :
    accessory = input("would you like to add gloves?")
    if accessory == "yes" :accessory= "gloves"