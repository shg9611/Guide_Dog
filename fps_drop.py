import cv2
import time

save_path='./test/mp4/fps_drop/test_video_drop.mp4'
video = cv2.VideoCapture('./test/mp4/test_video2.mp4')
w, h = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
prev_time=0
FPS=int(video.get(cv2.CAP_PROP_FPS))

vid_writer=cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), FPS/4, (w, h))

while(video.isOpened()):
    ret, frame = video.read()
    current_time = time.time() - prev_time



    if ret is not True :
        break

    if (ret is True) and (current_time > 1. / FPS):
        prev_time = time.time()
        frame=frame+30s
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        h,s,v=cv2.split(frame)
        s+=12
        frame=cv2.merge((h,s,v))

        frame=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

        cv2.imshow('VideoCapture', frame)
        vid_writer.write(frame)




        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
vid_writer.release()
cv2.destroyAllWindows()