count = {"books": 100, "pot": 150, "pen": 120}
count_stock = {items: com * 2 for items, com in count.items()}
print(count_stock)

messy_names = ["COME", "Go", "juMp", "do", "Do", "come", "Good"]
clean_messed = {messed.lower() for messed in messy_names}
print(clean_messed)
print()

leager = [100.00, 12.45, 90.53, 50.00, 60.46]
cash_back_reward = [charge * 0.01 for charge in leager if charge > 50.00]
print(cash_back_reward)