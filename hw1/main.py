from pathlib import Path


def total_salary(path):
    salaries = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            file.seek(0)
            for line in file.readlines():
                line = line.split(",")
                salary = float(line[1].strip())
                salaries.append(salary)
            total = sum(salaries)
            try:
                average = total / len(salaries)
                return total, average
            except ZeroDivisionError:
                return None
    except FileNotFoundError:
        return None


try:
    total, average = total_salary("monthly_salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print("File is not found")