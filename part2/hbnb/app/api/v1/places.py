from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        try:
            new_place = facade.create_place(place_data)
        except Exception:
            return {'error': 'Invalid input data'}, 400
        if new_place is None:
            return {'error': 'Invalid input data'}, 400
        return {'id': new_place.id, 'title': new_place.title, 'description': new_place.description, 'price': new_place.price, 'latitude': new_place.latitude, 'longitude': new_place.longitude, 'owner_id': new_place.owner.id}, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()

        return [
            {
                'id': place.id,
                'title': place.title,
                'latitude': place.latitude,
                'longitude': place.longitude
            }
            for place in places
        ], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        owner = place.owner
        owner_dict = {"id": owner.id, "first_name": owner.first_name, "last_name": owner.last_name, "email": owner.email}
        list_amenities = [{'id': amenity.id, 'name': amenity.name}for amenity in place.amenities], 200
        return {'id': place.id, 'title': place.title, 'description': place.description, 'latitude': place.latitude, 'owner': owner_dict, 'amenities': list_amenities}, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404
        if not place_data:
            return {'error': 'Invalid input data'}, 400
        
        if "title" in place_data:
            if not isinstance(place_data["title"], str):
                return {'error': 'Invalid input data'}, 400
            if len(place_data["title"]) > 100:
                return {'error': 'Invalid input data'}, 400
        if "description" in place_data:
            if not isinstance(place_data["description"], str):
                return {'error': 'Invalid input data'}, 400
        if "price" in place_data:
            if not isinstance(place_data["price"], (float, int)):
                return {'error': 'Invalid input data'}, 400
        if "latitude" in place_data:
            if not isinstance(place_data["latitude"], (float, int)):
                return {'error': 'Invalid input data'}, 400
            if place_data["latitude"] > 90 or place_data["latitude"] < -90:
                return {'error': 'Invalid input data'}, 400
        if "longitude" in place_data:
            if not isinstance(place_data["longitude"], (float, int)):
                return {'error': 'Invalid input data'}, 400
            if place_data["longitude"] > 180 or place_data["longitude"] < -180:
                return {'error': 'Invalid input data'}, 400

        updated_place = facade.update_place(place_id, place_data)

        if not updated_place:
            return {'error': 'Place not found'}, 404
        return {"message": "Place updated successfully"}, 200

@api.route('/<place_id>/reviews')
class PlaceResource(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Reviews not found')
    def get(self, place_id):
        """Get list of reviews for a place"""
        reviews = facade.get_reviews_by_place(place_id)
        if not reviews:
            return {'error': 'Place not found'}, 404
        return [{'id': review.id, 'text': review.text, "rating": review.rating}for review in reviews], 200
