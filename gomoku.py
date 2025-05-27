import tkinter
import tkinter.messagebox

stage_width=80#１マスの大きさ
num_stage_x=8
num_stage_y=8
player=1#先行が黒から



stage=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ]
record=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ]


#ステージ情報の初期化
#0が空いているマス、1が黒のマス、-1が白のマス

def check_click1():
    tkinter.messagebox.showinfo("情報を表示","勝者は黒です")
    root.destroy()
    #黒が勝った場合にメッセージを表示し、プログラムを終了

def check_click2():    
    tkinter.messagebox.showinfo("情報を表示","勝者は白です")
    root.destroy()
    #白が勝った場合にメッセージを表示し、プログラムを終了

def check_click3():    
    tkinter.messagebox.showinfo("情報を表示","引き分けです")
    root.destroy()
    #引き分け場合にメッセージを表示し、プログラムを終了

def turn_change():
    global player
    
    return -player
    #黒と白のターンを変更する

def record_stage():
    global stage,record
    for i in range(8):
        for j in range(8):
            record[j][i] = stage[j][i]
    #マスの石を記録する

def judge_Winner():
    global stage
    
    #縦のラインがそろっているか探索
    for i in range(8):
        if ((stage[3][i] == stage[4][i]) and stage[3][i] != 0):
            if ((stage[0][i] == stage[1][i] and stage[1][i] == stage[2][i]) and stage[0][i] == stage[3][i]) or ((stage[1][i] == stage[2][i] and stage[2][i] == stage[5][i]) and stage[1][i] == stage[3][i]) or ((stage[2][i] == stage[5][i] and stage[5][i] == stage[6][i]) and stage[2][i] == stage[3][i]) or ((stage[5][i] == stage[6][i] and stage[6][i] == stage[7][i]) and stage[5][i] == stage[3][i]):
                return stage[3][i]
 
    #横のラインがそろっているか探索
    for j in range(8):
        if ((stage[j][3] == stage[j][4]) and stage[j][3] != 0):
            if ((stage[j][0] == stage[j][1] and stage[j][1] == stage[j][2]) and stage[j][0] == stage[j][3]) or ((stage[j][1] == stage[j][2] and stage[j][2] == stage[j][5]) and stage[j][1] == stage[j][3]) or ((stage[j][2] == stage[j][5] and stage[j][5] == stage[j][6]) and stage[j][2] == stage[j][3]) or ((stage[j][5] == stage[j][6] and stage[j][6] == stage[j][7]) and stage[j][5] == stage[j][3]):
                return stage[j][3]
 
    #斜めのラインがそろっているか探索
    for i in range(4):
        for j in range(4):
            if ((stage[i][j] == stage[i+1][j+1] and stage[i+1][j+1] == stage[i+2][j+2] and stage[i+2][j+2] == stage[i+3][j+3] and stage[i+3][j+3] == stage[i+4][j+4]) and stage[i][j] != 0):
                return stage[i][j]
    for i in range(4):
        for j in range(4,8):
            if ((stage[i][j] == stage[i+1][j-1] and stage[i+1][j-1] == stage[i+2][j-2] and stage[i+2][j-2] == stage[i+3][j-3] and stage[i+3][j-3] == stage[i+4][j-4]) and stage[i][j] != 0):
                return stage[i][j]
            
    #空いているマスがあるか探索
    for i in range(8):
        for j in range(8):
            if stage[j][i] == 0:
                return 0
            
    #空いているマスがない時
    return -2

def put_stone(event):
    global stage,player,record
    

    if player == 1:
    #黒のターンの時
        if (event.x<=80 and event.y<=80) and stage[0][0] == 0:
            canvas.create_oval(0,0,80,80,fill="black")
            stage[0][0] = 1  
        elif ((80<event.x and event.x<=160) and event.y<=80) and stage[0][1] == 0:
            canvas.create_oval(80,0,160,80,fill="black")
            stage[0][1] = 1
        elif ((160<event.x and event.x<=240) and event.y<=80) and stage[0][2] == 0:
            canvas.create_oval(160,0,240,80,fill="black")
            stage[0][2] = 1
        elif ((240<event.x and event.x<=320) and event.y<=80) and stage[0][3] == 0:
            canvas.create_oval(240,0,320,80,fill="black")
            stage[0][3] = 1
        elif ((320<event.x and event.x<=400) and event.y<=80) and stage[0][4] == 0:
            canvas.create_oval(320,0,400,80,fill="black")
            stage[0][4] = 1
        elif ((400<event.x and event.x<=480) and event.y<=80) and stage[0][5] == 0:
            canvas.create_oval(400,0,480,80,fill="black")
            stage[0][5] = 1
        elif ((480<event.x and event.x<=560) and event.y<=80) and stage[0][6] == 0:
            canvas.create_oval(480,0,560,80,fill="black")
            stage[0][6] = 1
        elif ((560<event.x and event.x<=640) and event.y<=80) and stage[0][7] == 0:
            canvas.create_oval(560,0,640,80,fill="black")
            stage[0][7] = 1
        elif (event.x<=80 and (80<event.y and event.y<=160)) and stage[1][0] == 0:
            canvas.create_oval(0,80,80,160,fill="black")
            stage[1][0] = 1
        elif ((80<event.x and event.x<=160) and (80<event.y and event.y<=160)) and stage[1][1] == 0:
            canvas.create_oval(80,80,160,160,fill="black")
            stage[1][1] = 1
        elif ((160<event.x and event.x<=240) and (80<event.y and event.y<=160)) and stage[1][2] == 0:
            canvas.create_oval(160,80,240,160,fill="black")
            stage[1][2] = 1
        elif ((240<event.x and event.x<=320) and (80<event.y and event.y<=160)) and stage[1][3] == 0:
            canvas.create_oval(240,80,320,160,fill="black")
            stage[1][3] = 1
        elif ((320<event.x and event.x<=400) and (80<event.y and event.y<=160)) and stage[1][4] == 0:
            canvas.create_oval(320,80,400,160,fill="black")
            stage[1][4] = 1
        elif ((400<event.x and event.x<=480) and (80<event.y and event.y<=160)) and stage[1][5] == 0:
            canvas.create_oval(400,80,480,160,fill="black")
            stage[1][5] = 1
        elif ((480<event.x and event.x<=560) and (80<event.y and event.y<=160)) and stage[1][6] == 0:
            canvas.create_oval(480,80,560,160,fill="black")
            stage[1][6] = 1
        elif ((560<event.x and event.x<=640) and (80<event.y and event.y<=160)) and stage[1][7] == 0:
            canvas.create_oval(560,80,640,160,fill="black")
            stage[1][7] = 1
        elif (event.x<=80 and (160<event.y and event.y<=240)) and stage[2][0] == 0:
            canvas.create_oval(0,160,80,240,fill="black")
            stage[2][0] = 1
        elif ((80<event.x and event.x<=160) and (160<event.y and event.y<=240)) and stage[2][1] == 0:
            canvas.create_oval(80,160,160,240,fill="black")
            stage[2][1] = 1
        elif ((160<event.x and event.x<=240) and (160<event.y and event.y<=240)) and stage[2][2] == 0:
            canvas.create_oval(160,160,240,240,fill="black")
            stage[2][2] = 1
        elif ((240<event.x and event.x<=320) and (160<event.y and event.y<=240)) and stage[2][3] == 0:
            canvas.create_oval(240,160,320,240,fill="black")
            stage[2][3] = 1
        elif ((320<event.x and event.x<=400) and (160<event.y and event.y<=240)) and stage[2][4] == 0:
            canvas.create_oval(320,160,400,240,fill="black")
            stage[2][4] = 1
        elif ((400<event.x and event.x<=480) and (160<event.y and event.y<=240)) and stage[2][5] == 0:
            canvas.create_oval(400,160,480,240,fill="black")
            stage[2][5] = 1
        elif ((480<event.x and event.x<=560) and (160<event.y and event.y<=240)) and stage[2][6] == 0:
            canvas.create_oval(480,160,560,240,fill="black")
            stage[2][6] = 1
        elif ((560<event.x and event.x<=640) and (160<event.y and event.y<=240)) and stage[2][7] == 0:
            canvas.create_oval(560,160,640,240,fill="black")
            stage[2][7] = 1
        elif (event.x<=80 and (240<event.y and event.y<=320)) and stage[3][0] == 0:
            canvas.create_oval(0,240,80,320,fill="black")
            stage[3][0] = 1
        elif ((80<event.x and event.x<=160) and (240<event.y and event.y<=320)) and stage[3][1] == 0:
            canvas.create_oval(80,240,160,320,fill="black")
            stage[3][1] = 1
        elif ((160<event.x and event.x<=240) and (240<event.y and event.y<=320)) and stage[3][2] == 0:
            canvas.create_oval(160,240,240,320,fill="black")
            stage[3][2] = 1
        elif ((240<event.x and event.x<=320) and (240<event.y and event.y<=320)) and stage[3][3] == 0:
            canvas.create_oval(240,240,320,320,fill="black")
            stage[3][3] = 1
        elif ((320<event.x and event.x<=400) and (240<event.y and event.y<=320)) and stage[3][4] == 0:
            canvas.create_oval(320,240,400,320,fill="black")
            stage[3][4] = 1
        elif ((400<event.x and event.x<=480) and (240<event.y and event.y<=320)) and stage[3][5] == 0:
            canvas.create_oval(400,240,480,320,fill="black")
            stage[3][5] = 1
        elif ((480<event.x and event.x<=560) and (240<event.y and event.y<=320)) and stage[3][6] == 0:
            canvas.create_oval(480,240,560,320,fill="black")
            stage[3][6] = 1
        elif ((560<event.x and event.x<=640) and (240<event.y and event.y<=320)) and stage[3][7] == 0:
            canvas.create_oval(560,240,640,320,fill="black")
            stage[3][7] = 1
        elif (event.x<=80 and (320<event.y and event.y<=400)) and stage[4][0] == 0:
            canvas.create_oval(0,320,80,400,fill="black")
            stage[4][0] = 1
        elif ((80<event.x and event.x<=160) and (320<event.y and event.y<=400)) and stage[4][1] == 0:
            canvas.create_oval(80,320,160,400,fill="black")
            stage[4][1] = 1
        elif ((160<event.x and event.x<=240) and (320<event.y and event.y<=400)) and stage[4][2] == 0:
            canvas.create_oval(160,320,240,400,fill="black")
            stage[4][2] = 1
        elif ((240<event.x and event.x<=320) and (320<event.y and event.y<=400)) and stage[4][3] == 0:
            canvas.create_oval(240,320,320,400,fill="black")
            stage[4][3] = 1
        elif ((320<event.x and event.x<=400) and (320<event.y and event.y<=400)) and stage[4][4] == 0:
            canvas.create_oval(320,320,400,400,fill="black")
            stage[4][4] = 1
        elif ((400<event.x and event.x<=480) and (320<event.y and event.y<=400)) and stage[4][5] == 0:
            canvas.create_oval(400,320,480,400,fill="black")
            stage[4][5] = 1
        elif ((480<event.x and event.x<=560) and (320<event.y and event.y<=400)) and stage[4][6] == 0:
            canvas.create_oval(480,320,560,400,fill="black")
            stage[4][6] = 1
        elif ((560<event.x and event.x<=640) and (320<event.y and event.y<=400)) and stage[4][7] == 0:
            canvas.create_oval(560,320,640,400,fill="black")
            stage[4][7] = 1
        elif (event.x<=80 and (400<event.y and event.y<=480)) and stage[5][0] == 0:
            canvas.create_oval(0,400,80,480,fill="black")
            stage[5][0] = 1
        elif ((80<event.x and event.x<=160) and (400<event.y and event.y<=480)) and stage[5][1] == 0:
            canvas.create_oval(80,400,160,480,fill="black")
            stage[5][1] = 1
        elif ((160<event.x and event.x<=240) and (400<event.y and event.y<=480)) and stage[5][2] == 0:
            canvas.create_oval(160,400,240,480,fill="black")
            stage[5][2] = 1
        elif ((240<event.x and event.x<=320) and (400<event.y and event.y<=480)) and stage[5][3] == 0:
            canvas.create_oval(240,400,320,480,fill="black")
            stage[5][3] = 1
        elif ((320<event.x and event.x<=400) and (400<event.y and event.y<=480)) and stage[5][4] == 0:
            canvas.create_oval(320,400,400,480,fill="black")
            stage[5][4] = 1
        elif ((400<event.x and event.x<=480) and (400<event.y and event.y<=480)) and stage[5][5] == 0:
            canvas.create_oval(400,400,480,480,fill="black")
            stage[5][5] = 1
        elif ((480<event.x and event.x<=560) and (400<event.y and event.y<=480)) and stage[5][6] == 0:
            canvas.create_oval(480,400,560,480,fill="black")
            stage[5][6] = 1
        elif ((560<event.x and event.x<=640) and (400<event.y and event.y<=480)) and stage[5][7] == 0:
            canvas.create_oval(560,400,640,480,fill="black")
            stage[5][7] = 1
        elif (event.x<=80 and (480<event.y and event.y<=560)) and stage[6][0] == 0:
            canvas.create_oval(0,480,80,560,fill="black")
            stage[6][0] = 1
        elif ((80<event.x and event.x<=160) and (480<event.y and event.y<=560)) and stage[6][1] == 0:
            canvas.create_oval(80,480,160,560,fill="black")
            stage[6][1] = 1
        elif ((160<event.x and event.x<=240) and (480<event.y and event.y<=560)) and stage[6][2] == 0:
            canvas.create_oval(160,480,240,560,fill="black")
            stage[6][2] = 1
        elif ((240<event.x and event.x<=320) and (480<event.y and event.y<=560)) and stage[6][3] == 0:
            canvas.create_oval(240,480,320,560,fill="black")
            stage[6][3] = 1
        elif ((320<event.x and event.x<=400) and (480<event.y and event.y<=560)) and stage[6][4] == 0:
            canvas.create_oval(320,480,400,560,fill="black")
            stage[6][4] = 1
        elif ((400<event.x and event.x<=480) and (480<event.y and event.y<=560)) and stage[6][5] == 0:
            canvas.create_oval(400,480,480,560,fill="black")
            stage[6][5] = 1
        elif ((480<event.x and event.x<=560) and (480<event.y and event.y<=560)) and stage[6][6] == 0:
            canvas.create_oval(480,480,560,560,fill="black")
            stage[6][6] = 1
        elif ((560<event.x and event.x<=640) and (480<event.y and event.y<=560)) and stage[6][7] == 0:
            canvas.create_oval(560,480,640,560,fill="black")
            stage[6][7] = 1
        elif (event.x<=80 and (560<event.y and event.y<=640)) and stage[7][0] == 0:
            canvas.create_oval(0,560,80,640,fill="black")
            stage[7][0] = 1
        elif ((80<event.x and event.x<=160) and (560<event.y and event.y<=640)) and stage[7][1] == 0:
            canvas.create_oval(80,560,160,640,fill="black")
            stage[7][1] = 1
        elif ((160<event.x and event.x<=240) and (560<event.y and event.y<=640)) and stage[7][2] == 0:
            canvas.create_oval(160,560,240,640,fill="black")
            stage[7][2] = 1
        elif ((240<event.x and event.x<=320) and (560<event.y and event.y<=640)) and stage[7][3] == 0:
            canvas.create_oval(240,560,320,640,fill="black")
            stage[7][3] = 1
        elif ((320<event.x and event.x<=400) and (560<event.y and event.y<=640)) and stage[7][4] == 0:
            canvas.create_oval(320,560,400,640,fill="black")
            stage[7][4] = 1
        elif ((400<event.x and event.x<=480) and (560<event.y and event.y<=640)) and stage[7][5] == 0:
            canvas.create_oval(400,560,480,640,fill="black")
            stage[7][5] = 1
        elif ((480<event.x and event.x<=560) and (560<event.y and event.y<=640)) and stage[7][6] == 0:
            canvas.create_oval(480,560,560,640,fill="black")
            stage[7][6] = 1
        elif ((560<event.x and event.x<=640) and (560<event.y and event.y<=640)) and stage[7][7] == 0:
            canvas.create_oval(560,560,640,640,fill="black")
            stage[7][7] = 1
    elif player == -1:
    #白のターンの時
        if (event.x<=80 and event.y<=80) and stage[0][0] == 0:
            canvas.create_oval(0,0,80,80,fill="white")
            stage[0][0] = -1
        elif ((80<event.x and event.x<=160) and event.y<=80) and stage[0][1] == 0:
            canvas.create_oval(80,0,160,80,fill="white")
            stage[0][1] = -1
        elif ((160<event.x and event.x<=240) and event.y<=80) and stage[0][2] == 0:
            canvas.create_oval(160,0,240,80,fill="white")
            stage[0][2] = -1
        elif ((240<event.x and event.x<=320) and event.y<=80) and stage[0][3] == 0:
            canvas.create_oval(240,0,320,80,fill="white")
            stage[0][3] = -1
        elif ((320<event.x and event.x<=400) and event.y<=80) and stage[0][4] == 0:
            canvas.create_oval(320,0,400,80,fill="white")
            stage[0][4] = -1
        elif ((400<event.x and event.x<=480) and event.y<=80) and stage[0][5] == 0:
            canvas.create_oval(400,0,480,80,fill="white")
            stage[0][5] = -1
        elif ((480<event.x and event.x<=560) and event.y<=80) and stage[0][6] == 0:
            canvas.create_oval(480,0,560,80,fill="white")
            stage[0][6] = -1
        elif ((560<event.x and event.x<=640) and event.y<=80) and stage[0][7] == 0:
            canvas.create_oval(560,0,640,80,fill="white")
            stage[0][7] = -1
        elif (event.x<=80 and (80<event.y and event.y<=160)) and stage[1][0] == 0:
            canvas.create_oval(0,80,80,160,fill="white")
            stage[1][0] = -1
        elif ((80<event.x and event.x<=160) and (80<event.y and event.y<=160)) and stage[1][1] == 0:
            canvas.create_oval(80,80,160,160,fill="white")
            stage[1][1] = -1
        elif ((160<event.x and event.x<=240) and (80<event.y and event.y<=160)) and stage[1][2] == 0:
            canvas.create_oval(160,80,240,160,fill="white")
            stage[1][2] = -1
        elif ((240<event.x and event.x<=320) and (80<event.y and event.y<=160)) and stage[1][3] == 0:
            canvas.create_oval(240,80,320,160,fill="white")
            stage[1][3] = -1
        elif ((320<event.x and event.x<=400) and (80<event.y and event.y<=160)) and stage[1][4] == 0:
            canvas.create_oval(320,80,400,160,fill="white")
            stage[1][4] = -1
        elif ((400<event.x and event.x<=480) and (80<event.y and event.y<=160)) and stage[1][5] == 0:
            canvas.create_oval(400,80,480,160,fill="white")
            stage[1][5] = -1
        elif ((480<event.x and event.x<=560) and (80<event.y and event.y<=160)) and stage[1][6] == 0:
            canvas.create_oval(480,80,560,160,fill="white")
            stage[1][6] = -1
        elif ((560<event.x and event.x<=640) and (80<event.y and event.y<=160)) and stage[1][7] == 0:
            canvas.create_oval(560,80,640,160,fill="white")
            stage[1][7] = -1
        elif (event.x<=80 and (160<event.y and event.y<=240)) and stage[2][0] == 0:
            canvas.create_oval(0,160,80,240,fill="white")
            stage[2][0] = -1
        elif ((80<event.x and event.x<=160) and (160<event.y and event.y<=240)) and stage[2][1] == 0:
            canvas.create_oval(80,160,160,240,fill="white")
            stage[2][1] = -1
        elif ((160<event.x and event.x<=240) and (160<event.y and event.y<=240)) and stage[2][2] == 0:
            canvas.create_oval(160,160,240,240,fill="white")
            stage[2][2] = -1
        elif ((240<event.x and event.x<=320) and (160<event.y and event.y<=240)) and stage[2][3] == 0:
            canvas.create_oval(240,160,320,240,fill="white")
            stage[2][3] = -1
        elif ((320<event.x and event.x<=400) and (160<event.y and event.y<=240)) and stage[2][4] == 0:
            canvas.create_oval(320,160,400,240,fill="white")
            stage[2][4] = -1
        elif ((400<event.x and event.x<=480) and (160<event.y and event.y<=240)) and stage[2][5] == 0:
            canvas.create_oval(400,160,480,240,fill="white")
            stage[2][5] = -1
        elif ((480<event.x and event.x<=560) and (160<event.y and event.y<=240)) and stage[2][6] == 0:
            canvas.create_oval(480,160,560,240,fill="white")
            stage[2][6] = -1
        elif ((560<event.x and event.x<=640) and (160<event.y and event.y<=240)) and stage[2][7] == 0:
            canvas.create_oval(560,160,640,240,fill="white")
            stage[2][7] = -1
        elif (event.x<=80 and (240<event.y and event.y<=320)) and stage[3][0] == 0:
            canvas.create_oval(0,240,80,320,fill="white")
            stage[3][0] = -1
        elif ((80<event.x and event.x<=160) and (240<event.y and event.y<=320)) and stage[3][1] == 0:
            canvas.create_oval(80,240,160,320,fill="white")
            stage[3][1] = -1
        elif ((160<event.x and event.x<=240) and (240<event.y and event.y<=320)) and stage[3][2] == 0:
            canvas.create_oval(160,240,240,320,fill="white")
            stage[3][2] = -1
        elif ((240<event.x and event.x<=320) and (240<event.y and event.y<=320)) and stage[3][3] == 0:
            canvas.create_oval(240,240,320,320,fill="white")
            stage[3][3] = -1
        elif ((320<event.x and event.x<=400) and (240<event.y and event.y<=320)) and stage[3][4] == 0:
            canvas.create_oval(320,240,400,320,fill="white")
            stage[3][4] = -1
        elif ((400<event.x and event.x<=480) and (240<event.y and event.y<=320)) and stage[3][5] == 0:
            canvas.create_oval(400,240,480,320,fill="white")
            stage[3][5] = -1
        elif ((480<event.x and event.x<=560) and (240<event.y and event.y<=320)) and stage[3][6] == 0:
            canvas.create_oval(480,240,560,320,fill="white")
            stage[3][6] = -1
        elif ((560<event.x and event.x<=640) and (240<event.y and event.y<=320)) and stage[3][7] == 0:
            canvas.create_oval(560,240,640,320,fill="white")
            stage[3][7] = -1
        elif (event.x<=80 and (320<event.y and event.y<=400)) and stage[4][0] == 0:
            canvas.create_oval(0,320,80,400,fill="white")
            stage[4][0] = -1
        elif ((80<event.x and event.x<=160) and (320<event.y and event.y<=400)) and stage[4][1] == 0:
            canvas.create_oval(80,320,160,400,fill="white")
            stage[4][1] = -1
        elif ((160<event.x and event.x<=240) and (320<event.y and event.y<=400)) and stage[4][2] == 0:
            canvas.create_oval(160,320,240,400,fill="white")
            stage[4][2] = -1
        elif ((240<event.x and event.x<=320) and (320<event.y and event.y<=400)) and stage[4][3] == 0:
            canvas.create_oval(240,320,320,400,fill="white")
            stage[4][3] = -1
        elif ((320<event.x and event.x<=400) and (320<event.y and event.y<=400)) and stage[4][4] == 0:
            canvas.create_oval(320,320,400,400,fill="white")
            stage[4][4] = -1
        elif ((400<event.x and event.x<=480) and (320<event.y and event.y<=400)) and stage[4][5] == 0:
            canvas.create_oval(400,320,480,400,fill="white")
            stage[4][5] = -1
        elif ((480<event.x and event.x<=560) and (320<event.y and event.y<=400)) and stage[4][6] == 0:
            canvas.create_oval(480,320,560,400,fill="white")
            stage[4][6] = -1
        elif ((560<event.x and event.x<=640) and (320<event.y and event.y<=400)) and stage[4][7] == 0:
            canvas.create_oval(560,320,640,400,fill="white")
            stage[4][7] = -1
        elif (event.x<=80 and (400<event.y and event.y<=480)) and stage[5][0] == 0:
            canvas.create_oval(0,400,80,480,fill="white")
            stage[5][0] = -1
        elif ((80<event.x and event.x<=160) and (400<event.y and event.y<=480)) and stage[5][1] == 0:
            canvas.create_oval(80,400,160,480,fill="white")
            stage[5][1] = -1
        elif ((160<event.x and event.x<=240) and (400<event.y and event.y<=480)) and stage[5][2] == 0:
            canvas.create_oval(160,400,240,480,fill="white")
            stage[5][2] = -1
        elif ((240<event.x and event.x<=320) and (400<event.y and event.y<=480)) and stage[5][3] == 0:
            canvas.create_oval(240,400,320,480,fill="white")
            stage[5][3] = -1
        elif ((320<event.x and event.x<=400) and (400<event.y and event.y<=480)) and stage[5][4] == 0:
            canvas.create_oval(320,400,400,480,fill="white")
            stage[5][4] = -1
        elif ((400<event.x and event.x<=480) and (400<event.y and event.y<=480)) and stage[5][5] == 0:
            canvas.create_oval(400,400,480,480,fill="white")
            stage[5][5] = -1
        elif ((480<event.x and event.x<=560) and (400<event.y and event.y<=480)) and stage[5][6] == 0:
            canvas.create_oval(480,400,560,480,fill="white")
            stage[5][6] = -1
        elif ((560<event.x and event.x<=640) and (400<event.y and event.y<=480)) and stage[5][7] == 0:
            canvas.create_oval(560,400,640,480,fill="white")
            stage[5][7] = -1
        elif (event.x<=80 and (480<event.y and event.y<=560)) and stage[6][0] == 0:
            canvas.create_oval(0,480,80,560,fill="white")
            stage[6][0] = -1
        elif ((80<event.x and event.x<=160) and (480<event.y and event.y<=560)) and stage[6][1] == 0:
            canvas.create_oval(80,480,160,560,fill="white")
            stage[6][1] = -1
        elif ((160<event.x and event.x<=240) and (480<event.y and event.y<=560)) and stage[6][2] == 0:
            canvas.create_oval(160,480,240,560,fill="white")
            stage[6][2] = -1
        elif ((240<event.x and event.x<=320) and (480<event.y and event.y<=560)) and stage[6][3] == 0:
            canvas.create_oval(240,480,320,560,fill="white")
            stage[6][3] = -1
        elif ((320<event.x and event.x<=400) and (480<event.y and event.y<=560)) and stage[6][4] == 0:
            canvas.create_oval(320,480,400,560,fill="white")
            stage[6][4] = -1
        elif ((400<event.x and event.x<=480) and (480<event.y and event.y<=560)) and stage[6][5] == 0:
            canvas.create_oval(400,480,480,560,fill="white")
            stage[6][5] = -1
        elif ((480<event.x and event.x<=560) and (480<event.y and event.y<=560)) and stage[6][6] == 0:
            canvas.create_oval(480,480,560,560,fill="white")
            stage[6][6] = -1
        elif ((560<event.x and event.x<=640) and (480<event.y and event.y<=560)) and stage[6][7] == 0:
            canvas.create_oval(560,480,640,560,fill="white")
            stage[6][7] = -1
        elif (event.x<=80 and (560<event.y and event.y<=640)) and stage[7][0] == 0:
            canvas.create_oval(0,560,80,640,fill="white")
            stage[7][0] = -1
        elif ((80<event.x and event.x<=160) and (560<event.y and event.y<=640)) and stage[7][1] == 0:
            canvas.create_oval(80,560,160,640,fill="white")
            stage[7][1] = -1
        elif ((160<event.x and event.x<=240) and (560<event.y and event.y<=640)) and stage[7][2] == 0:
            canvas.create_oval(160,560,240,640,fill="white")
            stage[7][2] = -1
        elif ((240<event.x and event.x<=320) and (560<event.y and event.y<=640)) and stage[7][3] == 0:
            canvas.create_oval(240,560,320,640,fill="white")
            stage[7][3] = -1
        elif ((320<event.x and event.x<=400) and (560<event.y and event.y<=640)) and stage[7][4] == 0:
            canvas.create_oval(320,560,400,640,fill="white")
            stage[7][4] = -1
        elif ((400<event.x and event.x<=480) and (560<event.y and event.y<=640)) and stage[7][5] == 0:
            canvas.create_oval(400,560,480,640,fill="white")
            stage[7][5] = -1
        elif ((480<event.x and event.x<=560) and (560<event.y and event.y<=640)) and stage[7][6] == 0:
            canvas.create_oval(480,560,560,640,fill="white")
            stage[7][6] = -1
        elif ((560<event.x and event.x<=640) and (560<event.y and event.y<=640)) and stage[7][7] == 0:
            canvas.create_oval(560,560,640,640,fill="white")
            stage[7][7] = -1

        
    #石がそろっていないか確認
    if judge_Winner() == 1:
        print("黒の勝ち")
        check_click1()
    elif judge_Winner() == -1:
        print("白の勝ち")
        check_click2()
    elif judge_Winner() == -2:
        print("引き分けです")
        check_click3()
    count_1=0
    count_2=0
    for i in range(8):
        for j in range(8):
            if stage[j][i] == 0:
                count_1 += 1
    for i in range(8):
        for j in range(8):
            if record[j][i] == 0:
                count_2 += 1
    #そろっていないのでターンを変える
    if count_1 != count_2:
    #マスに石をちゃんと置いた場合
        player = turn_change()
    record_stage()
    #マスの石を記録する
        
root=tkinter.Tk()
root.title("５目並べ")
root.bind("<ButtonPress>",put_stone)
#クリックをしたらput_stoneを実行

canvas=tkinter.Canvas(root,width=stage_width*num_stage_x, height=stage_width*num_stage_y,bg="orange")
canvas.create_line(0,80,640,80,fill="black")
canvas.create_line(0,160,640,160,fill="black")
canvas.create_line(0,240,640,240,fill="black")
canvas.create_line(0,320,640,320,fill="black")
canvas.create_line(0,400,640,400,fill="black")
canvas.create_line(0,480,640,480,fill="black")
canvas.create_line(0,560,640,560,fill="black")
canvas.create_line(0,640,640,640,fill="black")
canvas.create_line(80,0,80,640,fill="black")
canvas.create_line(160,0,160,640,fill="black")
canvas.create_line(240,0,240,640,fill="black")
canvas.create_line(320,0,320,640,fill="black")
canvas.create_line(400,0,400,640,fill="black")
canvas.create_line(480,0,480,640,fill="black")
canvas.create_line(560,0,560,640,fill="black")
canvas.create_line(640,0,640,640,fill="black")
canvas.pack()
#キャンバスを配置

root.mainloop()

