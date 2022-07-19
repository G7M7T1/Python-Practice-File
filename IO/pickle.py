import pickle

# Write Pickle FIle Here ---------------------
number = 10
text = "Here is new text"
new_list = [1, 3, 5, 7, 9]


def save_data():
    global number, text, new_list
    data = {"number": number, "text": text, "new_list": new_list}
    with open("pickle_file", "wb") as p_file:
        pickle.dump(data, p_file)


save_data()

# Read Pickle FIle Here ---------------------

num = None
txt = None
lst = None


def restore_data():
    global num, txt, lst
    with open("pickle_file", "rb") as p_file:
        data = pickle.load(p_file)
        num = data["number"]
        txt = data["text"]
        lst = data["new_list"]


restore_data()
print(num, txt, lst)
