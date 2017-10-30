import cv2

from utils.app_utils import FPS, WebcamVideoStream

'''
stream = cv2.VideoCapture(0)

print (stream == None)

while True:
    (grabbed, frame) = stream.read()

    if not grabbed:
        print ('[INFO] no frame grabbed')
    else:
        output = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

        cv2.imshow('Video', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
'''
video_capture = WebcamVideoStream(src=0).start()

while True:
    frame = video_capture.read()

    output = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

    cv2.imshow('Video', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
