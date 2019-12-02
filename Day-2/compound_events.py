X = {"Red":4/7, "Black":3/7}
Y = {"Red":5/9, "Black":4/9}
Z = {"Red":4/8, "Black":4/8}
#A ball is drawn from each urn
first_case = X["Red"] * Y["Red"] * Z["Black"]
second_case = X["Red"] * Y["Black"] * Z["Red"]
third_case = X["Black"] * Y["Red"] * Z["Red"]

print(first_case + second_case + third_case)