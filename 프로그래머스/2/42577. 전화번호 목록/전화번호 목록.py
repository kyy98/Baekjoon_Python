phone_book = ["119", "97674223", "1195524421"]

# def solution(phone_book):
#     dic = dict(zip([len(i) for i in phone_book],phone_book))
#     smallest_len = min(dic.keys())
#     phone_book.remove(dic[smallest_len])
#     for i in phone_book:
#         if dic[smallest_len] in i[:smallest_len]:
#             return False
#         else:
#             return True
# solution(phone_book)
def solution(phone_book):
    phone_book.sort()  
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True    