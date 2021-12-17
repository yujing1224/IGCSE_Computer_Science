#dictionaries or hashmaps have fast lookup due to how they're stored in memory {}

#create a dictionary (key-value pairs) aka "Hashmap, Map, HashTable"
assignment_scores = { "Angelina": 90, "Barbie":90, "Yujing":100, "Rola":95 }
yujing_assignment_score = assignment_scores.get("Yujing")
print("Yujing assignment score", yujing_assignment_score)

#create a dictionary using built in dict function (same thing, different way to write it)
exam_scores = dict(Howard=95, Amy=90, Rain=85)
amy_score = exam_scores.get("Amy")
print("Amy's exam score", amy_score)

#iterate the keys in the dicitonary (traverse through dictionary)
for key in exam_scores:
    print(key)

#remove method - pop
exam_score_removed = exam_scores.pop("Howard")
print(exam_score_removed)
print(exam_scores)