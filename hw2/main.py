from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.strip().split(",")
                cat_id = line[0]
                cat_name = line[1]
                cat_age = line[2]
                infos = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age,
                    }
                cats_info.append(infos)
        return cats_info
    except FileNotFoundError:
        return None




try:
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
except TypeError:
    print("File is not found")