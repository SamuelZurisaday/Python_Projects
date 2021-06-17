def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Samuel Zurisaday", "lastname": "Rivera Bravo"}

    super_list = [
    {"firstname": "Samuel Zurisaday", "lastname": "Rivera Bravo"},
    {"firstname": "Olga Hanai", "lastname": "Mendoza Gallo"},
    {"firstname": "Romina Betsabé", "lastname": "Rivera Mendoza"},
    {"firstname": "Renata Abigaíl", "lastname": "Rivera Mendoza"},
    {"firstname": "Ian Zurisaday", "lastname": "Rivera Mendoza"}
     ]

    super_dict = {
    "natural_nums": [1,2,3,4,5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.43]
     }

    for key, value in super_dict.items():
    print(key, " - " , value)

if __name__ == '__main__':
    run()