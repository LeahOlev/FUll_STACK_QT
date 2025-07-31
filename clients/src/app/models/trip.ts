import { attractionType } from "./attraction-type.model";
import { location } from "./location";
import { visitor } from "./visitor.model";
import {Map} from 'immutable';

export interface trip{
    pointDeparture:location //נקודת מוצא
    startHour:number //שעת התחלה
    endHour:number //שעת חזרה
    area: number //אזור
    typeVisitor:visitor //סוג מטייל
    attraction: Map<attractionType, number>; //מילון של סוג אטרקיצה וכמות מאותה סוג
    dateTrip:Date; //תאריך הטיול
    budget:number//תקציב
    countPepole: number //כמות אנשים
}

