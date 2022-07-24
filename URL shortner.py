import pyshorteners   
# install pyshorteners library
# pip install pyshorteners
# pyshorteners==1.0.1


print("Hello and welcome to Amar's terminal for URL shortening! \n")

#Asking for Long URL input
long_link = input("Please enter the link you would like to shorten: ") 

#using pyshorteners package
pyshort = pyshorteners.Shortener()
short_link = pyshort.tinyurl.short(long_link)

#Shortened Url displayed.
print("The shortened URL is: " + short_link) 


# Amar Kumar (github@Amar985)