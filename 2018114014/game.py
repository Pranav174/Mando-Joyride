from session import session
from character import Mando
from getch import _getChUnix
from alarmexception import AlarmException
from datetime import datetime
import signal 

def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

getch = _getChUnix()

def alarmHandler(signum, frame):
	raise AlarmException

def input_to(timeout = 1):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''


if __name__ == "__main__":
	newSession = session()
	newSession.addobject(Mando())
	newSession.getInitialFrame()
	input()
	while(1):
		prev = datetime.now()
		c = input_to(0.05)
		now = datetime.now()
		while (now-prev).total_seconds()<0.05:
			now = datetime.now()
		if c=='q':
			break
		newSession.setInput(c)
		newSession.renderNextFrame()
		if newSession.endGame():
			break
	newSession.getFinalFram()