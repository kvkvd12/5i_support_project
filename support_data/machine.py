import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import torch
import cv2
from django.conf import settings 


# yolov5 깃헙 저장소에서 모델을 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def transform_image(image):
    print(settings.BASE_DIR)
    print(image)
    print(settings.BASE_DIR / image[1:])
    img = cv2.imread(settings.BASE_DIR/image[1:])


    results = model(img)
    result = results.pandas().xyxy[0].to_numpy()
    result = [item for item in result if item[6]=='person']

    return len(result)


    # 인식 오류 났을 경우 확인용 코드
    # tmp_img = cv2.imread('Untitled.jpeg')

    # for j in range(len(result)):
    #     cv2.rectangle(tmp_img, (int(results.xyxy[0][j][0].item()), int(results.xyxy[0][j][1].item())), (int(results.xyxy[0][j][2].item()), int(results.xyxy[0][j][3].item())), (255,255,255))
    # print(j+1)
