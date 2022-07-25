import hashlib

static_trail = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

bUsername_trial = b"GOUGH"

arr = [4, 5, 3, 6, 2, 7, 1, 8]
s = ""
for i in arr:
    s = s + hashlib.sha256(bUsername_trial).hexdigest()[i]

static_trail = static_trail + s + key_part_static2_trial

print(static_trail)
