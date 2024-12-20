import os, re

def mult(file):
    with open(file) as f:
        content = f.read()
        pattern = r'(mul){1}\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\,([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)'
        matches = re.findall(pattern, content)

        products = []
        for item in matches:
            item = list(item)
            num1,num2 = item[1], item[2]
            product = int(num1) * int(num2)
            products.append(product)

        result = sum(products)
        return result

file_name = "source.txt"
file = os.path.join(os.getcwd(), file_name)
res = mult(file)
print(res)