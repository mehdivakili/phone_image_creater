from PIL import Image, ImageOps

# Read the two images
image1 = Image.open('phone_cover.png')
image1 = image1.convert("RGBA")

image2 = Image.open(input('please inter input image path: '))
image2 = image2.convert("RGBA")

mask = Image.open('mask.png').convert('L')

image2 = ImageOps.fit(image2, mask.size, centering=(0.5, 0.5))
image2.putalpha(mask)
image2 = image2.resize((2070, 4498))


# image2.show()
# resize, first image
image1_size = image1.size
image2_size = image2.size
# new_image = Image.new('RGB', image1_size, (255))
image1.paste(image2, (1465, 212), image2)
# new_image.paste(image1, (0, 0))


image1.save(input('please inter output image path: '), format="png")
# new_image.show()
