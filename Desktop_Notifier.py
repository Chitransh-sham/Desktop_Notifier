import time
from plyer import notification
if __name__=='__main__':
    while(True):
        notification.notify(
            title="HELLO",
            message="THIS NOTIFIER IS MADE BY CHITRANSHU SHARMA",
            app_icon="C:/Users/HP/Desktop/favicon.ico",
            timeout=10
        )
        time.sleep(5)
