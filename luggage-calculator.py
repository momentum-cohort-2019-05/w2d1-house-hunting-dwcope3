#description
#ask the user for the weight of bag of luggage
#   - if the user has no more bag, stop
#   - otherwise, ask again
# add up the weight of all bags
# if > weight limit (100 lbs), warn the user

done = False
total_weight = 0
weight_limit = 100

while not done:
    bag_weight_as_str = input("How much does your bag weigh in  pounds? (Hit Enter if you are done)" )
    if bag_weight_as_str == "":
        done = True
    else:
        bag_weight = int(bag_weight_as_str)
        total_weight = total_weight + bag_weight 
        print("Your total weight so far is " + str(total_weight) + ".")

    # ^ same code as total_weight += bag_weight

if total_weight > weight_limit:
    print("Warning! You are over the weight limit by " + str(total_weight - weight_limit) + " pounds.")