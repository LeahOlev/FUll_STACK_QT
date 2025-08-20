# 🏞️ QUICK TRIP - Your Smart Trip Planner

Welcome to **QUICK TRIP**, the ultimate platform for planning customized trips in Israel. Whether you're looking for a relaxing family trip or a challenging trail, our advanced algorithm will find the perfect route for you with a single click.

## 🚀 Key Features

* **AI-Powered Trip Planning**: A smart algorithm analyzes your preferences to create an optimal trip itinerary, including attractions and relevant links.
* **Full Personalization**: Choose the exact data that suits you: date, region, budget, target audience, trip duration, and desired attraction types.
* **Save and Reuse**: The site allows you to save previous trips and access them easily, or choose from pre-planned routes stored in the system.
* **User-Friendly Interface**: A clean and easy-to-use design that makes the planning process quick and simple.

---

## ⚙️ How the Algorithm Works

Our algorithm, implemented in `TripAlgo.py`, is designed to find the most efficient and enjoyable trip route based on a series of filters and a custom scoring system.

### 1. Initial Filtering (`select_attractions`)

The algorithm first performs a preliminary filtering of all available attractions based on the user's input:

* **Target Audience**: It selects only attractions that match the user's defined `typeVisitor`.
* **Region**: Filters attractions based on the specified `area` (`RegionId`).
* **Time Constraints**: Ensures attractions are open during the user's planned trip hours (`openingHours` and `closingHours`).
* **Budget**: Removes attractions that exceed the user's `budget` based on the number of people (`countPepole`) and price per person.

The remaining attractions are then grouped by type (`AttractionTypeID`).

### 2. Attraction Scoring

A custom scoring function `score()` is used to rank attractions within each group, prioritizing those that offer a good balance of cost, travel time, and operating hours.

```python
def score(attraction, origin):
    return (
        0.5 * attraction.Price +
        0.3 * get_drive_time_minutes(origin, attraction) -
        0.2 * (attraction.closingHours - attraction.openingHours)
    )
```
The formula gives more weight to the attraction's price (0.5) and drive time (0.3), while penalizing for a long operation duration (0.2). After scoring, the algorithm selects the N top-ranked attractions from each type, where N is the count specified by the user.
### 3. Route Calculation (`compute_best_route`)
Once the attractions are selected, the algorithm calculates the optimal route. It iterates through every possible permutation of the chosen attractions. For each permutation, it checks if the route is valid by ensuring the arrival and departure times at each attraction fall within its operating hours. The route with the minimum total travel time is selected as the best_route.

### 4. Output Generation (`export_route_to_json`)
Finally, the best_route is formatted into a clear, structured JSON output. The output includes key details for each attraction, such as arrival time, price, and a direct link to the attraction's website (DescriptionLink). The JSON also provides a summary of the total cost and budget status.

## 📝 Quick Usage Guide
1. **Personalization:** On the main page, choose your desired data:
    - **Departure Date:** Select the day you plan to start your trip.
  
    - **Region:** Choose from different regions (North, South, Center, Jerusalem, etc.).
  
    - **Budget:** Mark the budget that suits you (Free, up to ₪100, ₪100+, etc.).
  
    - **Target Audience:** Mark the target audience (Families, Couples, Solo travelers, etc.).
  
    - **Trip Duration:** Choose the duration of the trip in hours.
  
    - **Attraction Types:** Select your preferred types of attractions (Water, Nature, Urban, Historical, etc.).

2. **Generate a Route:** After filling in all the fields, click the "Apply Filter" button for the algorithm to plan your route.

3. **Saving Trips:** To save the route or view previous trips, use the "Save Trip" or "Trip History" option on the profile page.

## 📌 Usage Examples
  - **Example 1 - Family Trip:**

    - **Date:** 17.03.2025
  
    - **Region:** Center
  
    - **Budget:** Up to ₪100
  
    - **Target Audience:** Families
  
    - **Duration:** 4-6 hours
  
    - **Attractions:** Water, Forests

<br/>
The algorithm will present a route that includes a water park or a stream trail with additional attractions, and a link to the relevant website.

Example 2 - Couples Trip:

Date: 25.04.2025

Region: Jerusalem

Budget: ₪100+

Target Audience: Couples

Duration: 6-8 hours

Attractions: Urban, Historical

<br/>
The algorithm will present a route that includes a visit to historical sites and urban activities, such as a tour of Mahane Yehuda market, and relevant links.

Example 3 - Solo Traveler on a Budget:

Date: 10.05.2025

Region: North

Budget: Free

Target Audience: Solo travelers

Duration: 3-5 hours

Attractions: Nature

<br/>
The algorithm will present a route focused on free natural attractions like hiking trails or scenic viewpoints, optimizing for minimal travel time and cost.

Example 4 - Group Trip with a Specific Interest:

Date: 08.06.2025

Region: South

Budget: Up to ₪100

Target Audience: Group

Duration: 5-7 hours

Attractions: Historical

<br/>
The algorithm will present a route that includes historical sites, monuments, and museums in the specified region, ensuring the itinerary fits within the budget and time constraints.

## 🤝 Questions and Support
If you encounter any issues or have questions, please open an issue on GitHub or contact us. Enjoy your next trip!
