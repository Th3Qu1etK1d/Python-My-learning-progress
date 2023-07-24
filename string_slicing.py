# slicing = create a substring by extracting elements from another string
#                indexing[] or slice()
#                [start:stop:step]

name = "Hugo Pelletier"

first_name = name[0:4]
last_name = name[6:8]
funky_name = name[0:9:2]
reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

website = "https://github.com/Th3Qu1etK1d"

slice = slice(19, -1)


print(website[slice])