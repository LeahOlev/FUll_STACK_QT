import { Component } from '@angular/core';
import { DurationComponent } from '../duration/duration.component'
import { TimeComponent } from '../time/time.component';
import { AttractionTypeComponent } from '../attraction-type/attraction-type.component';
import { BudgetComponent } from '../budget/budget.component';
import { RouterModule } from "@angular/router";
import { CommonModule } from '@angular/common';
@Component({
  standalone: true,
  selector: 'app-requirement',
  templateUrl: './requirement.component.html',
  styleUrls: ['./requirement.component.css'],
  imports: [
    CommonModule,
    BudgetComponent,
    TimeComponent,
    DurationComponent,
    AttractionTypeComponent,
  
]
})
export class RequirementComponent {}

