from threading import Thread, current_thread, main_thread, active_count


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            ct = current_thread()
            print(ct)
            print("Child ", i)


t1 = PrintThread()
t1.setName("Child")
print("Count ", active_count() )
mt = main_thread()
print(mt)
t1.start()
print("Count ", active_count() )
