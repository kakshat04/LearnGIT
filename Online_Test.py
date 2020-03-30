# Q1
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        scoop_lst = []
        if not isinstance(self.ingredients, list):
            return "Input data is not valid"

        for ingredient in self.ingredients:
            for topping in self.toppings:
                scoop_lst.append([ingredient, topping])

        return scoop_lst


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


# Q2
def group_by_owners(files):
    new_dict = {}
    file_lst = []

    for file, name in files.items():
        print(name, new_dict.keys())
        if name not in new_dict.keys():
            print("*****")
            file_lst = []
            file_lst.append(file)
            new_dict[name] = file_lst
            print(new_dict)
        else:
            print("####")
            file_lst = new_dict[name]
            file_lst.append(file)
            new_dict[name] = file_lst
            print(new_dict)
    return new_dict


if __name__ == "__main__":
    files = { 'Input.txt': 'Randy', 'Code.py': 'Stan','Output.txt': 'Randy'}
    print(group_by_owners(files))


def unique_names(names1, names2):
    if not isinstance(names1, list) or not isinstance(names2, list):
        raise TypeError

    return list(set(names1 + names2))


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia