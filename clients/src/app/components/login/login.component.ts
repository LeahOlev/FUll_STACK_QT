import { CommonModule } from '@angular/common';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { user } from '../../models/user.model';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-login',
  imports: [FormsModule, CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnInit {
  readonly dialog = inject(MatDialog);
  readonly userservice = inject(UserService);
  readonly rourouterter = inject(Router)
  click: boolean = false
  formGroup!: FormGroup;
  mouseoverLogin: boolean = false;
  constructor(private formBuilder: FormBuilder) { }
  onClick() {
    this.click = true;
  }



  ngOnInit() {
    this.initForm();
  }
  initForm() {

    this.formGroup = this.formBuilder.group({
      firstName: ['', [Validators.required, Validators.maxLength(9)]],
      lastName: ['', [Validators.required, Validators.maxLength(9)]],
      email: ['', [Validators.required, Validators.email, Validators.maxLength(8)]]
      , ID: ['', [
        Validators.required,
        Validators.minLength(9),
        Validators.maxLength(9),
        Validators.pattern(/^[0-9]{9}$/)
      ]]
    });
  }
  passwordFieldType = 'password';

  toggleIdVisibility() {
    this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password';
  }
  close(): void {
    if (this.formGroup.invalid) {
      return;
    }

    const user: user = this.formGroup.value;
    console.log('שולחת את המשתמש:', user);

    this.userservice.saveUser(user).subscribe({
      next: () => this.dialog.closeAll(),
      error: err => console.error('שגיאה', err)
    });
    // close(): void {
    //   this.click = true;
    //   if (this.click) {
    //     const dialodRef = this.dialog.closeAll()
    //   }
    // }
    // emailValidator(control: FormControl) {
    //   if (
    //     control.value.match(
    //       /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    //     )
    //   ) {
    //     return null;
    //   } else {
    //     return { invalidEmailAddress: true };
    //   }
  }
}