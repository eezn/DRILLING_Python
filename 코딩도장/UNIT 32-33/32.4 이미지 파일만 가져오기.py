# .jpg, .png인 이미지 파일만 출력

files = ['font', '1.png', '10.png', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))