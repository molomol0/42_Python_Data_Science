ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Can modify list directly from the index
ft_list[1] = "World!"

# Can't add/remove/change anything so need to redifine
ft_tuple = ("Hello", "France!")

# Can't change directly so need the remove then add
# (discard so there are no error if tutu is not found)
ft_set.discard("tutu!")
ft_set.add("Paris!")

# Can directly change the value associated to the key Hello
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
