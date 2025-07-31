import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { service } from '../../services/service.service';

@Component({
  selector: 'app-time',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './time.component.html',
  styleUrls: ['./time.component.scss']
})
export class TimeComponent {
  service = inject(service);

  date: string = '';

  onDateChange(event: Event) {
    const input = event.target as HTMLInputElement;
    this.date = input.value;
    const parsedDate = new Date(this.date);
    if (!isNaN(parsedDate.getTime())) {
      this.service.updateTrip({ dateTrip: parsedDate });
      console.log('תאריך עודכן ל:', parsedDate);
    }
  }
}
