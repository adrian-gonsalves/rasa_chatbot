import zomatopy
import json
import pandas as pd

def search_restaurants(loc, cuisine, price):
	# set the api key and initialize the zomato app
	config={ "user_key":"f2908e64685067cfe0673670a0f71388"}
	zomato = zomatopy.initialize_app(config)

	location_detail=zomato.get_location(loc, 1)
	loc_json = json.loads(location_detail)
	lat=loc_json["location_suggestions"][0]["latitude"]
	lon=loc_json["location_suggestions"][0]["longitude"]
	cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
	

	results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
	d1 = json.loads(results)
	d = d1['restaurants']

	df = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                     'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two']
                     , 'restaurant_url': x['restaurant']['url'] } for x in d])

	df['budget'] = df.apply(lambda row: budget_group(row),axis=1)
	restaurant_df = df[(df.budget == price)]
	restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)

	return restaurant_df


def budget_group(row):
		if row['budget_for2people'] <300 :
			return 'less than 300'
		elif 300 <= row['budget_for2people'] <700 :
			return '300-700'
		else:
			return 'greater than 700'