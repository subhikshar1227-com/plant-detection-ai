from detector import PlantDetector

detector = PlantDetector("best.pt")

result = detector.detect_image(r"C:\Users\User\Downloads\your_image.jpg")
print(result)