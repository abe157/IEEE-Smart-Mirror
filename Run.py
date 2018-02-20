import Finished_Mirror
import datetime
import time

def main():
	print "=====Running Mirror====="
	while(1):
		w = Finished_Mirror.FullWindow()
		w.tk.update()
		for i in range(7200):
			time.sleep(1)
			w.tk.update()
		print "=====Restarting Mirror====="
		w.tk.destroy()
	print "Closed at: ", datetime.datetime.today()
	
main()
