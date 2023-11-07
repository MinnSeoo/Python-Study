from multiprocessing import Process
import time


class Subprocess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name
    
    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")
        

if __name__ == "__main__":              # 메인 모듈일때만
    print("[main] start")
    p = Subprocess(name = "startcoding")
    p.start()
    p.join()            # main 프로세스가 sub 프로세스의 작업이 끝날때 까지 기다림.
    print("[main] end")