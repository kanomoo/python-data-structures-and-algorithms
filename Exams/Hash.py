#  https://share.gemini.google/SJXI2wdwjceD
#  https://share.gemini.google/v6raXDvrr0Tp

def hash(key, table_size):
    hash_val = 0
    for char in key:
        hash_val += ord(char)
        print(f"-{ord(char)}")
    return hash_val % table_size

if __name__ == "__main__":
    print(hash("AB" , 10))
