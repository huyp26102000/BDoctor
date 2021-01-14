import hashlib
# class DoctorAccount:
#     ID = None
#     Username = None
#     Password = None
#     def __init__(self, Username, Password):
#         self.Username



string_to_hash = '123'
hash_object = hashlib.sha256(str(string_to_hash).encode('utf-8'))
print('Hash', hash_object.hexdigest())