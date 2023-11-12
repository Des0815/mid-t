from pkg import triangle_zhonxin

print("請輸入三角形的3個頂點坐標")
print("--------------------------------------")

A = tuple(input("請輸入頂點a的坐標:").split(','))
B = tuple(input("請輸入頂點b的坐標:").split(','))
C = tuple(input("請輸入頂點c的坐標:").split(','))

print("--------------------------------------")

XY = triangle_zhonxin(A, B, C)
print(f'此三角形重心為: {XY[0]}, {XY[1]}')
