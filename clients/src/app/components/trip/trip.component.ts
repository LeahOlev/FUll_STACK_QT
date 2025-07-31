import { Component, inject } from '@angular/core';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-trip',
  imports: [RouterModule],
  templateUrl: './trip.component.html',
  styleUrl: './trip.component.scss'
})
export class TripComponent {
  router = inject(Router);
  img = "assets/dreampPool.jpg"
  name = "Dream pool ..."
  pool1 = false;
  pool2 = false;
  pool3 = false;

  changeP1() {
    this.pool1 = !this.pool1;
  }

  changeP2() {
    this.pool2 = !this.pool2;
  }
  
  changeP3() {
    this.pool3 = !this.pool3;
  }
  goToComponent(path: string) {
    this.router.navigate([path]);

  }
}
