import { environment } from "../../enviroments/enviroment";

export const ApiEndpoints = {
    attractionType: `${environment.apiUrl}/Attraction-type`,
    attractions: `${environment.apiUrl}/Attractions`,
    region: `${environment.apiUrl}/region`,
    savedtravels: `${environment.apiUrl}/sacedTravel`,
    TravelPerUser: `${environment.apiUrl}/TravelPerUser`,
    user: `${environment.apiUrl}/user`,
    visitor: `${environment.apiUrl}/visitor`,
    visitorPerAttraction: `${environment.apiUrl}/visitorPerAttraction`
    // , users: '/api/users'
}
