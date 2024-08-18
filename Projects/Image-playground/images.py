from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR) # SMOOTH # ShARPEN
# filtered_img.save("./Output/blur.png", 'png')

converted_img = img.convert('L')
converted_img.save('./Output/grey.png', 'png')
# converted_img.show()

rotated_img = converted_img.rotate(90)
rotated_img.save('./Output/rgray.png', 'png')

resized_img = converted_img.resize((300, 300))
resized_img.save('./Output/regray.png', 'png')   

# Crop
box = (100, 100, 400, 400)
croped_img = converted_img.crop(box)
croped_img.save('./Output/cgray.png', 'png')   

img2 = Image.open('./astro.jpg')
print(img2.size)
new_img = img2.resize((400, 400))
new_img.save('./Output/thumbnail.jpg') 

img2.thumbnail((400, 400))
img2.save('./Output/thumbnail1.jpg')

print(img2.size)