from PIL import Image ,ImageChops
img1=Image.open(r"C:\Users\dell\Desktop\Kat\difference-between-two-similar-looking-images-master\1.jpg")#image 1 path
img2=Image.open(r"C:\Users\dell\Desktop\Kat\difference-between-two-similar-looking-images-master\2.jpg")#image 2 path
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
	diff.show()