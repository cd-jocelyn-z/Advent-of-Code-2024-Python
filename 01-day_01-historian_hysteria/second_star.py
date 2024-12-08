import os
from collections import Counter

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

similarity_score = []
counter = Counter(right_list)
score = 0
for left_nb in left_list:
    left_nb_occ = counter[left_nb]
    product = left_nb * left_nb_occ
    score += product
    similarity_score.append(score)
    score = 0

res = sum(similarity_score)
print(res)




