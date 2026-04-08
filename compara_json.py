import json
from deepdiff import DeepDiff

json_a = {"nome": "Ana", "idade": 30, "habilidades": ["Python", "Data"]}

json_b = {"nome": "Ana", "idade": 31, "habilidades": ["Python", "Data"]}


def compara_jsons(input1, input2):
    str1 = json.dumps(input1, ensure_ascii=False)
    str2 = json.dumps(input2, ensure_ascii=False)

    data1 = json.loads(str1)
    data2 = json.loads(str2)

    if data1 == data2:
        print("json iguais")
    else:

        diff = DeepDiff(data1, data2, ignore_order=True)
        if not diff:
            print("JSONs são logicamente iguais (mesmo com ordens diferentes).")
        else:
            print("jsons Diferentes:")
            print(diff.to_json(indent=2))

if __name__ == '__main__':
    compara_jsons(json_a, json_b)
