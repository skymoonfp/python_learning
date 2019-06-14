import turtle


def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1500, 600, 0, 0)
    pythonsize = float(size)
    turtle.pensize(pythonsize)
    turtle.pencolor(color)
    angleSet = float(angle)
    turtle.seth(float(direction) - angleSet / 2)
    radSet = float(rad)
    numSet = int(num)
    drawSnake(radSet, angleSet, numSet, pythonsize / 2)


size = input('输入小蛇的宽度：')
color = input('输入小蛇的颜色：')
direction = input('输入小蛇前进的坐标系方向：')
rad = input('输入小蛇爬行的弧度半径：')
angle = input('输入小蛇爬行的弧度大小：')
num = input('输入小蛇爬行的弧度个数：')

main()
