# Talabat_WebScraper
A web scraper for the details and menu of various restaurants featured on talabat.com

Files: 
sample_data.json: Existing sample restaurant url links which need to be scraped 

my_data.json: Some more restaurant url links, which contain unique issues, to imply the robustness of the scraper

menu.json: Stores the json file obtained after sending HTTP GET request (contains all the dynamic data relevant to the website)

Restaurant.json : Stores the details of the restaurants

menu_list.json: Stores the menu details of all the restaurants, in the data file.

restaurant.csv: CSV file which contains the restaurant details, after data cleanup and some slight modifications

menu.csv: CSV file which contains the menu details, after being extracted from the json and arranged properly.


restaurant.json: First 5 are from sample_data, next 5 are from my_data.json
menu.json: Each restaurant has 4 parameters: Menu Items, Items description, Price(in AED), Item image. 
note: If some item does not have a description or a price, it is saved as "". An item without an image has its url saved as null. 



