import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { GenericService } from '../../services/GenericService.service';
import { Region } from '../../models/region.model';
import { service } from '../../services/service.service';
import { HttpClient } from '@angular/common/http';
import { ApiEndpoints } from '../../config/api-endpoint';

@Component({
  selector: 'app-duration',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './duration.component.html',
  styleUrl: './duration.component.scss'
})
export class DurationComponent {
  readonly service = inject(service);
  area = 'assets/Maps.png'
  clock = 'assets/clock.png'
  timeObject = {
    startTime: 0,
    endTime: 0
  };
  errorMessage: string = '';

  totalHours: number = 6;
  maxAttractions: number = 0;
  ngOnInit(): void {
    this.maxAttractions = this.calculateAttractions(this.totalHours);
    this.regionService.getAll().subscribe(data => {
      this.selectType = data;
    });
  }


  calculateAttractions(total: number): number {
    const hoursPerAttraction = 2;
    return Math.floor(total / hoursPerAttraction);
  }
  submitTimes() {
    if (this.timeObject.startTime < 1 || this.timeObject.startTime > 12) {
      this.errorMessage = 'שעת התחלה חייבת להיות בין 0 ל-12';
      return;
    }
    if (this.timeObject.endTime < 1 || this.timeObject.endTime > 12) {
      this.errorMessage = 'שעת סיום חייבת להיות בין 0 ל-12';
      return;
    }
    this.errorMessage = '';
    this.service.updateTrip({
      startHour: this.timeObject.startTime,
      endHour: this.timeObject.endTime,
      area: this.service.getTrip().area ?? 0
    });
    console.log(this.service.getTrip());
  }
  //region
  regionService = new GenericService<Region>(inject(HttpClient), ApiEndpoints.region);
  selectType: Region[] = [];



  onRegionChange(regionID: number) {
    this.service.updateTrip({ area: regionID });
  }






  // selectType: any = [
  //   { name: 'צפון ', completed: false },
  //   { name: 'דרום', completed: false },
  //   { name: 'מרכז ', completed: false },
  // ]



}

