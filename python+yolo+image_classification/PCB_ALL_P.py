import cv2
import numpy as np
import glob

def draw_text(img, text,
          font=cv2.FONT_HERSHEY_PLAIN,
          pos=(0, 0),
          font_scale=1,
          font_thickness=1,
          text_color=(0, 0, 0),
          text_color_bg=(0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size

min_confidence = 0.5
width = 1280
height = 0
show_ratio = 1.0
title_name = 'Custom Yolo'

# Load Yolo
net = cv2.dnn.readNet("./PCB_ALL/custom-train-yolo_final.weights", "./PCB_ALL/custom-train-yolo.cfg")
classes = []
with open("./PCB_ALL/classes.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
color_lists = [(0,0,255), (0,255,0)]

# Loading image
for filename in glob.glob("./PCB_IMG/good1.jpg"):
    img = cv2.imread(filename)
    h, w = img.shape[:2]
    height = int(h * width / w)
    img = cv2.resize(img, (width, height))
    cv2.imshow("Original Image", img)

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    names = []
    boxes = []
    # colors = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > min_confidence:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                names.append(classes[class_id])
                # colors.append(color_lists[class_id])

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1
    font_thickness = 1
    for j in range(len(boxes)):
        if j in indexes:
            x, y, w, h = boxes[j]
            label = '{} {:,.2%}'.format(names[j], confidences[j])
            # if names[j] == 'right_good' or names[j] == 'middle_good' or names[j] == 'left_good':
            if names[j] == "good":
                color = color_lists[1]
            # 사각형 그리기
            else:
                color = color_lists[0]
            print(filename, label)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y-10), font, 1, color, 1)        
    cv2.imshow("YOLO Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
