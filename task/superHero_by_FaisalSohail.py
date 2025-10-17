# **** Superhero Team Formation System Solved by Faisal Sohail****

# 1. Create and initialize Superhero List:

superheroes = [
    ("Superman", 100, "DC", 5.0),
    ("Iron Man", 85, "Marvel", 4.7),
    ("Wonder Woman", 90, "DC", 4.9),
    ("Hulk", 95, "Marvel", 4.8)
]

new_hero = ("SpiderMan", 88, "Marvel", 4.6)
superheroes.append(new_hero)
print(superheroes)

# 2. Filter Superheroes by Power Level
max_power = max(superheroes, key=lambda hero: hero[1])
print("Most Powerful Superhero:", max_power[0], "with Power Level:", max_power[1])

# 3. Sort superheroes by rating in descending order
sorted_heroes = sorted(superheroes, key=lambda hero: hero[3], reverse=True)
print("Heroes sorted by rating (high to low):")
print(sorted_heroes)


# 4. Calculate team statistics
total_power = sum(map(lambda hero: hero[1], superheroes))
average_rating = sum(map(lambda hero: hero[3], superheroes)) / len(superheroes)

# 5. remove a superhero by name
print("Total Power Level:", total_power)
print("Average Rating:", round(average_rating, 2))
name_to_remove = input("Enter the superhero name to remove: ")
superheroes = tuple(filter(lambda hero: hero[0] != name_to_remove, superheroes))
print("Updated Superheroes List:", superheroes)


# 6. Add a new superhero user input
new_hero = (
    input("Enter name: "),
    int(input("Enter power level: ")),
    input("Enter universe: "),
    float(input("Enter rating: "))
)
superheroes = superheroes + (new_hero,)
print("After adding new hero:", superheroes)

# 7 Display the Final Team
hero_set = set(map(lambda hero: hero[0], superheroes))
print("Initial Set:", hero_set)
hero_set.add(new_hero[0])
print("Is Flash in set?", "Flash" in hero_set)
print("Updated Set:", hero_set)
