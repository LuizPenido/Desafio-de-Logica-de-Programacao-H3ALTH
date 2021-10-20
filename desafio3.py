def countPeopleOnTheBus(arrayBalance):
    totalNumberOfPeoples = 0
    for balance in arrayBalance:
        totalNumberOfPeoples += balance[0]
        totalNumberOfPeoples -= balance[1]

    return totalNumberOfPeoples