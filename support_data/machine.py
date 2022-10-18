import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
img = cv2.imread('Untitled.jpeg')

results = model(img)

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('Untitled.jpeg')

for j in range(len(result)):
    cv2.rectangle(tmp_img, (int(results.xyxy[0][j][0].item()), int(results.xyxy[0][j][1].item())), (int(results.xyxy[0][j][2].item()), int(results.xyxy[0][j][3].item())), (255,255,255))
print(j+1)
