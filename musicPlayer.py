import json


def prompt(message):
    return input(message)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


play_list = read_json_file('./playList.json')
print(play_list)
recent = read_json_file('./recent.json')

if not play_list.get("0"):
    length_of_playlist = prompt("How many songs do you want in your playlist ? : ")
    try:
        intex = int(length_of_playlist)
    except ValueError:
        print("Please rerun the code and enter the number but not any string")
    else:
        pp = {}
        for i in range(intex):
            song = prompt(f"there are {i} songs in your playlist , which song you want on position {i + 1} : ")
            pp[str(i)] = song

        write_json_file("./playList.json", pp)
        print('Your playlist is Ready congrats!!')
        print(pp)
else:
    print("Give the key of song you want to play")
    number = input()
    print(play_list.get(number))
    print(number)

    if not play_list.get(number):
        print("Sorry no such key found")
    else:
        print("Playing", play_list.get(number))

        if recent.get("1"):
            recent["2"] = recent["1"]
            recent["1"] = recent["0"]
            recent["0"] = play_list.get(number)
        elif recent.get("0"):
            recent["1"] = recent["0"]
            recent["0"] = play_list.get(number)
        else:
            recent["0"] = play_list.get(number)

        write_json_file("./recent.json", recent)
        print("Here is your recent list", recent)
