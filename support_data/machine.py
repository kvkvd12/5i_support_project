import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import torch
import cv2
from django.conf import settings 


# yolov5 깃헙 저장소에서 모델을 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 사람 수 세어주는 함수
def transform_image(image):
    img = cv2.imread(settings.BASE_DIR/image[1:])

    results = model(img)
    result = results.pandas().xyxy[0].to_numpy()
    result = [item for item in result if item[6]=='person']

    return len(result)


# 사람 인식해서 네모모양으로 찍어주는 함수
def rectangle_image(image,write_image):

    img = cv2.imread(settings.BASE_DIR/image[1:])

    results = model(img)
    result = results.pandas().xyxy[0].to_numpy()
    result = [item for item in result if item[6]=='person']

    tmp_img = cv2.imread(settings.BASE_DIR/image[1:])
    for j in range(len(result)):
        cv2.rectangle(tmp_img, (int(results.xyxy[0][j][0].item()), int(results.xyxy[0][j][1].item())), (int(results.xyxy[0][j][2].item()), int(results.xyxy[0][j][3].item())), (255,255,255))
    cv2.imwrite(settings.BASE_DIR/write_image[1:], tmp_img)
    return tmp_img

    
    
