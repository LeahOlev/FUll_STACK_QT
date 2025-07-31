import { TestBed } from '@angular/core/testing';

import { AttractionsHttpService } from './attractions.service';

describe('CheckHttpService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AttractionsHttpService = TestBed.get(AttractionsHttpService);
    expect(service).toBeTruthy();
  });
});
