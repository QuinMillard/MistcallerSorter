from imutils.video import VideoStream
from imutils.video import FPS
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import shutil
import pytesseract

class VideoTextRecognizer:
    def __init__(self, source=1,threshold=7,rectangle_size_offset=3,min_confidence=0.5):
        self.SOURCE = source
        self.THRESHOLD = threshold
        self.RECTANGLE_SIZE_OFFSET = rectangle_size_offset
        self.MIN_CONFIDENCE = min_confidence

    def crop_image(self, img, start_x, start_y, end_x, end_y):
        cropped = img[start_y:end_y, start_x:end_x]
        return cropped

    def apply_threshold(self, img, argument):
        switcher = {
            1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
            2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
            3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
            4: cv2.threshold(cv2.medianBlur(img, 5), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
            5: cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
            6: cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
            7: cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
        }
        return switcher.get(argument, "Invalid method")

    def get_string(self, img, method):
        file_name = 'test.jpg'
        output_path = os.path.join('output/', file_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        if img.size == 0: return 'NOPE'
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        img = self.apply_threshold(img, method)
        save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")
        cv2.imwrite(save_path, img)

        result = pytesseract.image_to_string(img, lang="eng")
        return result

    def decode_predictions(self, scores, geometry):
        (numRows, numCols) = scores.shape[2:4]
        rects = []
        confidences = []

        for y in range(0, numRows):
            scoresData = scores[0, 0, y]
            xData0 = geometry[0, 0, y]
            xData1 = geometry[0, 1, y]
            xData2 = geometry[0, 2, y]
            xData3 = geometry[0, 3, y]
            anglesData = geometry[0, 4, y]

            for x in range(0, numCols):
                if scoresData[x] < self.MIN_CONFIDENCE:
                    continue
                (offsetX, offsetY) = (x * 4.0, y * 4.0)

                angle = anglesData[x]
                cos = np.cos(angle)
                sin = np.sin(angle)

                h = xData0[x] + xData2[x]
                w = xData1[x] + xData3[x]

                endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
                endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
                startX = int(endX - w)
                startY = int(endY - h)

                rects.append((startX, startY, endX, endY))
                confidences.append(scoresData[x])

        return (rects, confidences)

    def decode_from_stream(self):
        (W, H) = (None, None)
        (newW, newH) = (320, 320)
        (rW, rH) = (None, None)

        layerNames = [
            "feature_fusion/Conv_7/Sigmoid",
            "feature_fusion/concat_3"]

        print("[INFO] loading EAST text detector...")
        net = cv2.dnn.readNet('OCR/frozen_east_text_detection.pb')

        print("[INFO] starting video stream...")
        vs = VideoStream(src=self.SOURCE).start()
        time.sleep(1.0)

        fps = FPS().start()

        while True:
            frame = vs.read()
            print("[INFO] Reading a new frame.")

            if frame is None:
                break

            frame = imutils.resize(frame, width=1000)
            orig = frame.copy()

            if W is None or H is None:
                (H, W) = frame.shape[:2]
                rW = W / float(newW)
                rH = H / float(newH)

            frame = cv2.resize(frame, (newW, newH))

            blob = cv2.dnn.blobFromImage(frame, 1.0, (newW, newH),
                (123.68, 116.78, 103.94), swapRB=True, crop=False)
            net.setInput(blob)
            (scores, geometry) = net.forward(layerNames)

            (rects, confidences) = self.decode_predictions(scores, geometry)
            boxes = non_max_suppression(np.array(rects), probs=confidences)

            results = []

            for (startX, startY, endX, endY) in boxes:
                startX = int(startX * rW) - self.RECTANGLE_SIZE_OFFSET
                startY = int(startY * rH) - self.RECTANGLE_SIZE_OFFSET
                endX = int(endX * rW) + self.RECTANGLE_SIZE_OFFSET
                endY = int(endY * rH) + self.RECTANGLE_SIZE_OFFSET

                cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

                roi = orig[startY:endY, startX:endX]

                flipped_roi = roi.copy()
                flipped_roi = imutils.rotate(flipped_roi, angle=180)

                best_match = self.get_string(roi, self.THRESHOLD)
                best_flipped_match = self.get_string(flipped_roi, self.THRESHOLD)

                results.append(best_match)
                results.append(best_flipped_match)

            yield results

            fps.update()

            cv2.imshow("Text Detection", orig)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        fps.stop()

        print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

        vs.stop()

        cv2.destroyAllWindows()
