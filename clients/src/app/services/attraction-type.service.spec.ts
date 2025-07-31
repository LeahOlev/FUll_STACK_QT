import { TestBed } from '@angular/core/testing';

import { AttractionTypeHttpService } from './attraction-typeHttpService';

describe('CheckHttpService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AttractionTypeHttpService = TestBed.get(AttractionTypeHttpService);
    expect(service).toBeTruthy();
  });
});
