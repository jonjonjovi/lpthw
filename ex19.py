def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")

print("We can just give a funcion directly")
cheese_and_crackers(20,30)
print("OR,we can use the function numbers directly:")
amount_of_cheese =10
amount_of_crackers=5

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)
