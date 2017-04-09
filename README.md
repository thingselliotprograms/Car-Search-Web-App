# Car-Search-Web-App
Cars Query is a website that allows the user look up new vehicle information, either searching by car maker, or sorting cars by criteria, like horsepower, mpg, price, etc. A unique feature of the site is allowing a user to search based on the weight of multiple criteria, for example cars with high horsepower and low price. If all you care about are the extremes, this is the car search site for you.

Backend is a MySQL database, built using data from the Edmunds Vehicle API. Data is queried using SQLAlchemy and MySQLdb, the mysql-connector package for python.
Server App is written in Python using the Flask web framework.
