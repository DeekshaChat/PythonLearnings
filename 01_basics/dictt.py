chai_types = {"Masala" : "Spicy", "Ginger": "Zesty","Green":"Mild"}
# print(chai_types)
# print(chai_types["Masala"])
# print(chai_types["Masalaa"]) # KeyError
# print(chai_types.get("Masalaa")) # None - it will not give error

# for chai in chai_types:
#     print(chai)

# for chai in chai_types:
#     print(chai_types[chai])

# for key,value in chai_types.items():
#     print(key, value)

# val = chai_types.pop("Masala")
# print(val)
# print(chai_types)

val = chai_types.popitem()
print(val)
print(chai_types)