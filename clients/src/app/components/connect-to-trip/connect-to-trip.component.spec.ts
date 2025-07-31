import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConnectToTripComponent } from './connect-to-trip.component';

describe('ConnectToTripComponent', () => {
  let component: ConnectToTripComponent;
  let fixture: ComponentFixture<ConnectToTripComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConnectToTripComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ConnectToTripComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
