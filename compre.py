count = {"books": 100, "pot": 150, "pen": 120}
count_stock = {items: com * 2 for items, com in count.items()}
print(count_stock)