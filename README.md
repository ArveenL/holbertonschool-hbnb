# holbertonschool-hbnb
HBnB
------
Key Classes in the HBnB UML
The following core classes are fundamental to the project and usually form the basis of the UML class diagram:

->BaseModel: The parent class for all other models. It manages common attributes like id, created_at, and updated_at, along with methods for saving and converting to a dictionary representation.

->User: Represents a user of the platform (can be a guest or a host), with attributes such as email, password, first name, and last name.

->State: Represents a geographical state, linked to cities.

->City: Represents a city within a state.

->Place: Represents an accommodation listing (e.g., house, room), including details like location, host ID, number of rooms, and price per night.

->Amenity: Represents a facility or service offered at a place (e.g., Wi-Fi, pool, parking).

->Review: Represents feedback and ratings provided by a user about a specific place.

->FileStorage (or Database Storage): A storage engine class responsible for serializing instances to a JSON file or MySQL database and deserializing them back into objects. 

Typical Relationships:
All classes (User, State, City, Place, etc.) inherit from BaseModel.
A User can be the host of many Place listings and a guest who writes many Reviews and makes many Bookings.
A Place is located in a City, which belongs to a State.
A Place can have many Amenity options and many Reviews.
The application uses an API to provide an interface between the front-end and the data stored by the FileStorage engine or database. 
For a visual representation, kindly refer to UML diagram available in same repo.
