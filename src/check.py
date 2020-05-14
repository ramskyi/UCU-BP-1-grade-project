import re
import matplotlib.pyplot as plt

#
# def add_line_to_dict(line, dct, index1_type, index2_type):
#     pattern = re.compile('\([^:]*, [^:]*\): \d*')
#     data = re.findall(pattern, line)
#     for item in data:
#         raw_index, value = item.split(': ')
#         value = int(value)
#
#         pattern1 = re.compile('\([^,]*,')
#         index1 = re.findall(pattern1, raw_index)[0][1: -1]
#
#         pattern2 = re.compile(', .*\)')
#         raw_index2 = re.findall(pattern2, raw_index)[0][2: -1]
#
#         index2, i, length = [], 0, len(raw_index2)
#         while i < length and raw_index2[i] not in ',(':
#             index2.append(raw_index2[i])
#             i += 1
#         while raw_index2[-1] in ' ,()':
#             del raw_index2[-1]
#         index2 = ''.join(raw_index2)
#
#         if index1_type is str:
#             index1 = index1[1: -1]
#         if index2_type is str:
#             index2 = index2[1: -1]
#             if index2.endswith(' Metal'):
#                 index2 = index2[0: -6]
#         index1 = index1_type(index1)
#         index2 = index2_type(index2)
#
#         index = index1, index2
#         if index not in dct:
#             dct[index] = 0
#         dct[index] += value
#
#     return dct
#
#
# stat_genre = {}
# genre_dct = {}
#
# with open('status_result', 'r') as file:
#     lines = file.readlines()
#     add_line_to_dict(lines[0], stat_genre, str, str)
#     total = 0
#     for item in stat_genre:
#         if item[1] not in genre_dct:
#             genre_dct[item[1]] = 0
#         genre_dct[item[1]] += stat_genre[item]
#         total += stat_genre[item]
#     print(total)
#     diff = set()
#     for item in genre_dct:
#         if genre_dct[item] >= 50:
#             diff.add(item)
#     print(diff)
#     print(len(diff))
#     # diff = set()
#     # for item in stat_genre:
#     #     diff.add(item[0])
#     # print(diff)


plt.bar(['a', 'b', 'c', 'd'], [1, 2, 3, 5])
# plt.bar([1, 2, 3, 4], ['g', 'w', 'a', 'cd'])
plt.show()