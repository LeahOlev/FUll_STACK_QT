
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { trip } from '../models/trip.model';
import { Injectable } from '@angular/core';
import { ApiEndpoints } from '../config/api-endpoint';
import { attractionType } from '../models/attraction-type.model';
import {Map} from 'immutable';
import { Attractions } from '../models/attractions.model';
import{environment} from '../../enviroments/enviroment'
@Injectable({ providedIn: 'root' })
export class service {
    private tripData: trip = {
        pointDeparture: { lat: 0, lng: 0 }, // או null אם מותר
        startHour: 0,
        endHour: 0,
        area: 0,
        typeVisitor: { visitorID: 0, regionName: '' },
        attraction: Map<attractionType, number>(),
        dateTrip: new Date(),
        budget: 0,
        countPepole: 0
    };
    apiUrl=environment.apiUrl+"/plan-trip";
    constructor(private http: HttpClient) { }

    getTrip(): trip {
        if (!this.tripData)
            throw new Error('tripData not initialized');
        return this.tripData;
    }
    updateTrip(data: Partial<trip>) {
        if (!this.tripData)
            this.resetTrip(); 
        Object.assign(this.tripData!, data);
    }

    sendTrip(): Observable<any> {
        return this.http.post(ApiEndpoints.savedtravels, this.tripData);
    }
    resetTrip() {
        this.tripData = {
            pointDeparture: { lat: 0, lng: 0 },
            startHour: 0,
            endHour: 0,
            area: 0,
            typeVisitor: { visitorID: 0, regionName: '' },
            attraction: Map<attractionType, number>(),
            dateTrip: new Date(),
            budget: 0,
            countPepole: 0
        };
    }
    build(): Observable<Attractions[]> {
        return this.http.get<Attractions[]>(`${this.apiUrl}/${this.tripData}`);
      }
      
}