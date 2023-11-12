import pkg.modu as m

def askforCoordinate(CoordinateName: str):
    resp = []

    while len(resp) != 2:
        inputStr = input(f'請輸入頂點 {CoordinateName} 的座標:')
        inputStr = inputStr.replace(' ', '')

        resp = inputStr.split(',')
        resp = list(map(float, resp))

    return tuple(resp)

CoordinatA = askforCoordinate('a')
CoordinatB = askforCoordinate('b')
CoordinatC = askforCoordinate('c')

print(m.triangle_zhonxin(CoordinatA, CoordinatB, CoordinatC))
