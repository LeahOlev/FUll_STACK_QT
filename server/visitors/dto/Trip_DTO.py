class TripDTO:
    def __init__(self, pointDeparture, startHour, endHour, area, typeVisitor, attraction, dateTrip, budget, countPepole):
        self.pointDeparture = pointDeparture
        self.startHour = startHour
        self.endHour = endHour
        self.area = area
        self.typeVisitor = typeVisitor
        self.attraction = attraction  # dict {AttractionTypeID: count}
        self.dateTrip = dateTrip
        self.budget = budget
        self.countPepole = countPepole
