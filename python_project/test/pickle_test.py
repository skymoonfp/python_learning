import os
import pickle

a = 123
b = 234
c = 345
d = 456
with open("ceshi.pk", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)
    pickle.dump(d, f)

# e = 5
# g = 6
# with open("ceshi.pk", "rb+") as f:
#     print(pickle.load(f))
#     pickle.dump(e, f)
#     print(pickle.load(f))
#     print(pickle.load(f))
#     pickle.dump(g, f)

e = 567
g = 678
size = os.path.getsize("ceshi.pk")
print(size)
mark = []
with open("ceshi.txt", "rb+") as f:
    while 0 < size:
        size = size - 1
        f.seek(size)  # 指向文件最后一个字节
        try:
            print(pickle.load(f))
            print(f.tell())
        except Exception:  # 无法load时退一个字节，继续尝试load
            continue
        else:  # load成功时，
            mark.append(size)
    print(mark)
    # f.seek(16)
    # print(pickle.load(f))
    # pickle.dump(e, f)
# 结论：（1）每个load有两个位置可以成功读取，其他位置不可读
# （2）每次load完，自动跳到下一个load对象的开始位置
# （3）在指定位置写入，会覆盖当前位置的load对象，并且，如果新load的对象的原load对象长度不匹配时，会造成之后的所有load对象无法读取


print("")

with open("ceshi.txt", "rb") as f:
    while True:
        try:
            a = pickle.load(f)
        except:
            break
    a = pickle.load(f)
print(a)
