'''A script to practice looping over lists and using the enumerate function.
2025-05-13 EJS'''

movies = ["Scent of a Woman",
          "Lord of the Rings",
          "Prince of Persia",
          "101 Dalmations",
          "Honor Among Thieves"]

for i, title in enumerate(movies, start=1):
    print(f"Movie {i}: {title}")