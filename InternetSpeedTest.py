import speedtest
import logging
import time

time.sleep(10)	# 10 seconds before speed test only for startup using crontab

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",filename="internetchecker.log",level=logging.DEBUG)
st=speedtest.Speedtest()
x=0

while x<13:
	try:
		downSpeed=str(int(st.download()*pow(10,-6)))
		upSpeed=str(int(st.upload()*pow(10,-6)))
		speedLog="Download: "+downSpeed+"MB/s\t||\tUpload: "+upSpeed+"MB/s"
		logging.info(speedLog)
		x=13
	except:
		logging.error("no connection")
		x=x+1
		time.sleep(60)

