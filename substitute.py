import argparse
import json



def solution(input_dict, depth=float('inf')):
    depth -= 1
    if depth <= 0:
        return  
    for k, v in input_dict.items():
        if type(v) is not dict:
            input_dict[k] = {'_content': v, '_type': str(type(v))}
        else:
            solution(v)
    return input_dict





if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--file-name")
    parser.add_argument("--depth")
    parser.add_argument("--output-file")
    args = parser.parse_args()

    # open the json file and convert it to a dict
    json_file = args.file_name 
    f = open(json_file)
    input_dict = json.load(f)


    if args.depth:
        depth = int(args.depth)
        ans = solution(input_dict, depth)
    else:
        ans = solution(input_dict)

    # load the putput dict to json file
    with open(args.output_file, "w") as f:
        json.dump(ans, f)

