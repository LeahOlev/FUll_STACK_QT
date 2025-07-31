import { CommonModule } from '@angular/common';
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router, RouterModule } from '@angular/router';
import { BudgetComponent } from '../budget/budget.component';

@Component({
  selector: 'app-area',
  imports: [FormsModule, CommonModule, RouterModule,ReactiveFormsModule],
  templateUrl: './area.component.html',
  styleUrl: './area.component.scss'
})
export class AreaComponent {
  lastName = 'lastName:'
  ID = 'ID:'
  click: boolean = false
  readonly dialog = inject(MatDialog)

  onClick() {
    this.click = true;
  }
  router = inject(Router);
  mouseoverLogin: boolean = false;

  formGroup: FormGroup = {} as FormGroup;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.initForm;
  }
  initForm() {

    this.formGroup = this.formBuilder.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      ID: ['', [Validators.required, Validators.maxLength(9), Validators.minLength(9)]],
      email: ['', [Validators.required, Validators.email, Validators.maxLength(8)]]

    });
  }
  close(): void {
    // const { username, password } = this.formGroup.value;
    // localStorage.setItem('login', JSON.stringify({ username, password }));
    // if(this.firstName.length>1 && this.lastName.length>1 && this.email.length>5)

    console.log('value: ', this.formGroup.value);
    console.log('is dirty? ', this.formGroup.dirty);
    console.log('is valid? ', this.formGroup.valid);

    this.click = true;
    if (this.click) {
      const dialodRef = this.dialog.closeAll()
    }
    
    // console.log(this.click);
    // if (this.click) {
    //   this.router.navigate(['/login']);
    // }
  }
  emailValidator(control: FormControl) {
    if (
      control.value.match(
        /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
      )
    ) {
      return null;
    } else {
      return { invalidEmailAddress: true };
    }
  }
}
