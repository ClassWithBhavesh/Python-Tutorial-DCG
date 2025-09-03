# dictionary - collection of data but in the form of key & value pair

empData = [{
    "empId": 1001,
    "empName": "Aryan", 
    "empAge": 65,
    "empFavMovies": ["Captain America", "Endgame"],
    "empDOJ": "12-05-2025"
}, {
    "empId": 1002,
    "empName": "Harsh", 
    "empAge": 51,
    "empFavMovies": ["Black widow", "Endgame"]
}]

# dictionary methods 
# 1. .keys()
print(empData[0].keys())

# 2.values()
print(empData[1].values())

# 3. .get()
print(empData[1].get("empAge"))

# 4. .items()
print(empData[1])
print(empData[1].items())




# print("Harsh is our 2nd employee and his fav movies are Black Widow & Endgame")
# print(empData[1]["empName"] + " is our 2nd employee and his fav movies are " + empData[1]["empFavMovies"][0] + " & " + empData[1]["empFavMovies"][1])
# print(empData[1]["empFavMovies"])
# print(type(empData))

