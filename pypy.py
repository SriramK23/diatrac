from picamera import PiCamera
from time import sleep
from google.cloud import vision
from subprocess import call




camera = PiCamera()

    
        
def takephoto(): 
    camera.start_preview()
    sleep(5)
    camera.capture('picy.jpg')
    camera.stop_preview()


def detect_document():
    takephoto()
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open('picy.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
         for block in page.blocks:
             print('\nBlock confidence: {}\n'.format(block.confidence))

         for paragraph in block.paragraphs:
             print('Paragraph confidence: {}'.format(paragraph.confidence))

             for word in paragraph.words:
                 word_text = ''.join([
                 symbol.text for symbol in word.symbols
                     ])
                 sleep(0.5)
		 
			
                 print('Word text: {} (confidence: {})'.format(
                            word_text, word.confidence))
		 temp = float(word_text)

		 if temp < 90.0:
		     tem = 119.0-temp
		     t = tem/3.416
        	     print('You need to consume ')
		     print(t)
		     print(' g of sugar')
		     print(' Or ')
		     print((t / 13) * 100)
		     print(' % of an apple')

                 
			

                        
        
                               


while True:
        
     detect_document()
     sleep(10)
