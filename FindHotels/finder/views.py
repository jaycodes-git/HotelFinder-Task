from django.shortcuts import render, HttpResponse
from .models import Hotel

# Create your views here.


def Average(lst):
    return sum(lst) / len(lst)


def findhotels(request):
    output = ""
    if request.method == "POST":
        state = request.POST["state"]
        searchby = request.POST["searchby"]
        operation = request.POST["operation"]

        costs = []
        ratings = []
        state_hotels = Hotel.objects.filter(State=state)
            
    
        if not state == "State":                          
            if searchby == "Cost":
                for hotel in state_hotels:
                    cost = hotel.Cost
                    costs.append(cost)
                lowest = min(costs)
                highest = max(costs)
                average = Average(costs)
                average = round(average, )
                if operation == "Highest" or operation == "Lowest":
                    if operation == "Highest":
                        data = highest
                    elif operation == "Lowest":
                        data = lowest

                    hotelfound = Hotel.objects.all().filter(State=state, Cost=data)
                    hotelcodes = []
                    for h in hotelfound:
                        hotelcode = h.HotelCode
                        hotelcodes.append(hotelcode)
                    if len(hotelcodes) == 1:
                        output = "Hotel with {} price in {} is {} with price {}".format(
                            operation, state, hotelcode, data)
                    elif len(hotelcodes) > 1:
                        output = "Hotels with {} price in {} are {} with price {}".format(
                            operation, state, hotelcodes, data)

                elif operation == "Average":
                    data = average
                    output = "Average cost of Hotel in {} is {}".format(
                        state, data)

            elif searchby == 'Rating':
                for hotel in state_hotels:
                    rating = hotel.Rating
                    ratings.append(rating)
                lowest = min(ratings)
                highest = max(ratings)
                average = Average(ratings)
                average = round(average, 1)
                if operation == "Highest" or operation == "Lowest":
                    if operation == "Highest":
                        data = highest
                    elif operation == "Lowest":
                        data = lowest

                    hotelfound = Hotel.objects.all().filter(State=state, Rating=data)
                    hotelcodes = []
                    for h in hotelfound:
                        hotelcode = h.HotelCode
                        hotelcodes.append(hotelcode)
                    if len(hotelcodes) == 1:
                        output = "Hotel with {} rating in {} is {} with rating {}".format(
                            operation, state, hotelcode, data)
                    elif len(hotelcodes) > 1:
                        output = "Hotels with {} rating in {} are {} with rating {}".format(
                            operation, state, hotelcodes, data)

                elif operation == "Average":
                    data = average
                    output = "Average rating of Hotel in {} is {}".format(
                        state, data)

            else:
                output = "Please enter all the details"
        else:
            output = "Please enter all the details"
        
    result = {"output": output}
    return render(request, 'basic.html', result)
