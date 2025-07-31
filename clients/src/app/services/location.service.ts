import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpServiceBase } from './http-service.base';
import { HttpRequestModel } from '../models/http-request.model';

@Injectable({ providedIn: 'root' })
export class LocationHttpService extends HttpServiceBase {

    private get _serverUrl(): string {
        return `${this.config.ips.servicePath}students/`;
    }

    add_Attractions$(): Observable<LocationHttpService[]> {
        return this.post$(new HttpRequestModel({
            url: this._serverUrl,
            action: ''
        }));
    }

    get_Attractions$(): Observable<LocationHttpService[]> {
        return this.get$(new HttpRequestModel({
            url: this._serverUrl,
            action: ''
        }));
    }

    get_Attractions_by_id$(id: number): Observable<LocationHttpService> {

        return this.get$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'getattractiosnbyId',
            params: { id },
        }));
    }

    update_Attractions$(id: number) {

        return this.put$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'updateattractiondbyid',
            body: { id },
        }));
    }

    delete_Attractions$(id: number) {

        return this.delete$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'deleteattractions',
            body: { id },
        }));
    }
}
