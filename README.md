# G19-USTH2022-Python


***Group members:***
- BI11-015: Nguyễn Hải Anh
- BI11-240: Vũ Quốc Thái
- BI11-274: Nguyễn Thành Trung
- BI11-275: Nguyễn Trịnh Bảo Trung
- BI11-276: Nguyễn Việt Trung
- BI11-279: Trịnh Tuấn Tú


***Topic (#4) : Airline booking information management system***

***PRESENTATION ORDER: 1***

Program features:
- Most important classes: Flight.
- Flight class variable list_passanger will be a 2D array with elements being the passenger of each seat.
- Each plane has 120 seats, 20 letters of alphabet for number of rows, and 6 seats per row.
- To see if a seat is taken or not, another 2D array of 1s and 0s will be created parallel to the passenger list, 0 = empty, 1 = taken.
- All classes synchronised through f_code, variable for flight code.


GUI features:
- Seperate UI for managing the flights, and adding/booking additional seats.
- Show a hull diagram of the plane, with squares representing seats, reds are booked, greens are empty.
- Green seats can be clicked onto to choose to book.


Goal:
- List of flights are sorted according to depart time, to display.
- After picking the flight to manage, choose to display either the list of customers sorted by seats, or the hull diagram.
- The hull diagram will appear to pick and book seats.
- The list is for displaying data, and changing data on the list like: name, personal ID, seats.
- Changing depart and arrive time of flights.
- Adding flights.
