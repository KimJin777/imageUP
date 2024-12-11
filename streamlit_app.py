from PIL import Image

# 이미지 불러오기
image_path = 'your_image.jpg'
image = Image.open(image_path)

# 새로운 크기 설정 (예: 가로 2배, 세로 2배)
new_size = (image.width * 2, image.height * 2)
resized_image = image.resize(new_size)

# 이미지 저장
resized_image.save('resized_image.jpg')

# 이미지 표시
resized_image.show()
