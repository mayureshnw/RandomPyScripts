# Downloads all photos of Convocation 2015

import urllib2
from PIL import Image
import io


for i in range(7080, 8762):
	try:
		base_url = "http://info.vit.ac.in/30thconvocation/Day1/30%20th%20Convocation%20Photos/photos/DSC_"+str(i)+".jpg"
		html = urllib2.urlopen(base_url)
		image_file = io.BytesIO(html.read())
		im = Image.open(image_file)
		im.save(str(i)+".jpg")
	except:
		continue


