"""merge the tools using python (hackerrank)"""
'''method 1'''

# def merge_the_tools(string, k):
#     # your code goes here
#     for i in range(0,len(string),k):
#         t = string[i: i+k]
#         u = list(dict.fromkeys(t))
#         print("".join(u))
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

'''method 2'''

# def merge_the_tools(string, k):
#     occur = set()
#     for i in range(len(string)):
#         occur.add(string[i])
#         if (i+1) % k == 0:
#             print(''.join(occur))
#             occur = set()

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

'''method 3'''

# def merge_the_tools(string, k):
#     # your code goes here
#     result = ''
#     results = []
#     if len(string) % k != 0:
#         print("Invalid")
#     else:
#         for i in range(1, len(string) + 1):
#             if i % k  == 0:
#                 for letter in string[i - k : i]:
#                     if letter not in result:
#                         result += letter
#                 results.append(result)
#                 result = ''
#     for res in results:
#         print(res)

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
