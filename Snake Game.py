import random import curses

scr=curses.initscr() curses.curs_set(0)

height,width=scr.getmaxyx() win=curses.newwin(height,width,0,0)

scr.keypad(1) scr.timeout(100)

snk_x=int(width/4) snk_y=int(height/2)

snake=[ [snk_y,snk_x], [snk_y,snk_x-1], [snk_y,snk_x-2] ]

food=[int(height/2),int(width/2)] win.addch(food[0],food[1],"0")

key=curses.KEY_RIGHT while True: next_key=win.getch() key=key if next_key==-1 else next_key if snake[0][0] in [0,height] or snake[0][1] in [0,width] or snake[0] in snake[1:]: curses.endwin() quit() new_head=[snake[0][0],snake[0][1]] if key==curses.KEY_DOWN: new_head+=1 if key==curses.KEY_UP: new_head-=1 if key==curses.KEY_RIGHT: new_head+=1 if key==curses.KEY_LEFT: new_head-=1

snake.insert(0,new_head)

if snake[0]==food:
    food=None
    while food is None:
        nf=[
             random.randint(1,height-1),
             random.randint(1,width-1)
           ]
        food=nf if nf not in snake else None
    win.addch(food[0],food[1],curses.ACS_PI)
else:
    tail=snake.pop()
    win.addch(tail[0],tail[1]," ")
win.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)    
