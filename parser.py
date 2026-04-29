def parse_input(user_input):
    user_input = user_input.lower()

    parsed = {
        "conditions": []
    }

    # GREATER THAN
    if "greater than" in user_input:
        value = user_input.split("greater than")[1].strip().split()[0]
        if "salary" in user_input:
            parsed["conditions"].append(f"salary > {value}")
        elif "age" in user_input:
            parsed["conditions"].append(f"age > {value}")

    # LESS THAN
    if "less than" in user_input:
        value = user_input.split("less than")[1].strip().split()[0]
        if "salary" in user_input:
            parsed["conditions"].append(f"salary < {value}")
        elif "age" in user_input:
            parsed["conditions"].append(f"age < {value}")

    # DEPARTMENT
    if "department" in user_input:
        words = user_input.split()
        idx = words.index("department")
        dept = words[idx + 1]
        parsed["conditions"].append(f"department = '{dept.capitalize()}'")

    return parsed