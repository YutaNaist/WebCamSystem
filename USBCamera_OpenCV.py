import cv2
# import serial.tools.list_ports
import threading


class Camera:
    cameraIndex = 0
    w0 = 640
    h0 = 480
    vl0 = 0
    hl0 = 0

    def __init__(self, index):
        self.cameraIndex = index
        #self.cap0 = cv2.VideoCapture(self.cameraIndex, cv2.CAP_MSMF)
        self.cap0 = cv2.VideoCapture(self.cameraIndex)
        #self.cap0.set(cv2.CAP_PROP_FRAME_WIDTH, self.w0)
        #self.cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, self.h0)


    def __del__(self):
        # return 0
        self.cap0.release()
        cv2.destroyAllWindows()

    def scanOneImage(self):
        # print("start capture{}".format(self.cameraIndex))

        ret0, frame0 = self.cap0.read()
        cv2.line(frame0, (self.vl0, 0), (self.vl0, self.h0), (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)
        cv2.line(frame0, (self.vl0 + 1, 0), (self.vl0 + 1, self.h0),
                 (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)
        cv2.line(frame0, (self.vl0 - 1, 0), (self.vl0 - 1, self.h0),
                 (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)

        cv2.line(frame0, (0, self.hl0), (self.w0, self.hl0), (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)
        cv2.line(frame0, (0, self.hl0 + 1), (self.w0, self.hl0 + 1),
                 (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)
        cv2.line(frame0, (0, self.hl0 - 1), (self.w0, self.hl0 - 1),
                 (255, 255, 255),
                 thickness=1,
                 lineType=cv2.LINE_4)

        cv2.putText(frame0,
                    "H0=" + str(self.hl0), (0, self.hl0 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255),
                    thickness=1,
                    lineType=cv2.LINE_AA)
        cv2.putText(frame0,
                    "V0=" + str(self.vl0), (self.vl0 + 5, 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255),
                    thickness=1,
                    lineType=cv2.LINE_AA)
        # cv2.imshow('frame0', frame0)
        cv2.imwrite("./temp_{}.png".format(self.cameraIndex), frame0)
        # print("Capture {}".format(self.cameraIndex))


        return frame0

    def showCapture(self):
        while (True):
            ret0, frame0 = self.cap0.read()
            cv2.line(frame0, (self.vl0, 0), (self.vl0, self.h0),
                     (255, 255, 255),
                     thickness=1,
                     lineType=cv2.LINE_4)
            cv2.line(frame0, (0, self.hl0), (self.w0, self.hl0),
                     (255, 255, 255),
                     thickness=1,
                     lineType=cv2.LINE_4)
            cv2.putText(frame0,
                        "H0=" + str(self.hl0), (0, self.hl0 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 255),
                        thickness=1,
                        lineType=cv2.LINE_AA)
            cv2.putText(frame0,
                        "V0=" + str(self.vl0), (self.vl0 + 5, 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 255),
                        thickness=1,
                        lineType=cv2.LINE_AA)
            cv2.imshow('frame0', frame0)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break


if __name__ == "__main__":
    camera = Camera(1)
    print("camera connected")
    camera.showCapture()
    th = threading.Thread(target=camera.showCapture())
    th.start()
    th.join()
    # camera.scanOneImage()
