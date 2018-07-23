# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Tag,\
    Cuisine, Collection, Association, Dish
from cta import app
from flask_graphql import GraphQLView
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImageSchema,\
    RestaurantAmenitySchema, CuisineSchema, CollectionSchema, AssociationSchema, TagSchema, DishSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/restaurant', methods=['GET', 'POST'])
def restaurant_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        cuisine = request.args.get('cuisine')
        args.pop('cuisine', None)
        collection = request.args.get('collection')
        args.pop('collection', None)
        dish = request.args.get('dish')
        args.pop('dish', None)
        args.pop('rating', None)
        page = request.args.get('page', None)
        per_page = request.args.get('per_page', None)
        cuisine_restaurant_id = []
        collection_restaurant_id = []
        dish_restaurant_id = []
        rating_restaurant_id = []
        if cuisine:
            cuisine_id = Cuisine.query.filter(Cuisine.cuisine == cuisine).first().id
            print(cuisine_id)
            
            restaurant_list = Association.query.filter(Association.cuisine_id == cuisine_id).all()
            for restaurant_obj in restaurant_list:
                cuisine_restaurant_id.append(restaurant_obj.restaurant_id)
            restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(cuisine_restaurant_id)).all()
            
        elif collection:
            collection_id = Collection.query.filter(Collection.collection == collection).first().id
            print(collection_id)
            
            restaurant_list = Association.query.filter(Association.collection_id == collection_id).all()
            for restaurant_obj in restaurant_list:
                collection_restaurant_id.append(restaurant_obj.restaurant_id)
            restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(collection_restaurant_id)).all()
            
        elif dish:
            print(dish)
            dish_id = Dish.query.filter(Dish.dish == dish).first().id
            print(dish_id)
            restaurant_list = Association.query.filter(Association.dish_id == dish_id).all()
            for restaurant_obj in restaurant_list:
                dish_restaurant_id.append(restaurant_obj.restaurant_id)
            restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(dish_restaurant_id)).all()
            
        elif rating:
            restaurants = Restaurant.query.filter(Restaurant.rating >= rating).all()
            # for restaurant_obj in restaurant_list:
            #     rating_restaurant_id.append(restaurant_obj.id)
            # restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(rating_restaurant_id)).all()
            
        # if collection and cuisine and rating and dish:
        #     common_id = list(set(cuisine_restaurant_id).intersection(collection_restaurant_id))
        #     common_id = list(set(dish_restaurant_id).intersection(common_id))
        #     common_id = list(set(rating_restaurant_id).intersection(common_id))
            # restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(common_id)).all()
        elif page:
            restaurants = Restaurant.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        else:
            print("else")
            restaurants = Restaurant.query.filter_by(**args).all()
        result = RestaurantSchema(many=True).dump(restaurants)
        return jsonify({'result': {'restaurants': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/amenity', methods=['GET', 'POST'])
def restaurant_amenity():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = RestaurantAmenity.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantAmenitySchema(many=True).dump(data)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})
    else:
        post = RestaurantAmenity(**request.json)
        post.save()
        result = RestaurantAmenitySchema().dump(post)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/images', methods=['GET', 'POST'])
def restaurant_image_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = RestaurantImage.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantImageSchema(many=True).dump(data)
        return jsonify({'result': {'images': result.data}, 'message': "Success", 'error': False})
    else:
        post = RestaurantImage(**request.json)
        post.save()
        result = RestaurantImageSchema().dump(post)
        return jsonify({'result': {'image': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/tag', methods=['GET', 'POST'])
def restaurant_tag_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Tag.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = TagSchema(many=True).dump(data)
        return jsonify({'result': {'tag': result.data}, 'message': "Success", 'error': False})
    else:
        post = Tag(**request.json)
        post.save()
        result = TagSchema().dump(post)
        return jsonify({'result': {'tag': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/cuisine', methods=['GET', 'POST'])
def restaurant_cuisine_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Cuisine.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CuisineSchema(many=True).dump(data)
        return jsonify({'result': {'cuisine': result.data}, 'message': "Success", 'error': False})
    else:
        post = Cuisine(**request.json)
        post.save()
        result = CuisineSchema().dump(post)
        return jsonify({'result': {'cuisine': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/collection', methods=['GET', 'POST'])
def restaurant_collection_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Collection.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CollectionSchema(many=True).dump(data)
        return jsonify({'result': {'collection': result.data}, 'message': "Success", 'error': False})
    else:
        post = Collection(**request.json)
        post.save()
        result = CollectionSchema().dump(post)
        return jsonify({'result': {'collection': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/dish', methods=['GET', 'POST'])
def restaurant_dish_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Dish.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = DishSchema(many=True).dump(data)
        return jsonify({'result': {'dish': result.data}, 'message': "Success", 'error': False})
    else:
        post = Dish(**request.json)
        post.save()
        result = DishSchema().dump(post)
        return jsonify({'result': {'dish': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/association', methods=['GET', 'POST'])
def restaurant_association_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        # collection = request.args.get('collection')
        # args.pop('collection', None)
        # rating = request.args.get('rating')
        # args.pop('rating', None)
        # rating = request.args.get('rating')
        # args.pop('rating', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Association.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = AssociationSchema(many=True).dump(data)
        return jsonify({'result': {'association': result.data}, 'message': "Success", 'error': False})
    else:
        post = Association(**request.json)
        post.save()
        result = AssociationSchema().dump(post)
        return jsonify({'result': {'association': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/search', methods=['GET', 'POST'])
def restaurant_search_api():
    search = request.json
    search = search['search']
    cities = []
    names = []
    cuisines = []
    collections = []
    dishes = []
    tags = []
    restaurant_cities = Restaurant.query.distinct(Restaurant.city).filter(Restaurant.city.like('%' + search + '%')).order_by(Restaurant.city).all()
    for restaurant_city in restaurant_cities:
        cities.append(restaurant_city.city)
    restaurant_names = Restaurant.query.distinct(Restaurant.name).filter(Restaurant.name.like('%' + search + '%')).order_by(Restaurant.name).all()
    for restaurant_name in restaurant_names:
        names.append(restaurant_name.name)
    restaurant_cuisines = Cuisine.query.distinct(Cuisine.cuisine).filter(Cuisine.cuisine.like('%' + search + '%')).order_by(Cuisine.cuisine).all()
    for restaurant_cuisine in restaurant_cuisines:
        cuisines.append(restaurant_cuisine.cuisine)
    restaurant_collections = Collection.query.distinct(Collection.collection).filter(Collection.collection.like('%' + search + '%')).order_by(Collection.collection).all()
    for restaurant_collection in restaurant_collections:
        collections.append(restaurant_collection.collection)
    restaurant_dishes = Dish.query.distinct(Dish.dish).filter(Dish.dish.like('%' + search + '%')).order_by(Dish.dish).all()
    for restaurant_dish in restaurant_dishes:
        dishes.append(restaurant_dish.dish)
    restaurant_tags = ['dinner', 'cafe', 'breakfast', 'street_stalls', 'bars', 'lounge', 'diet', 'luxury', 'lunch', 'family',
                  'nightlife', 'pocket_friendly']
    for restaurant_tag in restaurant_tags:
        if restaurant_tag.startswith(search):
            tags.append(restaurant_tag)
    obj = {
    "cities": list(cities),
    "cuisines": list(cuisines),
    "collections": list(collections),
    "dishes": list(dishes),
    "tags": list(set(tags)),
    "names": list(names)
    }
    return jsonify({'result': obj, 'message': "Success", 'error': False})
