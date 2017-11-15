
print('hello', 'world')
name = 'zhangsan'
# name = input('input your name:')
print('hello %s' % name)

print(1.7 * 2)
print(10 / 3, 10 // 3, 10 % 3)
print(False)
print(None)


l = [1, '1', 'a', 'python3', 4.23, False]
print('长度:', len(l))
print('原始:', l)
l.append('被追加的')
l.insert(1, '被插入的')
l[2] = '被替换的'
print('修改:', l)
l.pop()
l.pop(1)
print('删除:', l)

t = (1, 2, 3, 'abc')
print(t)
print(type(t))

age = 18
if age < 18:
    print('未成年')
elif age < 30:
    print('小青年')
else:
    print('小老头')

for e in l:
    print(e)

i = 0
while i < len(l):
    print(l[i])
    i += 1

d = {'name': 'zhangsan', 'age': 18, 'gender': 1}
print(d)
print(d['name'])
try:
    print(d['name1'])
except KeyError:
    print('d["name1"]不存在就报错')
print(d.get('age'))
print('d.get("age1")不存在就返回', d.get('age1'))
print('d.get("age1, -1")不存在就返回指定值', d.get('age1', -1))
print('判断aaa是否存在', 'aaa' in d)
try:
    d.pop('aaa')
except KeyError:
    print('d.pop("aaa")删除不存在的key就报错')



