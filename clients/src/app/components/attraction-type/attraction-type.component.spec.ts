import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttractionTypeComponent } from './attraction-type.component';

describe('AttractionTypeComponent', () => {
  let component: AttractionTypeComponent;
  let fixture: ComponentFixture<AttractionTypeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AttractionTypeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AttractionTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
