# HBnB (Holberton Evolution Bed and Breakfast)

# ➜ Package
HBnB is structured using a **3-layer architecture** and follows **Object-Oriented Programming (OOP)** principles.

### _Layers_

1. Presentation Layer

- Exposes API endpoints
- Handles requests and responses

2. Business Logic Layer

- Contains core domain classes (User, Location, Review, Amenity)
- Applies validation and business rules
- Manages relationships between objects

3. Persistence Layer

- Handles database operations (CRUD)
- Stores and retrieves application data

**_Flow :_**
Presentation → Business Logic → Persistence

**_OOP Principles Used :_**

**Encapsulation:** Private attributes (e.g., id, email, password) are protected and accessed via methods.

**Abstraction:** Business logic is separated from API and database details.

**Association:** A User owns Location and writes Review. Location contains Amenity and Review.

**Composition:** A Location is composed of multiple Amenity objects.



# ➜ Classes
The classes for HBnB are

**1. User:** Represents a user of the platform (guest, host or administrator), with attributes such as email, password, first name, and last name.

**2. Location:** Represents properties listed on the site, including details like the location (longitude and latitude), a description and the price.

**3. Amenity:** Represents the amenities offered at a place.

**4. Review:** Represents ratings and comments provided by a user about a specific place.

**_Typical Relationships:_**
A User can own many Places and write many Reviews.
A Place can have many Amenities and be referenced in multiple Reviews but only has one owner.
A Review can only be written by one User and reference one Place.
An Amenity belongs to only one place.

For more details, please refer to the UML class diagram

# ➜ Sequence

**1. Get Places (GET /places)**

User → API → Business Logic → Database → Response list.

**2. User Registration**

User submits data → Validate → Store in database → Return success/error.

**3. Create Review**

Validate user + location → Insert review → Return result.

**4. Create Place**

Validate owner + data → Insert place → Return result.
