import { Component ,OnInit,inject} from '@angular/core';
import { RouterModule } from '@angular/router';
import { timeout } from 'rxjs';
import { Router } from '@angular/router';


@Component({
  selector: 'app-connect-to-trip',
  imports: [RouterModule],
  templateUrl: './connect-to-trip.component.html',
  styleUrl: './connect-to-trip.component.scss'
})
export class ConnectToTripComponent implements OnInit {

  img = 'assets/Hour-Glass.png';
  router = inject(Router)

  // router = inject(Router);
  ngOnInit(): void {
    setTimeout(() => {
      this.router.navigate(['/trip']);
    }, 2500)
  }
}

