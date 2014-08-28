languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x : x == "Python", languages)

squares = [x**2 for x in range(1, 11)]
print filter(lambda s: s >= 30 and s <= 70, squares)
