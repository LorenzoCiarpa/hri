from deepface import DeepFace
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time


def getEmotionFromImg(path):
    result = DeepFace.analyze(img_path=path, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']

if __name__ == '__main__':
    result = DeepFace.analyze(img_path="./face.jpg", actions=['emotion'])
    print(result)

    
