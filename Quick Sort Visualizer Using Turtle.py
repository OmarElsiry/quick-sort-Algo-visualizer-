import turtle
import random
import time

#startup window
sc = turtle.Screen()
sc.setup(400, 300)
sc.bgcolor("Grey")

#specify number of cols
x=turtle.textinput(" ", "Enter cols number : ")

#main window
screen = turtle.Screen()
screen.setup(800,800)
screen.tracer(0,0)
screen.title('Quick Sort visualizing')

turtle.speed(0)
turtle.hideturtle()
turtle.screensize(800,800,"Grey")

#main purpose is adding swipers to screen

#function to create cols
def draw_col(x,y,w,h):
    turtle.up();turtle.goto(x,y);turtle.seth(0);turtle.down()
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

#Function to fill cols
def draw_cols(u,n,current_i=-1,current_j=-1):
    turtle.clear()
    #making window size fit with cols number
    x = -400
    w = 800/n
    
    # red for i , cyan for j
    for i in range(n):
        if i == current_i:
            turtle.fillcolor('red')
        elif i == current_j:
            turtle.fillcolor('Cyan')
        else:
            turtle.fillcolor('Orange')
        draw_col(x,-400,w,u[i])
        x =x+ w
    
    #update screen continously
    screen.update()

#Hoare Partition Function
def partition(u,x,y):
    p = random.randint(x,y)
    u[p], u[y] = u[y], u[p]
    pivot = u[y]
    i, j = x, y-1
    while i <= j:
        while u[i] <= pivot and i <= j:
            draw_cols(u,n,i,j)
            i += 1
        while u[j] > pivot and j >= i:
            draw_cols(u,n,i,j)
            j =j - 1
        if i < j:
            draw_cols(u,n,i,j)
            u[i], u[j] = u[j], u[i]
    u[i], u[y] = u[y], u[i]
    draw_cols(u,n,i,y)
    return i

#Create quick sorting function
def quick_sort(u,x,y):
    if x >= y:
        return
    m = partition(u,x,y)
    quick_sort(u,x,m-1)
    quick_sort(u,m+1,y)

#number of cols = number enterd in the textbox
n = int(x)
u = [0] * n
for i in range(n):
    u[i] = random.randint(1,800)

#recalls
t1 = time.time()
quick_sort(u,0,n-1)
turtle.clear()
draw_cols(u,n,-1)
turtle.update()
t2 = time.time()

#Print time complexity & elapsed time in terminal
print('elapsed time=', t2-t1)
print("time complexity = O(n*log(n))")

# Print time complexity & elapsed time in window
time.sleep(1.5)
turtle.clearscreen()
turtle.bgcolor("black")
turtle.hideturtle()
turtle.penup()
turtle.pencolor("orange")
turtle.pensize(15)
turtle.goto(-140, 200)
turtle.write('elapsed time = ', align="center", font=("Arial", 24, "normal"))
turtle.goto(140, 200)
turtle.write(t2 - t1, align="center", font=("Arial", 24, "normal"))
turtle.goto(-190, 140)
turtle.write("time complexity = O(n*log(n))", font=("", 24, "normal"))

#Team_mates
turtle.goto(-80, 0)
time.sleep(2)
turtle.write("S.D Team", font=("Times new roman", 28, "normal"))
turtle.done()

