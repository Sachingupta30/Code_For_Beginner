# take input from user and print dict with seperated line....

user = {}
name = input("what is your name : ")
age = input("what is your age : ")
fav_movies = input("your fav movies seperated by comma : ").split(',')
fav_songs = input("your fav songs seperated by comma : ").split(",")

user["name"] = name
user["age"] = age
user["fav_movies"] = fav_movies
user["fav_songs"] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")