#Algoritmos da Unidade 1 de Computação Gráfica implementados em Tkinter, uma ferramenta de interface gráfica para Python
#Instalação: Selecione a caixa "tcl/tk e IDLE" em "Instalação personalizada" no instalador do Python
#Instruções de uso:
#1. Use o comando "py cg1.py" em um prompt de comando apontando para o diretorio contendo este programa;
#2. Clique em qualquer lugar do canvas com o botão esquerdo do mouse para selecionar as coordenadas do ponto inicial e com o direito para selecionar as do ponto final;
#3. Uma vez selecionados os pontos, clique na caixa com o nome do algoritmo que você quer rodar -alguns algoritmos rodam com valores pré-determinados e/ou requerem que seja definida uma rasterização primeiro;
#4. Clique em "limpar" para reiniciar as coordenadas e apagar os desenhos no canvas.

import tkinter as tk
from math import cos, sin, sqrt, pow, pi

xmin = 100
ymin = 80
xmax = 300
ymax = 170

class graphics_unit1:

    # ----- Gerar aviso de erro -----
    
    def popup(self, tx):
        win = tk.Toplevel()
        win.wm_title("Aviso")
        win.resizable(width=False, height=False)

        l = tk.Label(win, text=tx)
        l.grid(row=0, column=0)

        b = tk.Button(win, text="Close", command=win.destroy)
        b.grid(row=1, column=0)
    
    # ----- Desenhar linha por DDA -----
    
    def draw_dda(self):
      try:
        self.canvas.delete("all")
        
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())

        self.object_list = [x1, y1, x2, y2, "dda"]
        self.raster.set("DDA")

        dx = x2 - x1
        dy = y2 - y1

        steps, x, y = 0, x1, y1

        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        x_increment = dx/steps
        y_increment = dy/steps

        for i in range(steps):
            x = x + x_increment
            y = y + y_increment

            self.canvas.create_rectangle(round(x), round(y), round(x)+1, round(y)+1)
      except ZeroDivisionError:
        self.popup("Valores ruins para o algoritmo. Escolha outros.")
    
    # ----- Desenhar linha por Bresenham -----
    
    def draw_bresenham(self):
        
        self.canvas.delete("all")
        
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())

        self.object_list = [x1, y1, x2, y2, "bresenham"]
        self.raster.set("Bresenham")

        x, y = x1, y1
        
        self.canvas.create_rectangle(x, y, x+1, y+1)
        
        dx = x2 - x1
        dy = y2 - y1
        x_increment, y_increment = 0, 0
        
        if dx < 0:
            dx = dx * -1
            x_increment = -1
        else:
            x_increment = 1

        if dy < 0:
            dy = dy * -1
            y_increment = -1
        else:
            y_increment = 1

        if dx > dy:
            p = 2*dy - dx
            c1 = 2*dy
            c2 = 2*(dy-dx)

            for i in range(dx):
                x = x + x_increment
                if p < 0:
                    p = p + c1
                else:
                    p = p + c2
                    y = y + y_increment

                self.canvas.create_rectangle(x, y, x+1, y+1)
        else:
            p = 2*dx - dy
            c1 = 2*dx
            c2 = 2*(dx-dy)

            for i in range(dy):
                y = y + y_increment
                if p < 0:
                    p = p + c1
                else:
                    p = p + c2
                    x = x + x_increment

                self.canvas.create_rectangle(x, y, x+1, y+1)
                
    # ----- Auxiliar para a funcao "crop" -----

    def regionID(self, x, y):
        id= 0
        if(x<xmin):
            id|=1
        if(x>xmax):
            id|=2
        if(y<ymin):
            id|=4
        if(y>ymax):
            id|=8
        return id

    # ----- Cohen-Sutherland -Regiões codificadas -----
   
    def crop(self):
      if(not self.object_list):
        self.popup("Rasterização não definida!")
      elif(self.object_list[4] == "circle"):
        self.popup("Este algoritmo não é executado em círculos.")
      else:
        self.canvas.delete("all")
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())
        aceite= False
       #feito= False
        while(True):
            c1= self.regionID(x1, y1)
            c2= self.regionID(x2, y2)
            if(c1==0 and c2==0):
                aceite= True
               #feito= True
                break
            elif(c1 & c2):#you can do this on c++ too
               #feito= True
                break
            else:
                x=1.0
                y=1.0
                if(c1!=0):
                    cfora= c1
                else:
                    cfora= c2
                if(cfora & 1): #a.k.a. "if(cfora%2!=0)"
                    xint= xmin
                    yint= y1+(y2-y1)*(xmin-x1)/(x2-x1)
                elif(cfora & 2):
                    xint= xmax
                    yint= y1+(y2-y1)*(xmax-x1)/(x2-x1)
                elif(cfora & 4):
                    yint= ymin
                    xint= x1+(x2-x1)*(ymin-y1)/(y2-y1)
                elif(cfora & 8):
                    yint= ymax
                    xint= x1+(x2-x1)*(ymax-y1)/(y2-y1)
                if(c1==cfora):
                    x1=xint
                    y1=yint
                else:
                    x2=xint
                    y2=yint
        if(aceite):
            self.x1_value.set(str(int(x1)))
            self.y1_value.set(str(int(y1)))
            self.x2_value.set(str(int(x2)))
            self.y2_value.set(str(int(y2)))
            if self.object_list[4] == "dda":
                self.draw_dda()
           #elif self.object_list[4] == "circle":
               #self.draw_circle()
            elif self.object_list[4] == "bresenham":
                self.draw_bresenham()
        self.canvas.create_rectangle(xmin, ymin, xmax, ymax, outline="red")

    # ----- Auxiliar para a funcao "parametric" -----
    
    def cliptest(self, p, q):
        r= q/p
        result= True
        if (p<0.0): #fora para dentro
            if (r>self.u2):
                result= False
            elif (r>self.u1):
                self.u1= r
        elif(p>0.0): #dentro para fora
            if (r<self.u1):
                result= False
            elif (r<self.u2):
                self.u2= r
        elif (q<0.0):
            result= False
        return result

    # ----- Liang-Barsky -Equacao parametrica -----

    def draw_parametric(self):
      if(not self.object_list):
        self.popup("Rasterização não definida!")
      elif(self.object_list[4] == "circle"):
        self.popup("Este algoritmo não é executado em círculos.")
      else:
        self.canvas.delete("all")
        
        x1 = int(self.x1_value.get())
        y1 = int(self.y1_value.get())
        x2 = int(self.x2_value.get())
        y2 = int(self.y2_value.get())
        
        self.u1= 0.0
        self.u2= 1.0
        dx= x2-x1
        dy= y2-y1
        
        if(self.cliptest(-dx, x1-xmin)):
            if(self.cliptest(dx, xmax-x1)):
                if(self.cliptest(-dy, y1-ymin)):
                    if(self.cliptest(dy, ymax-y1)):
                        if(self.u2<1.0):
                            x2= x1+self.u2*dx
                            y2= y1+self.u2*dy
                        if(self.u1>0.0):
                            x1= x1+self.u1*dx
                            y1= y1+self.u1*dy
                        self.x1_value.set(str(int(x1)))
                        self.y1_value.set(str(int(y1)))
                        self.x2_value.set(str(int(x2)))
                        self.y2_value.set(str(int(y2)))
                        if self.object_list[4] == "dda":
                            self.draw_dda()
                       #elif self.object_list[4] == "circle":
                           #self.draw_circle()
                        elif self.object_list[4] == "bresenham":
                            self.draw_bresenham()
        
        self.canvas.create_rectangle(xmin, ymin, xmax, ymax, outline="red")

    # ----- Desenhar circunferencia por Bresenham -----
 
    def draw_circle(self):
    
        self.canvas.delete("all")
        
        cx = int(self.x1_value.get())
        cy = int(self.y1_value.get())
        x = int(self.x2_value.get())
        y = int(self.y2_value.get()) 
        radius = sqrt(pow((x - cx), 2) + pow((y - cy), 2))

        self.object_list = [cx, cy, x, y, "circle"]
        self.raster.set("Circunferência")

        x = 0
        y = int(radius)
        p = 3 - 2*radius
        self.draw_symmetric(x, y, cx, cy)

        while x < y:
            if p < 0:
                p += 4 * x + 6
            else:
                p += 4 * (x - y) + 10
                y = y - 1
            x = x + 1
            self.draw_symmetric(x, y, cx, cy)

    def draw_symmetric(self, x, y, cx, cy):

        self.canvas.create_rectangle((cx + x), (cy + y), (cx + x)+1, (cy + y)+1)
        self.canvas.create_rectangle((cx + x), (cy - y), (cx + x)+1, (cy - y)+1)
        self.canvas.create_rectangle((cx - x), (cy + y), (cx - x)+1, (cy + y)+1)
        self.canvas.create_rectangle((cx - x), (cy - y), (cx - x)+1, (cy - y)+1)
        self.canvas.create_rectangle((cx + y), (cy + x), (cx + y)+1, (cy + x)+1)
        self.canvas.create_rectangle((cx + y), (cy - x), (cx + y)+1, (cy - x)+1)
        self.canvas.create_rectangle((cx - y), (cy + x), (cx - y)+1, (cy + x)+1)
        self.canvas.create_rectangle((cx - y), (cy - x), (cx - y)+1, (cy - x)+1)

    # ----- Fatores de transformacao -----
    
    # @ Translação
    def translate(self):
      if(not self.object_list):
        self.popup("Rasterização não definida!")
      else:
        self.canvas.delete("all")
        
        tx = 10 #constante da translacao para x
        ty = 10 #constante da translacao para y

        new_x1 = self.object_list[0] + tx
        new_y1 = self.object_list[1] + ty
        new_x2 = self.object_list[2] + tx
        new_y2 = self.object_list[3] + ty

        self.x1_value.set(str(new_x1))
        self.y1_value.set(str(new_y1))
        self.x2_value.set(str(new_x2))
        self.y2_value.set(str(new_y2))

        if self.object_list[4] == "dda":
            self.draw_dda()
        elif self.object_list[4] == "circle":
            self.draw_circle()
        elif self.object_list[4] == "bresenham":
            self.draw_bresenham()
            
    # @ Escala -dos pontos em relacao as coordenadas (0, 0)
    def scale(self):
      if(not self.object_list):
        self.popup("Rasterização não definida!")
      else:
        self.canvas.delete("all")
        
        sc = 1.2 #constante da escala

        new_x1 = int(self.object_list[0] * sc)
        new_y1 = int(self.object_list[1] * sc)
        new_x2 = int(self.object_list[2] * sc)
        new_y2 = int(self.object_list[3] * sc)

        self.x1_value.set(str(new_x1))
        self.y1_value.set(str(new_y1))
        self.x2_value.set(str(new_x2))
        self.y2_value.set(str(new_y2))

        if self.object_list[4] == "dda":
            self.draw_dda()
        elif self.object_list[4] == "circle":
            self.draw_circle()
        elif self.object_list[4] == "bresenham":
            self.draw_bresenham()
            
    # @ Rotacao -funciona, mas as coordenadas negativas nao sao visiveis
    def rotate(self):
      if(not self.object_list):
        self.popup("Rasterização não definida!")
      else:
        self.canvas.delete("all")

       #rt = int(self.x1_value.get())
        rt = pi/6 #constante de rotacao= mais conhecida como 30 graus

        new_x1 = int((self.object_list[0] * cos(rt)) - (self.object_list[1] * sin(rt)))
        new_y1 = int((self.object_list[0] * sin(rt)) + (self.object_list[1] * cos(rt)))
        new_x2 = int((self.object_list[2] * cos(rt)) - (self.object_list[3] * sin(rt)))
        new_y2 = int((self.object_list[2] * sin(rt)) + (self.object_list[3] * cos(rt)))

        self.x1_value.set(str(new_x1))
        self.y1_value.set(str(new_y1))
        self.x2_value.set(str(new_x2))
        self.y2_value.set(str(new_y2))

        if self.object_list[4] == "dda":
            self.draw_dda()
        elif self.object_list[4] == "circle":
            self.draw_circle()
        elif self.object_list[4] == "bresenham":
            self.draw_bresenham()
            
    # @ Reflexao -nao implementado, pois nao sera visivel
    def reflex(self):
        pass

    # ----- Limpar tela -----
 
    def clear_canvas(self):
        self.object_list = []
        self.canvas.delete("all")

        self.x1_value.set("0")
        self.y1_value.set("0")
        self.x2_value.set("0")
        self.y2_value.set("0")
        self.raster.set("Não definido")

    # ----- FUNCAO PRINCIPAL -----

    def __init__(self):
    
        # ----- Ler valores do clique -----
    
        def callback_init(event):
            self.x1_value.set(event.x)
            self.y1_value.set(event.y)
           #print(event.x, event.y)
        
        def callback(event):
            self.x2_value.set(event.x)
            self.y2_value.set(event.y)
           #print(event.x, event.y)

        # ----- Constantes -----

        win_width = 800
        win_height = 630
        canvas_width = 700
        canvas_height = 500

        self.object_list = []

        # ----- Montagem da janela -----

        window = tk.Tk()
        window.title("Computação Gráfica -Unidade 1")
        window.resizable(width=False, height=False)
        window.geometry('{}x{}'.format(win_width, win_height))

        # ----- Montagem do canvas -----

        self.canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#ffffff")
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()

        # ----- Entradas de valores -----

        label_one = tk.Label(frame, text="Coordenadas do ponto inicial: ").grid(row = 1, column = 2)
        self.x1_value = tk.StringVar()
        tk.Label(frame, textvariable = self.x1_value).grid(row = 1, column = 3)
        self.y1_value = tk.StringVar()
        tk.Label(frame, textvariable = self.y1_value).grid(row = 1, column = 4)
        label_three= tk.Label(frame, text= "Rasterização:").grid(row = 1, column = 5)
        
        label_two = tk.Label(frame, text="Coordenadas do ponto final: ").grid(row = 2, column = 2)
        self.x2_value = tk.StringVar()
        tk.Label(frame, textvariable = self.x2_value).grid(row = 2, column = 3)
        self.y2_value = tk.StringVar()
        tk.Label(frame, textvariable = self.y2_value).grid(row = 2, column = 4)
        self.raster = tk.StringVar()
        tk.Label(frame, textvariable = self.raster).grid(row = 2, column = 5)
        
        self.x1_value.set("0")
        self.y1_value.set("0")
        self.x2_value.set("0")
        self.y2_value.set("0")
        self.raster.set("Não definido")

        # ----- Acoes do mouse no canvas -----
        
        self.canvas.bind( "<Button-1>", callback_init )
        self.canvas.bind( "<Button-3>", callback )
        
        # ----- Acoes dos botoes -----

        dda_button = tk.Button(frame, text="DDA", command = self.draw_dda)
        dda_button.grid(row = 3, column = 1)
        
        bresenham_button = tk.Button(frame, text="Bresenham", command = self.draw_bresenham)
        bresenham_button.grid(row = 3, column = 2)
        
        parametric_button = tk.Button(frame, text="Equação Paramétrica", command = self.draw_parametric)
        parametric_button.grid(row = 3, column = 3)
        
        circumference_button = tk.Button(frame, text="Circunferência", command = self.draw_circle)
        circumference_button.grid(row = 3, column = 4)

        clear_button = tk.Button(frame, text="Limpar", command = self.clear_canvas)
        clear_button.grid(row = 3, column = 5)

        crop_button = tk.Button(frame, text="Recorte", command = self.crop)
        crop_button.grid(row = 4, column = 1)

        translation_button = tk.Button(frame, text="Translação", command = self.translate)
        translation_button.grid(row = 4, column = 2)
        
        scale_button = tk.Button(frame, text="Escala", command = self.scale)
        scale_button.grid(row = 4, column = 3)
        
        rotation_button = tk.Button(frame, text="Rotação", command = self.rotate)
        rotation_button.grid(row = 4, column = 4)

        # ----- Rodagem da janela -----

        window.mainloop()

cg_u1 = graphics_unit1()
#Marcos Tadeu Magalhães Rezende -Matrícula 552281