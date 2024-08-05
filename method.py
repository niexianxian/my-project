import json
import os
import re

class_pattern = re.compile(r'class\s+(\w+)\(([\w, ]+)\)')
scene_pattern = re.compile(r'self\.scene_name\s*=\s*["\']([^"\']+)["\']')


def get_name(py_files: str, results_dic: dict):
    if not (isinstance(py_files, str) or isinstance(results_dic, dict)):
        return

    with open(py_files, 'r', encoding='utf-8') as file:
        content = file.read()
    class_match = class_pattern.search(content)
    scene_match = scene_pattern.search(content)
    if class_match and scene_match:
        class_name = class_match.group(1)
        scene_name = scene_match.group(1)
        original_class_name = class_name
        counter = 1
        while class_name in results_dic:
            class_name = f'{original_class_name.split('-')[0]}-{counter}'
            counter += 1
        results_dic[class_name] = scene_name


def find_files(source_folder, results_dic):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                py_files = (os.path.join(root, file))
                get_name(py_files, results_dic)


def get_obj_class(init_obj: str, dic2: dict):
    if not (isinstance(init_obj, str) or isinstance(dic2, dict)):
        return
    if '_version' in init_obj:
        with open(init_obj, 'r', encoding='utf-8') as file:
            content = file.read()
            # for line in file:
            s = re.findall(r'(obj\d+)\s?=\s?(.+)\(', content)
            for obj_content, class_content in s:
                dic2[class_content] = obj_content


def main(lis: list):
    if not isinstance(lis, list):
        retrun

    results_dict = {}
    source_folder_pa = "D:/all_scene/all_scene"
    find_files(source_folder_pa, results_dict)

    with open('all-scene.json', 'w', encoding='utf-8') as json_file:
        json.dump(results_dict, json_file, ensure_ascii=False, indent=4)

    results_dict2 = {}
    init_obj_path = r"D:\all_scene\init_obj\hvdc_version.py"
    get_obj_class(init_obj_path, results_dict2)

    with open('single_version.json', 'w', encoding='utf-8') as json_file:
        json.dump(results_dict2, json_file, ensure_ascii=False, indent=4)

    scene_to_obj = {}
    for class_part, obj_part in results_dict2.items():
        scene_newname = results_dict[class_part]
        scene_to_obj[scene_newname] = obj_part
    obj_list = []
    for scene in lis:
        obj_newname = scene_to_obj[scene]
        obj_list.append(obj_newname)
    return obj_list


if __name__ == "__main__":
    lis1 = ['IT方仓UPS单体电池即将失压', 'IT方仓UPS单体电池温度异常']
    obj_lis = main(lis1)
    print(obj_lis)
