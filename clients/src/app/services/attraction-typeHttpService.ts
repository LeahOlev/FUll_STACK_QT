import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpServiceBase } from './http-service.base';
import { HttpRequestModel } from '../models/http-request.model';

@Injectable({ providedIn: 'root' })
export class AttractionTypeHttpService extends HttpServiceBase {

    private get _serverUrl(): string {
        return `${this.config.ips.servicePath}students/`;
    }

    add_AttractionType$(): Observable<AttractionTypeHttpService[]> {
        return this.post$(new HttpRequestModel({
            url: this._serverUrl,
            action: ''
        }));
    }
    get_AttractionType$(): Observable<AttractionTypeHttpService[]> {
        return this.get$(new HttpRequestModel({
            url: this._serverUrl,
            action: ''
        }));
    }

    get_AttractionType_by_id$(id: number): Observable<AttractionTypeHttpService> {

        return this.get$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'getattractiotypenbyId',
            params: { id },
        }));
    }

    update_AttractionType$(id: number) {

        return this.put$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'updateattractiontype',
            body: { id },
        }));
    }

    delete_AttractionType$(id: number) {

        return this.delete$(new HttpRequestModel({
            url: this._serverUrl,
            action: 'deleteattractiontype',
            body: { id },
        }));
    }
}
