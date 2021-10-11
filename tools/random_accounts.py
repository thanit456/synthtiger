import random 
from tqdm import tqdm

ten_digits_formats = [
    # 10 digits 
    '{}{}{}{}{}{}{}{}{}{}',
    '{}{}{}-{}-{}{}{}{}{}-{}',
    '{}{}-{}{}{}{}-{}{}{}{}',
    '{}{}{}-{}{}{}-{}{}{}{}',
    '{}{}{}{}-{}{}-{}{}-{}{}',
    '{}{}{}-{}{}{}-{}{}{}-{}',
    '{}{}{}-{}{}{}{}-{}{}{}',
]
twelve_digits_formats = [
    # 12 digits
    '{}{}{}{}{}{}{}{}{}{}{}{}',
    '{}{}-{}{}{}-{}{}{}{}{}{}-{}',
    '{}{}{}-{}{}{}{}-{}{}{}{}-{}',
    '{}{}{}-{}{}{}{}{}{}{}{}-{}'
]
thirteen_digits_formats = [
    # promptpay (13 digits)
    '{}-{}{}{}{}-{}{}{}{}{}-{}{}-{}',
    '{}{}{}{}{}{}{}{}{}{}{}{}{}'
]
num_ten_digits = 100000
num_twelve_digits = 100000
num_thirteen_digits = 100000

with open('my_resources/corpus/account.txt', 'w') as f:
    for i in tqdm(range(num_ten_digits)):
        current_num = [random.randint(1, 10) for _ in range(10)]
        current_string = ten_digits_formats[random.randint(0, len(ten_digits_formats)-1)].format(*current_num)
        f.write(f'{current_string}\n')
    for i in tqdm(range(num_twelve_digits)):
        current_num = [random.randint(1, 10) for _ in range(12)]
        current_string = twelve_digits_formats[random.randint(0, len(twelve_digits_formats)-1)].format(*current_num)
        f.write(f'{current_string}\n')
    for i in tqdm(range(num_thirteen_digits)):
        current_num = [random.randint(1, 10) for _ in range(13)]
        current_string = thirteen_digits_formats[random.randint(0, len(thirteen_digits_formats)-1)].format(*current_num)
        f.write(f'{current_string}\n')
print('Successfully generated accounts')