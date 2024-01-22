from tkinter import *
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import  os

class Stegno:
    def main(self,root):
        root.title('ImageSteganography')
        root.state('zoomed')
        f_m = Frame(root, background='light blue')
        title = Label(f_m, text='Image Steganography', bg="light blue", bd=20, fg="Black")
        title.config(font=('TimesNewRoman 28 bold'))
        # title.place(x=600, y=100)
        title.grid(pady=10)
        b_text = Button(f_m, text="TEXT IN IMAGE", command=lambda: self.frame1_text(f_m), padx=14, bg="Bisque", bd=5,
                          fg="Black")
        b_text.config(font=('TimesNewRoman 14 bold'))
        # b_encode.place(x=700, y= 200)
        b_text.grid(pady=12)
        b_image = Button(f_m, text="IMAGE IN IMAGE", padx=14, command=lambda: self.frame1_image(f_m), bg="Bisque", bd=5,
                          fg="Black")
        b_image.config(font=('TimesNewRoman 14 bold'))
        # b_decode.place(x=700, y=300)
        b_image.grid(pady=12)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        f_m.grid()
        title.grid(row=1)
        b_text.grid(row=2)
        b_image.grid(row=3)

    def frame1_text(self,f_m):
        f_m.destroy()
        f = Frame(root, background='light blue')
        title = Label(f, text='Image Steganography', bg="light blue", bd=20, fg="Black")
        title.config(font=('TimesNewRoman 28 bold'))
        # title.place(x=600, y=100)
        title.grid(pady=10)
        b_tencode = Button(f, text="Encode", command=lambda: self.frame1_tencode(f), padx=14, bg="Bisque", bd=5,
                          fg="Black")
        b_tencode.config(font=('TimesNewRoman 14 bold'))
        # b_encode.place(x=700, y= 200)
        b_tencode.grid(pady=12)
        b_tdecode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_tdecode(f), bg="Bisque", bd=5,
                          fg="Black")
        b_tdecode.config(font=('TimesNewRoman 14 bold'))
        # b_decode.place(x=700, y=300)
        b_tdecode.grid(pady=12)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        f.grid()
        title.grid(row=1)
        b_tencode.grid(row=2)
        b_tdecode.grid(row=3)

    def home(self,frame):
            frame.destroy()
            self.main(root)

    def frame1_tdecode(self,f):
        f.destroy()
        d_f2 = Frame(root,bg = "light blue")
        l1 = Label(d_f2, text='Select Image with Hidden text:',bg = "light blue", bd = 5, fg = "Black")
        l1.config(font=('TimesNewRoman 28 bold'))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda :self.frame2_tdecode(d_f2),bg = "Bisque", bd = 5, fg = "Black")
        bws_button.config(font=('TimesNewRoman 14 bold'))
        bws_button.grid(pady = 15)
        back_button = Button(d_f2, text='Cancel', command=lambda : Stegno.home(self,d_f2),bg = "Bisque", bd = 5, fg = "Black")
        back_button.config(font=('TimesNewRoman 14 bold'))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_tdecode(self,d_f2):
        d_f3 = Frame(root,bg = "light blue")
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :',bg = "light blue", bd = 5, fg = "Black")
            l4.config(font=('TimesNewRoman 28 bold'))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.tdecode(myimg)
            l2 = Label(d_f3, text='Hidden data is :',bg = "light blue", bd = 5, fg = "Black")
            l2.config(font=('TimesNewRoman 28 bold'))
            l2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel', command= lambda :self.page3(d_f3),bg = "Bisque", bd = 5, fg = "Black")
            back_button.config(font=('TimesNewRoman 14 bold'))
            back_button.grid(pady=15)
            back_button.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    def tdecode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_tencode(self,f):
        f.destroy()
        f2 = Frame(root,bg = "light blue")
        l1= Label(f2,text='Select the Image in which \n you want to hide text :',bg = "light blue", bd = 5, fg = "Black")
        l1.config(font=('TimesNewRoman 28 bold'))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.frame2_tencode(f2),bg = "Bisque", bd = 5, fg = "Black")
        bws_button.config(font=('TimesNewRoman 14 bold'))
        bws_button.grid(pady = 15)
        back_button = Button(f2, text='Cancel', command=lambda : Stegno.home(self,f2),bg = "Bisque", bd = 5, fg = "Black")
        back_button.config(font=('TimesNewRoman 14 bold'))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()


    def frame2_tencode(self,f2):
        ep= Frame(root,bg = "light blue")
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='Selected Image',bg = "light blue", bd = 5, fg = "Black")
            l3.config(font=('TimesNewRoman 28 bold'))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message',bg = "light blue", bd = 5, fg = "Black")
            l2.config(font=('TimesNewRoman 28 bold'))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            tencode_button = Button(ep, text='Cancel', command=lambda : Stegno.home(self,ep),bg = "Bisque", bd = 5, fg = "Black")
            tencode_button.config(font=('TimesNewRoman 14 bold'))
            data = text_area.get("1.0", "end-1c")
            back_button = Button(ep, text='Encode', command=lambda : [self.enc_fun(text_area,myimg),Stegno.home(self,ep)],bg = "Bisque", bd = 5, fg = "Black")
            back_button.config(font=('TimesNewRoman 14 bold'))
            back_button.grid(pady=15)
            tencode_button.grid()
            ep.grid(row=1)
            f2.destroy()


    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                '\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                    self.o_image_w,self.o_image_h,
                                    self.d_image_size/1000000,
                                    self.d_image_w,self.d_image_h)
            messagebox.showinfo('info',str)
        except:
            messagebox.showinfo('Info','Unable to get the information')

    def genData(self,data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def tencode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.tencode_enc(newimg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def page3(self,frame):
        frame.destroy()
        self.main(root)

    def frame1_image(self, f_m):
        f_m.destroy()
        f = Frame(root, background='light blue')
        title = Label(f, text='Image Steganography', bg="light blue", bd=20, fg="Black")
        title.config(font=('TimesNewRoman 28 bold'))
        # title.place(x=600, y=100)
        title.grid(pady=10)
        b_iencode = Button(f, text="Encode", command=lambda: self.frame1_iencode(f), padx=14, bg="Bisque", bd=5,
                          fg="Black")
        b_iencode.config(font=('TimesNewRoman 14 bold'))
        # b_encode.place(x=700, y= 200)
        b_iencode.grid(pady=12)
        b_idecode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_idecode(f), bg="Bisque", bd=5,
                          fg="Black")
        b_idecode.config(font=('TimesNewRoman 14 bold'))
        # b_decode.place(x=700, y=300)
        b_idecode.grid(pady=12)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        f.grid()
        title.grid(row=1)
        b_iencode.grid(row=2)
        b_idecode.grid(row=3)
    def home(self,frame):
            frame.destroy()
            self.main(root)

    def frame1_iencode(self, f):
        f.destroy()
        f2 = Frame(root, bg="light blue")
        l1 = Label(f2, text='Select the Image in which \n you want to hide image :', bg="light blue", bd=10, fg="Black")
        l1.config(font=('TimesNewRoman 28 bold'))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_iencode(f2), bg="Bisque", bd=5, fg="Black")
        bws_button.config(font=('TimesNewRoman 14 bold'))
        bws_button.grid(pady=15)
        back_button = Button(f2, text='Cancel', command=lambda: Stegno.home(self, f2), bg="Bisque", bd=5, fg="Black")
        back_button.config(font=('TimesNewRoman 14 bold'))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()

    def frame2_iencode(self, f2, text_area=None):
        ep= Frame(root,bg = "light blue")
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300, 300))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep, text='Selected Image', bg="light blue", bd=5, fg="Black")
            l3.config(font=('TimesNewRoman 28 bold'))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Select the secret image', bg="light blue", bd=5, fg="Black")
            l2.config(font=('TimesNewRoman 28 bold'))
            l2.grid(pady=15)
            bws_button =Button(ep, text='Select', command=lambda: Stegno.home(self, ep), bg="Bisque", bd=5, fg="Black")
            bws_button.config(font=('TimesNewRoman 14 bold'))
            iencode_button = Button(ep, text='Cancel', command=lambda: Stegno.home(self, ep), bg="Bisque", bd=5,
                                    fg="Black")
            iencode_button.config(font=('TimesNewRoman 14 bold'))

            back_button = Button(ep, text='encode',
                                 command=lambda: [self.enc_fun(text_area, myimg), Stegno.home(self, ep)], bg="Bisque",
                                 bd=5, fg="Black")
            back_button.config(font=('TimesNewRoman 14 bold'))
            back_button.grid(pady=15)
            iencode_button.grid()
            ep.grid(row=1)
            f2.destroy()






















root = Tk()

"""bg_img = Image.open("bg.png")
bg_back = ImageTk.PhotoImage(bg_img)
bg_label = Label(root, image=bg_back)
bg_label.place(x=0, y=0)"""

o = Stegno()
o.main(root)

root.mainloop()
