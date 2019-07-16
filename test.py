# import subprocess
# subprocess.run('shutdown -s -f -t 0')
import ctypes
import socket
import threading
from datetime import datetime
def week52(count):
    title = "주52시간-체커"
    count += 1
    timer = threading.Timer(3.0, week52, args=[count])
    timer.start()  # called every minute
    ip = socket.gethostbyname( socket.getfqdn() )
    print( "IP : " + ip )
    h = 18
    m = 20
    now = datetime.now()
    limitdate = now.replace(hour=h, minute=m, second=0, microsecond=0)
    print( "현재시간 : " + str(now) )
    print( "제한시간 : " + str(limitdate) )

    if now > limitdate:
        print("주52시간 종료")

        msg = ctypes.windll.user32.MessageBoxW(None, "근무시간은 "+ str(h) +":"+ str(m) +"까지 입니다.\nPC가 곧 종료됩니다.", title, 0)
        if msg == 1:
            print("OK")

    else:
        print("근무시간")
    if count == 5 :
        print(" 체크종료 ")
        timer.cancel()

week52(0)


