from PIL import Image
if __name__ == '__main__':
	im = Image.open('cardDeck.png')
	print im.size[0]
	for x in xrange(0,13):
		for y in xrange(0,5):
			im2 = im.crop(((im.size[0]/13+0.5)*x, (im.size[1]/5)*y, (im.size[0]/13)*(x+1)+5, (im.size[1]/5)*(y+1)))
			im2.save(str(x)+'_'+str(y)+'.png')