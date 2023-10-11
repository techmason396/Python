'''
    các file media (image, audio, video) đều là file nhị phân
    cho nên các mode trong function open() thì phải thêm 'b'
'''

pic = open('pic1.jfif','rb')
img = pic.read()

copying = open('pic2.jfif','wb')
copying.write(img)

pic.close()
copying.close()