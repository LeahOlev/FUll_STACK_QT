import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { user } from '../models/user.model'
import { ApiEndpoints } from '../config/api-endpoint';

@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) {}

  saveUser(user: user): Observable<any> {
    return this.http.post(ApiEndpoints.user, user);
  }
}
