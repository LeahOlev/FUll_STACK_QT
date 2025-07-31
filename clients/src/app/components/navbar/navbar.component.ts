import { Component, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';

import { BudgetComponent } from '../../components/budget/budget.component';
import { AttractionTypeComponent } from '../attraction-type/attraction-type.component';
import { HomeComponent } from '../home/home.component';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from '../login/login.component';
import { AreaComponent } from '../area/area.component';


@Component({
  selector: 'app-navbar-component',
  standalone: true,
  imports: [RouterModule, HomeComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {
  global2 = 'assets/Globe.png'
  router = inject(Router);
  logo = 'assets/logo.png'
  readonly dialog = inject(MatDialog)
  goToComponent(path: string) {
    this.router.navigate([path]);
  }

  openDialog(): void {
    this.dialog.open(LoginComponent)
  }
  openDialog2(): void {
    this.dialog.open(AreaComponent)
  }
}

