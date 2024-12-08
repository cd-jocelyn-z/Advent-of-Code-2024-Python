import os

file_name = "source.txt"
text_file = os.path.join(os.getcwd(),file_name )

left_list = []
right_list = []
with open(text_file,"r") as f:
    content = f.readlines()

    for line in content:
        num_pair = line.split()
        left_list.append(int(num_pair[0]))
        right_list.append(int(num_pair[1]))


left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

difference_list = []

for idx in range(len(left_sorted)):
    differnce = abs(left_sorted[idx] - right_sorted[idx])
    difference_list.append(differnce)

total_distance = sum(difference_list)
print(total_distance)


