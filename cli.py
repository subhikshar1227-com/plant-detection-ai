from detector import PlantDetector

def main():
    print("\n🌱 Plant Detection CLI")
    print("Drag and drop image or video file here and press Enter:\n")

    file_path = input("File path: ").strip().strip('"')

    detector = PlantDetector("best.pt")

    result = detector.detect(file_path)

    print("\n--- Detection Result ---")
    print(result)
    print("------------------------\n")

if __name__ == "__main__":
    main()