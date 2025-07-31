import { Component, inject } from '@angular/core';
import { LoginComponent } from '../login/login.component';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';


@Component({
  selector: 'app-home',
  imports: [RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})

export class HomeComponent {
  public click = false;
  img = 'assets/logo.jpg'
  router = inject(Router);
  readonly dialog = inject(MatDialog)

  onClick() {
    this.click = true;
    console.log(this.click);
    if (this.click) {
      this.router.navigate(['/login']);
    }
  }
  goToComponent(path: string) {
    this.router.navigate([path]);

  }
  openDialog(): void {
    const dialodRef = this.dialog.open(LoginComponent)
  }
}
