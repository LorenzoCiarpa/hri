from deepface import DeepFace

result = DeepFace.analyze(img_path="captured_image0.jpg", actions=['emotion'])
print(result)
