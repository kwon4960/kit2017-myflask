import json
def set_charact(name):
    character = {
        "name": name,
        "level": 1,
        "hp": 100,
        "items": ["전기충격기", "야구방망이", "휴대폰"],
        "skill": ["이단돌려차기", "니킥", "뒤돌려차기"]
    }
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    #print("{0}님 반갑습니다. (HP {1})으로 게임을 시작 합니다.".format(character["name"], character["hp"]))
    return character

    def save_game(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in character:
        print("%s:%s" % (key, character[key]))
        f.write("%s:%s\n" % (key, character[key]))
    f.close()   