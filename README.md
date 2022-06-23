# Talabat_WebScraper
A web scraper for the details and menu of various restaurants featured on talabat.com

Files: 
Input:
sample_data.json: Existing sample restaurant url links which need to be scraped 

my_data.json: Some more restaurant url links, which contain unique issues, to imply the robustness of the scraper

menu.json: Stores the json file obtained after sending HTTP GET request (contains all the dynamic data relevant to the website)

Output:
Restaurant.json : Stores the details of the restaurants (First 5 are from sample_data, next 5 are from my_data.json)

menu_list.json: Stores the menu details of all the restaurants, in the data file. Each restaurant has 4 parameters: Menu Items, Items description, Price(in AED), Item image.

cms_scrape.csv: CSV file which contains the restaurant details, for both sample data and experimental data, grouped together

menu_list.csv: CSV file which contains the menu details for sample data restaurants.
menu_list_new.csv: CSV file containing menu details for experimental data restaurants.



Note: If some item does not have a description or a price, it is saved as "". An item without an image has its url saved as null. 



