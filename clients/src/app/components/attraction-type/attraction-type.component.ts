import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatFormFieldModule } from '@angular/material/form-field';
import { attractionType } from '../../models/attraction-type.model';
import { service } from '../../services/service.service';
import { GenericService } from '../../services/GenericService.service';
import { HttpClient } from '@angular/common/http';
import { ApiEndpoints } from '../../config/api-endpoint';
import { Map } from 'immutable';

@Component({
  selector: 'app-attraction-type',
  standalone: true,
  imports: [MatCheckboxModule, FormsModule, MatFormFieldModule, CommonModule],
  templateUrl: './attraction-type.component.html',
  styleUrls: ['./attraction-type.component.scss']
})
export class AttractionTypeComponent implements OnInit {
  cards: attractionType[] = [];
  private service = inject(service);
  private attractionService = new GenericService<attractionType>(inject(HttpClient), ApiEndpoints.attractionType);

  ngOnInit(): void {
    this.attractionService.getAll().subscribe(data => {
      this.cards = data.map(card => ({
        ...card,
        isSelected: false,
        selectedQuantity: 0
      }));
    });
  }

  onCardClick(card: attractionType) {
    card.isSelected = !card.isSelected;
  }

  confirmSelection(card: attractionType) {
    if (card.selectedQuantity > 0) {
      const currentMap = this.service.getTrip().attraction;
      const updatedMap = currentMap.set(card, card.selectedQuantity);
      this.service.updateTrip({ attraction: updatedMap });
      console.log('עודכן ל-tripData:', updatedMap.toJS());
    }
  }

  isSelected(card: attractionType): boolean {
    return card.isSelected;
  }
}


// import { CommonModule } from '@angular/common';
// import { Component, inject } from '@angular/core';
// import { FormsModule } from '@angular/forms';
// import { MatCheckboxModule } from '@angular/material/checkbox';
// import { MatFormFieldModule } from '@angular/material/form-field';
// import { MatInput } from '@angular/material/input';
// import { MatSelectModule } from '@angular/material/select';
// import { service } from '../../services/service.service';
// import { GenericService } from '../../services/GenericService.service';
// import { attractionType } from '../../models/attraction-type.model';

// @Component({
//   selector: 'app-attraction-type',
//   standalone: true,
//   imports: [MatCheckboxModule, FormsModule, MatFormFieldModule, CommonModule],
//   templateUrl: './attraction-type.component.html',
//   styleUrls: ['./attraction-type.component.scss']
// })
// export class AttractionTypeComponent {
//   type = "";
//   // AttractionTypeService!: GenericService<attractionType>;
//   // cards:attractionType[]=[];
//   // service=inject(service)
  
  
//   // ngOnInit(): void {
//   //   this.AttractionTypeService.getAll().subscribe(data => this.cards = data);
//   // }
//   cards = [
//     { id: 1, image: 'assets/image1.jpg', caption: 'יבש', isSelected: false, selectedQuantity: 0 },
//     { id: 2, image: 'assets/image2.jpg', caption: 'פארקים וגינות', isSelected: false, selectedQuantity: 0 },
//     { id: 3, image: 'assets/image3.jpg', caption: 'מפלים וטבע', isSelected: false, selectedQuantity: 0 },
//     { id: 4, image: 'assets/image4.jpg', caption: 'לונהפארק', isSelected: false, selectedQuantity: 0 },
//     { id: 5, image: 'assets/image5.jpg', caption: 'מסלולי הליכה', isSelected: false, selectedQuantity: 0 },
//     { id: 6, image: 'assets/image6.jpg', caption: 'רטוב', isSelected: false, selectedQuantity: 0 },
//     { id: 7, image: 'assets/image7.jpg', caption: 'אתרים', isSelected: false, selectedQuantity: 0 },
//   ];

//   onCardClick(card: any) {
//     if (!card.isSelected) {
//       this.cards.forEach(c => c.isSelected = false); // Deselect other cards
//     }
//     card.isSelected = !card.isSelected; // Toggle selection
//   }

//   confirmSelection(card: any) {
//     console.log(`Confirmed quantity for ${card.caption}: ${card.selectedQuantity}`);
//     // Do not hide the popup after confirmation
//   }

//   isSelected(card: any): boolean {
//     return card.isSelected; // Return the selection state
//   }
// }




