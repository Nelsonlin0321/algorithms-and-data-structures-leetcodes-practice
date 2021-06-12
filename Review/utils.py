import os
import random

codes_list = []

folder_list = [folder for folder in os.listdir("../") if '.' not in folder and folder != 'Review']
_ = [codes_list.extend(os.listdir(os.path.join("../", folder))) for folder in folder_list]


def random_question():
    return random.sample(codes_list, 1)[0]


if __name__ == '__main__':
    print(random_question())