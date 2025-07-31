import { Component, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { service } from '../../services/service.service';

@Component({
  selector: 'app-budget',
  standalone: true,
  imports: [RouterModule, MatFormFieldModule, MatSelectModule, FormsModule],
  templateUrl: './budget.component.html',
  styleUrl: './budget.component.scss'
})
export class BudgetComponent {
  money = 'assets/Cash.png'
  budget: number;
  maxBudget: number;
  errorMessage: string;
  service = inject(service)

  constructor() {
    this.budget = 0;
    this.maxBudget = 5500;
    this.errorMessage = '';
  }
  submitBudget() {
    if (this.budget > this.maxBudget || this.budget < 0) {
      alert(`התקציב חייב להיות בין 0 ל-${this.maxBudget}`);
    } else {
      // כאן נעשה עדכון של trip
      if (this.service.getTrip()) {
        this.service.updateTrip({ budget: this.budget });
      }
      console.log('התקציב שלך הוא:', this.service.getTrip().budget);
    }
  }

  clickWoman = false;
  clickMan = false;
  clickFamily = false

  selectedLevelWoman = ''
  selectedLevelMan = ''
  selectedLevelFamily = ''
  selectedAgeWoman = ''
  selectedAgeMan = ''

  click: boolean = true

  onClickWomank() {
    if (this.clickMan) {
      this.clickMan = !this.clickMan
      this.clickWoman = true;

    }
    if (this.clickFamily) {
      this.clickFamily = !this.clickFamily
      this.clickWoman = true
    }
    else {
      this.clickWoman = true

    }
  }

  onClickman() {
    if (this.clickWoman) {
      this.clickWoman = !this.clickWoman
      this.clickMan = true;

    }
    if (this.clickFamily) {
      this.clickFamily = !this.clickFamily
      this.clickMan = true
    }
    else {
      this.clickMan = true

    }
  }

  onClickFamily() {
    if (this.clickMan) {
      this.clickMan = !this.clickMan
      this.clickFamily = true;

    }
    if (this.clickWoman) {
      this.clickWoman = !this.clickWoman
      this.clickFamily = true
    }
    else {
      this.clickFamily = true

    }
  }
}
