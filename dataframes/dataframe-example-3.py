from pandas import DataFrame, Series
import numpy

def create_dataframe():

	countries = ['Russian Fed.', 'Norway', 'Canada', 'United States','Netherlands', 'Germany', 'Switzerland', 'Belarus','Austria', 'France', 'Poland', 'China', 'Korea', 'Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
	gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
	silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
	bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

	olympic_medals_count = {'country_name': Series(countries),'gold': Series(gold),'silver': Series(silver),'bronze': Series(bronze),}

	olympic_medals_count_df = DataFrame(olympic_medals_count)
	return olympic_medals_count_df

def avg_medal_count():

	countries = ['Russian Fed.', 'Norway', 'Canada', 'United States','Netherlands', 'Germany', 'Switzerland', 'Belarus','Austria', 'France', 'Poland', 'China', 'Korea', 'Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
	gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
	silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
	bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

	olympic_medals_count = {'country_name': Series(countries),'gold': Series(gold),'silver': Series(silver),'bronze': Series(bronze),}

	olympic_medals_count_df = DataFrame(olympic_medals_count)
	avg_bronze_at_least_one_gold = numpy.mean(olympic_medals_count_df['gold'].map(lambda x: x >= 1) & olympic_medals_count_df['bronze'].map(lambda x: x >= 1))
	print(avg_bronze_at_least_one_gold)

avg_medal_count()