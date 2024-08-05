# 1. 写一个程序，输出100以内所有的奇数
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i, end=' ')


# 2. 写一个程序，求1到100的和
# todo 用匿名函数实现它
# sum = 0
# for i in range(101):
#     sum += i
# print('1到100的和为：', sum)

# s = lambda: range(101)
# result = sum(s())
# print(result)

# s = sum(range(101))
# print(s)


# # 3. 写一个程序，将一个列表中的元素按照大小重新排序
# 从大到小reverse = Ture
# n = [2, 1, 3, 4, 5, 7, 6, 10, 9, 8]
# n.sort()
# print(n)


# 4. 写一个程序，将两个列表合并成一个从小到大排序的列表
# a = [1, 3, 5, 7, 9]
# b = [2, 4, 6, 8, 10]
# c = sorted(a + b)
# print(c)


# 5. 写一个程序，找出两个列表中的相同元素
# a = [1, 3, 5, 8]
# b = [2, 3, 4, 8]
# c = set(a)
# d = set(b)
# e = c & d
# print('相同元素为：', e)


# 6. 写一个程序，找出两个列表中的不同元素
# a = [1, 2, 3, 4, 5]
# b = [1, 3, 5, 7, 8]
# c = set(a)
# d = set(b)
# e = c - d
# f = d - c
# g = e.union(f)
# print('不同元素为：', g)


# 7. 写一个程序，将一个列表中的元素去重
# lis = [1, 2, 3, 3, 4, 5, 5, 6, 6, 7]
# a = set(lis)
# b = list(a)
# print(b)


# 8. 写一个程序，生成一个随机数并将其逆序输出
# import random
#
# a = random.randint(1, 100)
# b = str(a)
# c = b[::-1]
# d = int(c)
# print('原始随机数：', a)
# print('逆序后的数字：', d)

# 9. 写一个程序，将一个字典中的键和值互换
# todo 用for循环
# dic1 = {'a': 1, 'b': 2, 'c': 3}
# dic2 = {value: key for key, value in dic1.items()}
# print(dic2)
# dic1 = {"a": 1, "b": 2, "c": 3}
# dic2 = {}
# for key, value in dic1.items():
#     dic2[value] = key
# print(dic2)

# 10. 写一个程序，将一个字符串中的所有字母大小写互换
# s = 'Hello World'
# s = s.swapcase()
# print(s)


# st = 'Hello World'
# st1 = ''
# for char in st:
#     if char.isupper():
#         st1 += char.lower()
#     elif char.islower():
#         st1 += char.upper()
#     else:
#         char += char
# print(st1)


# 11. 写一个程序，将一个字符串中的所有字母小写并去除空格
# s = 'HELLE WORLD'
# s = s.lower()
# s = s.replace(' ', '')
# print(s)


# 12. 写一个程序，输出100以内的所有偶数，直到累加和大于1000
# a = 0
# b = []
# for i in range(2, 101, 2):
#     a += i
#     b.append(i)
#     if a > 1000:
#         break
# print(b)


# def test_print():
#     s = 'Hello World'
#     s = s.swapcase()
#     print(s)
#
# def fuc2():
#     print("f2")
#
# # if __name__ == "__main__":
# #     # s = 'Hello World'
# #     # s = s.swapcase()
# #     # print(s)
# print("in test_print")
# test_print()
#
#
# print("fuc2")
# fuc2()
#
# print(__name__)


# import os
# import shutil
#
#
# def add_suffix_to_filename(src: str, suffix: str):
#     for root, dirs, files in os.walk(src):
#         for filename in files:
#             original_file_path = os.path.join(root, filename)
#             file_root, file_extension = os.path.splitext(filename)
#             new_filename = f'{file_root}{suffix}{file_extension}'
#             new_file_path = os.path.join(root, new_filename)
#             os.rename(original_file_path, new_file_path)
#             print('文件已重命名。')


# def add_suffix_to_filename(src: str, suffix: str):
#     if not (isinstance(src, str) and isinstance(suffix, str)):
#         print('入参错误，请重新调用。')
#         return
#     for filename in os.listdir(src):
#         file_path = os.path.join(src, filename)
#         if os.path.isfile(file_path):
#             file_root, file_extension = os.path.splitext(filename)
#             new_filename = f'{file_root}{suffix}{file_extension}'
#             new_file_path = os.path.join(src, new_filename)
#             os.rename(file_path, new_file_path)
#             print(f'文件{file_path}已重命名为{new_file_path}。')
#         elif os.path.isdir(file_path):
#             add_suffix_to_filename(file_path, suffix)


# def cut_and_paste(src: str, dst: str) -> None:
#     if not (isinstance(src, str) and isinstance(dst, str)):
#         print('入参错误，请重新调用。')
#         return
#
#     if not os.path.exists(src):
#         print(f'源目录{src}不存在。')
#         return
#     if not os.path.exists(dst):
#         os.makedirs(dst)
#         print(f'目标目录{dst}已创建。')
#
#     for item in os.listdir(src):
#
#         src_item = os.path.join(src, item)
#         dst_item = os.path.join(dst, item)
#
#         if os.path.isfile(src_item):
#
#             shutil.move(src_item, dst_item)
#             print(f'文件{src_item}已剪贴到{dst_item}.')
#         elif os.path.isdir(src_item):
#
#             cut_and_paste(src_item, dst_item)
#
#     if not os.listdir(src):
#         os.rmdir(src)
#         print(f'空目录{src}已被删除。')
#
#
# if __name__ == '__main__':
#     source_folder = "D:\文件夹A"
#     destination_folder = "D:\文件夹B"
#     suffix = 'niexian'
#
#     add_suffix_to_filename(source_folder, suffix)
#     cut_and_paste(source_folder, destination_folder)

from functools import reduce
def add(x, y):
    return x + y

s = print(reduce(add, [1, 2, 3, 4, 5]))




lis = ["a", "b", "c"]
print(len(lis))