#
#
# class Solution(object):
#     def next_passcode(self,passcode,idx):
#         pass_list  = []
#         pos = passcode[idx]
#         if pos == '9':
#             new_pass_code = '0' + pass_code[pos_idx + 1:]
#
#     def openLock(self, deadends, target):
#         """
#         :type deadends: List[str]
#         :type target: str
#         :rtype: int
#         """
#
#         queque = ["0000"]
#
#         while len(queque) != 0:
#             size = len(queque)
#             for idx in range(size):
#                 pass_code = queque[idx]
#                 # breath function
#                 for pos_idx in range(4):
#                     pos = pass_code[pos_idx]
#                     if pos == '9':
#                         # add
#                         new_pass_code = '0' + pass_code[pos_idx + 1:]
#                         if new_pass_code not in deadends:
#                             queque.append(new_pass_code)
#                         new_pass_code = '8' + pass_code[pos_idx + 1:]
#                         if new_pass_code not in deadends:
#                             queque.append(new_pass_code)
#                     elif pos == '0':
#                         new_pass_code = '9' + pass_code[pos_idx + 1:]
#                         if new_pass_code not in deadends:
#                             queque.append(new_pass_code)
#                         new_pass_code = '1' + pass_code[pos_idx + 1:]
#                         if new_pass_code not in deadends:
#                             queque.append(new_pass_code)
#                     else:
#
#
#
# if __name__ == "__main__":
#     pass
