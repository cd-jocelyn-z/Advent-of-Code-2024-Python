import os

file_name = 'source.txt'
file = os.path.join(os.getcwd(), file_name)
with open(file, 'r') as file:
    reports = file.readlines()

def verify_safety(report):
    is_increasing = report[0] < report[1]
    for nb in range(1, len(report)):
        current_item = report[nb]
        previous_item = report[nb - 1]

        if current_item == previous_item:
            return False

        if is_increasing and previous_item > current_item:
            return False

        if not is_increasing and current_item > previous_item:
            return False

        distance = abs(current_item - previous_item)
        if distance < 1 or distance > 3:
            # return False
            return False

    return True

safe_counter = 0
for report in reports:
    nb_list = [int(x) for x in report.split()]
    print(nb_list)
    if verify_safety(nb_list):
        safe_counter+=1
    else:
        for nb in range(len(nb_list)):
            sub_list = nb_list[:nb] + nb_list[nb+1:]
            if verify_safety(sub_list):
                safe_counter+=1
                break

print(safe_counter)