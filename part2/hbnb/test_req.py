#!/usr/bin/env python3
import requests as rq
r = rq.post('http://localhost:5678/api/v1/users/', json={"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"})
user_id = r.json()['id']
print(f"user: {user_id}")
r = rq.post('http://localhost:5678/api/v1/amenities/', json={"name": "Wi-Fi"})
amenity_id = r.json()['id']
print(f"amenity: {amenity_id}")
r = rq.post('http://localhost:5678/api/v1/places/', json={"title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": user_id})
place_id = r.json()['id']
print(f"place: {place_id}")
r = rq.post('http://localhost:5678/api/v1/reviews/', json={"text": "Great place to stay!", "rating": 5, "user_id": user_id, "place_id": place_id})
review_id = r.json()['id']
print(f"review: {review_id}")
