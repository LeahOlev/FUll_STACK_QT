class AttractionsDTO:
    def __init__(self, AttractionID, Lat, Lng, RegionId, AttractionName, DurationMax, Price,
                 DescriptionLink, AttractionTypeID,OpeningHours,ClosingHours):
        self.AttractionID = AttractionID
        self.Lat = Lat
        self.Lng = Lng
        self.RegionId = RegionId #קוד איזור לפי טבלת איזורים
        self.AttractionName = AttractionName #שם האטרקציה
        self.openingHours=OpeningHours #שעת פתיחה
        self.closingHours = ClosingHours #שעת סגירה
        self.DurationMax = DurationMax #זמן שהייה מקסימאלי
        self.Price = Price #מחיר לאדם
        self.DescriptionLink = DescriptionLink #קישור לאתר האטרקציה
        self.AttractionTypeID = AttractionTypeID #קטגוריה של אטרקציה
