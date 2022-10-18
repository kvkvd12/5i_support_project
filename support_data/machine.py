import torch
import cv2

#yolo 모델을 불러오고 이미지를 읽은 뒤 이미지를 모델안에 넣어줌
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
img = cv2.imread('2-1.jpg')
results = model(img)

#사람을 인식하는 코드
result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('2-1.jpg')

#사람을 인식한수 만큼 for문을 돌려 사람을 사각형으로 둘러쌈
for j in range(len(result)):
    cv2.rectangle(tmp_img, (int(results.xyxy[0][j][0].item()), int(results.xyxy[0][j][1].item())), (int(results.xyxy[0][j][2].item()), int(results.xyxy[0][j][3].item())), (255,255,255))
print(j+1)