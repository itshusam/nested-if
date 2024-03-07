attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#2
if venue == "large hall" :
    facilities = input("would you like to add audio system or projector?")
print ("we will add the " + facilities + " for you")

#3
food = input("would you like vegetarian food?")
if food == "yes" :
    print ("vegetarian food will be served")
else : print ("what about Gourmet Meals Caterers?")