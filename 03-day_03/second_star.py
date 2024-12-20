import os, re
def mult(file_path):

    file = os.path.join(os.getcwd(), file_path)
    with open(file, 'r') as f:
        content = f.read().replace("\n", "")

        pattern = r'(mul)\((\d+),(\d+)\)'
        pattern_delete = r'don\'t\(\).*?(do\(\)|$)'

        cleaned_content = re.sub(pattern_delete, '', content)
        matches = re.findall(pattern, cleaned_content)

        products = []
        for item in matches:
            num1, num2 = int(item[1]), int(item[2])
            product = num1 * num2
            products.append(product)

        result = sum(products)
        return result

file_name = "source.txt"
res = mult(file_name)
print("Final Result:", res)