import { Routes } from '@angular/router';

export const routes: Routes = [
    { path: '', redirectTo: 'navbar', pathMatch: 'full' },

    {
        path: 'navbar',
        loadComponent: () =>
            import('./components/navbar/navbar.component').then((m) => m.NavbarComponent
            )
        , children: [
            {
                path: 'home',
                loadComponent: () =>
                    import('./components/home/home.component').then((m) => m.HomeComponent)
            },
            {
                path: 'about_us',
                loadComponent: () =>
                    import('./components/about-us/about-us.component').then((m) => m.AboutUsComponent)
            },
            {
                path: 'requirement',
                loadComponent: () =>
                    import('./components/requirement/requirement.component').then((m) => m.RequirementComponent)
                // , children: [
                //     // {
                //     //     path: 'visitors',
                //     //     loadComponent: () =>
                //     //         import('./components/visitors/visitors.component').then((m) => m.VisitorsComponent
                //     //         )
                //     // },
                //     // {
                //     //     path: 'region',
                //     //     loadComponent: () =>
                //     //         import('./components/region/region.component').then((m) => m.RegionComponent)
                //     // },
                //     {
                //         path: 'budget',
                //         loadComponent: () =>
                //             import('./components/budget/budget.component').then((m) => m.BudgetComponent)
                //     },
                //     {
                //         path: 'duration',
                //         loadComponent: () =>
                //             import('./components/duration/duration.component').then((m) => m.DurationComponent)
                //     },
                //     {
                //         path: 'attractionType',
                //         loadComponent: () =>
                //             import('./components/attraction-type/attraction-type.component').then((m) => m.AttractionTypeComponent)
                //     },
                //     {
                //         path: 'time',
                //         loadComponent: () =>
                //             import('./components/time/time.component').then((m) => m.TimeComponent)
                //     },
                // ]
            },
            // {
            //     path: 'visitors',
            //     // component:VisitorsComponent
            //     loadComponent: () =>
            //         import('./component/visitors/visitors.component').then((m) => m.VisitorsComponent
            //         )
            // },
            // {
            //     path: 'region',
            //     loadComponent: () =>
            //         import('./component/region/region.component').then((m) => m.RegionComponent)
            // },
            // {
            //     path: 'budget',
            //     loadComponent: () =>
            //         import('./component/budget/budget.component').then((m) => m.BudgetComponent)
            // },
            // {
            //     path: 'duration',
            //     loadComponent: () =>
            //         import('./component/duration/duration.component').then((m) => m.DurationComponent)
            // },
            // {
            //     path: 'attractionType',
            //     loadComponent: () =>
            //         import('./component/attraction-type/attraction-type.component').then((m) => m.AttractionTypeComponent)
            // },
            // {
            //     path: 'time',
            //     loadComponent: () =>
            //         import('./component/time/time.component').then((m) => m.TimeComponent)
            // },

        ],
    },
    {
        path: 'connectToTrip',
        loadComponent: () =>
            import('./components/connect-to-trip/connect-to-trip.component').then((m) => m.ConnectToTripComponent)
    },

    {
        path: 'trip',
        loadComponent: () =>
            import('./components/trip/trip.component').then((m) => m.TripComponent)
    },


];
