# Michelin-project

This project does the following things:

1) Merges three datasets sourced from Kaggle called "one-star-michelin-restaurants.csv
 "two-stars-michelin-restaurants" and "three-stars-michelin-restaurants".
 
2) Fixes incorrect values in the dataset and adds a "country" field for each restaurant.

3) Pings the corresponding url's for Michelin guide's web page and discards the restaurants, 
whose web is not responding (i.e the restaurant is no longer in business).

4) Scrapes Michelin's web page in order to obtain the minimum and maximum price range for each restaurant
according to the Michelin guide. It also corrects some values that don't have it's local currency correctly stated.

5) Once obtained the interval of prices in each corresponding local currency, the program scrapes
the web page "https://www.finanzen.net/" in order to get the most updated currency rate agains the EUR for each of the 
local currencies of each restaurant.

6) Once obtained the exchange rates, it calculates all the minimum and maximum prices (in spot EUR prices)
for each restaurant.

7) We can use the program to find out which are the 3 cheapest restaurants in a 
specific country, based on a certain star rating. The program will display the result in an html formatted table, using
the Plotly library.

For example, to get the three cheapest restaurants in the United states with 2 Michelin stars, we would do:
'python main.py "United States" 2'

The country has to be one of the following and has to be written EXACTLY as such:

United States
United Kingdom
China
Singapore
Denmark
South Korea
Thailand
Taiwan
Sweden
Austria
Brasil
Ireland
Norway
Finland
Hungary
Croatia
Greece
Czech Republic
Poland