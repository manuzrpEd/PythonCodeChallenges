# def first_unique_product(products):
#     if len(products) == 1:
#         return products[0]
#     elif products == []:
#         return None
#     for i in products:
#         if products.count(i) == 1:
#             return i
#     return None
#     pass

# if __name__ == "__main__":
#     print(first_unique_product(["Apple", "Computer", "Apple", "Bag"])) #should print "Computer"

# https://stackoverflow.com/questions/18767385/python-first-unique-number-in-a-list
def first_unique_product(products):
    counts = {}

    for item in products:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in products:
        if counts[item] == 1:
            return item

    return None
    pass

if __name__ == "__main__":
    print(first_unique_product(["Apple", "Computer", "Apple", "Bag"])) #should print "Computer"