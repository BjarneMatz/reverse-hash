import hashlib
import timeit


def main():
    with open("data", "rt") as file:
        count = 0
        for line in file:
            count = count + 1
            print("-----------------------------------------------------")
            print(f"Line {count}")
            print("")
            possible_hashes = define_hashes()
            hash_values(possible_hashes, line)
            print("")


def define_hashes():
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()
    md5 = hashlib.md5()
    possible_hashes = [sha1, sha224, sha256, sha384, sha512, md5]

    return possible_hashes


def hash_values(hash_methods, data):
    data = data.replace("\n", "")
    print(data)
    hashes = [data]
    data = data.encode("utf-8")
    for x in hash_methods:
        x.update(data)
        print(f"{x.name} : {x.hexdigest()}")
        hashes.append(x.hexdigest())
    print("all hashes generated")


if __name__ == "__main__":
    main()

'''
# measure execution time of generating one set of hashes
a = []

for x in range(100):
    time = timeit.timeit(maincode)
    print(f"execution time: {time}s")
    a.append(time)

average = sum(a)/len(a)
print(f"average execution time: {average}s")
'''
