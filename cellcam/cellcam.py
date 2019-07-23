import camconfig
from cv2 import VideoCapture

class CellphoneCam:
    def __init__(self, protocol, context_type = 1):
        
        if protocol == "http":
            if context_type == 1:
                context = "/video"
            elif context_type == 2:
                context = "/onvif/device_service"
        
        elif protocol == "rtsp":
            if context_type == 1:
                context = "/h264_pcm.sdp"
            elif context_type == 2:
                context = "/h264_ulaw.sdp"
        
        protocol = protocol + "://"
        self.url = protocol + camconfig.cam_user + ":" + camconfig.pwd + "@" + camconfig.cam_ip + ":" + camconfig.port + context
        self.stream = VideoCapture(self.url)