import json


with open('input_completion_mark.json') as json_file:
    data = json.load(json_file)
if __name__ == '__main__':
    print(data['password'])
    # test minimum attempt
