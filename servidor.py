from flask import Flask, request, render_template, Response
from flask_cors import CORS
from PIL import Image
import os
import io
import PIL.Image as Image
import base64
import urllib
import cv2 as cv
import numpy as np


app = Flask(__name__)
CORS(app)

app.config['CARPETA_PRINCIPAL'] = os.path.dirname(__file__)
app.config['GUARDAR_COSAS'] = os.path.dirname(__file__)+"\\"+"desdehtml"+"\\"
app.config['IMAGENES_ANALIZADAS'] = os.path.dirname(__file__)+"\\"+"analizadas"+"\\"
path_imagenes_analizadas = os.path.dirname(__file__)+"\\"+"analizadas"+"\\"
path_coger_imagenes = os.path.dirname(__file__)+"\\"+"desdehtml"+"\\"

@app.route('/', methods= ['GET', 'POST'])
def index():
 print("Me pides el index y yo te lo doy")
 return render_template("index.html")

@app.route('/objects', methods= ['GET', 'POST'])
def objects():
 # if request.method == "GET":
 print("Te cargo los objetos pishica")
 return render_template("objects.html")

@app.route('/colors', methods= ['GET', 'POST'])
def colors():
 # if request.method == "GET":
 print("¿Quieres los colores? Aquí tienes miarma")
 return render_template("colors.html")

@app.route('/future', methods= ['GET', 'POST'])
def future():
 # if request.method == "GET":
 print("Te doy el futuro compadre")
 return render_template("future.html")


@app.route('/mandarimagen', methods=['GET','POST'])
def mandarimagen():
    if request.method == 'POST':
        print("Vamos a recibir la imagen")
        # print(request.values)
        i = request.form.get('img')  # Con esto tengo lo que el ordenador interpreta como la información de la imagen


        # POR FIN HOSTIA YA PUEDO CONVERTIR LOS PUTOS DATOS EN PUTAS IMAGENES VAMOOOOOOOOOOOOOOOOOS!!!!!!!!
        response = urllib.request.urlopen(i)
        with open(app.config['GUARDAR_COSAS']+'imagendesdehtml.png', 'wb') as f:
            f.write(response.file.read())
        

        # Quitarle el rgba (no se por qué sale con él XD)
        imagen = Image.open(app.config['GUARDAR_COSAS']+'imagendesdehtml.png')
        rgb = imagen.convert('RGB')
        rgb.save(app.config['GUARDAR_COSAS']+'imagenbuena.png')


        # Guardo también el txt por si acaso
        txt = open(app.config['GUARDAR_COSAS']+'dataurldelaimagen.txt', 'w')
        txt.write(i)
        txt.close() 


        # Para analizar la imagen y guardarla
        filename_entrada = 'imagenbuena.png'
        analizarimagenes(filename_entrada)


        # Para cargar la imagen y enviarla al html (En proceso aún)
        filename_salida = 'imagenanalizada.png'
        img = Image.open(app.config['IMAGENES_ANALIZADAS']+filename_salida)
        data = io.BytesIO()
        img.save(data, format="png")
        encode_img_data = base64.b64encode(data.getvalue())
        userimage = encode_img_data.decode("UTF-8")
        pasarajavascript = 'data:image/png;base64,'+userimage

        return (pasarajavascript)
    else:
        # Para cargar la imagen y enviarla al html
        filename_salida = 'imagenanalizada.png'
        img = Image.open(app.config['IMAGENES_ANALIZADAS']+filename_salida)
        data = io.BytesIO()
        img.save(data, format="png")
        encode_img_data = base64.b64encode(data.getvalue())
        userimage = encode_img_data.decode("UTF-8")
        pasarajavascript = 'data:image/png;base64,'+userimage

        return (pasarajavascript)

def analizarimagenes(filename):
    net = cv.dnn.readNet('yolov3.weights','yolov3.cfg')
    classes = [] # person, bicycle, airport...
    with open("coco.names", "r") as f: 
        classes = [line.strip() for line in f.readlines()]
    layers_names = net.getLayerNames()
    output_layers = [layers_names[i-1] for i in net.getUnconnectedOutLayers()]
    
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Load image    
    img = cv.imread(path_coger_imagenes+"/"+filename) # foto que quiero analizar 
    img = cv.resize(img, None, fx=1, fy=1) # fx, fy se redimensiona la foto
    height, width, channels = img.shape 


    # Detecting objects
    blob = cv.dnn.blobFromImage(img, 0.00392, (416,416), (0,0,0), True, crop = False)
    # 320x320 small, 416x416 medium, 609x609 bigger

    net.setInput(blob)
    outs = net.forward(output_layers)
    # print(outs)

    # Showing informations on the screen 
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5: # Más del 50% de efectividad 
                # Object detected
                center_x = int(detection[0]*width) #width and height original from the image
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                # Rectangle coordinates 
                x = int(center_x - w /2)
                y = int(center_y - h / 2)

                
                boxes.append([ x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    number_objects_detected = len(boxes)
    font = cv.FONT_ITALIC # Fuente del recuadro
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])  # Label son las clases identificadas en la foto
            
            color = colors[i]
            cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
            # introducir texto en cada rectangulo
            cv.putText(img, label, (x,y+30), font, 0.7, color, 2)  # Font es el tamaño de letra y color es si la quieres mas gruesa o menos
    
    cv.imwrite(os.path.join(path_imagenes_analizadas,'imagenanalizada.png'), img)
    cv.waitKey(0)
    return 0


# Con esto streameamos lo de los colores

@app.route('/streamcolores', methods=['GET','POST'])
def streamcolores():
    # camera = cv.VideoCapture("https://192.168.1.118:8080/video") # Esto es un apaño para la cámara del móvil, hacienso uso de la aplicación IP Webcam
    camera = cv.VideoCapture(0)

    Blue_light = np.array([100,100,20], np.uint8)
    Blue_dark = np.array([125,255,255], np.uint8)

    yellow_light = np.array([15,100,20], np.uint8)
    yellow_dark = np.array([45,255,255], np.uint8)

    red_light1 = np.array([0,100,20], np.uint8)
    red_dark1 = np.array([5,255,255], np.uint8)

    red_light2 = np.array([175,100,20], np.uint8)
    red_dark2 = np.array([179,255,255], np.uint8)

    font = cv.FONT_HERSHEY_SIMPLEX

    def gen_frames():  
        while True:
            ret, frame = camera.read()  # read the camera frame
            if not ret:
                break
            else:
                frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                maskBlue = cv.inRange(frameHSV, Blue_light, Blue_dark)
                maskYellow = cv.inRange(frameHSV, yellow_light, yellow_dark)
                maskRed1 = cv.inRange(frameHSV, red_light1, red_dark1)
                maskRed2 = cv.inRange(frameHSV, red_light2, red_dark2)
                maskRed = cv.add(maskRed1, maskRed2)

                # #### Para el azul
                # dibujar(maskBlue, (255,0,0))
                contornos,_ = cv.findContours(maskBlue, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                for c in contornos:
                    area = cv.contourArea(c)
                    if area > 3000:
                        M = cv.moments(c)
                        if (M["m00"]==0): M["m00"]=1
                        x = int(M["m10"]/M["m00"])
                        y = int(M['m01']/M['m00'])
                        nuevoContorno = cv.convexHull(c)
                        # cv.circle(frame, (x,y), 7, (0,255,0), -1)
                        # cv.putText(frame, '{},{}' .format(x,y), (x+10,y), font, 0.75, (0,255,0), 1, cv.LINE_AA)
                        cv.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
                
                # #### Para el amarillo
                # dibujar(maskYellow, (3,255,255))
                contornos,_ = cv.findContours(maskYellow, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                for c in contornos:
                    area = cv.contourArea(c)
                    if area > 3000:
                        M = cv.moments(c)
                        if (M["m00"]==0): M["m00"]=1
                        x = int(M["m10"]/M["m00"])
                        y = int(M['m01']/M['m00'])
                        nuevoContorno = cv.convexHull(c)
                        # cv.circle(frame, (x,y), 7, (0,255,0), -1)
                        # cv.putText(frame, '{},{}' .format(x,y), (x+10,y), font, 0.75, (0,255,0), 1, cv.LINE_AA)
                        cv.drawContours(frame, [nuevoContorno], 0, (3,255,255), 3)
                
                # #### Para el rojo
                # dibujar(, (0,0,255))
                contornos,_ = cv.findContours(maskRed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                for c in contornos:
                    area = cv.contourArea(c)
                    if area > 3000:
                        M = cv.moments(c)
                        if (M["m00"]==0): M["m00"]=1
                        x = int(M["m10"]/M["m00"])
                        y = int(M['m01']/M['m00'])
                        nuevoContorno = cv.convexHull(c)
                        # cv.circle(frame, (x,y), 7, (0,255,0), -1)
                        # cv.putText(frame, '{},{}' .format(x,y), (x+10,y), font, 0.75, (0,255,0), 1, cv.LINE_AA)
                        cv.drawContours(frame, [nuevoContorno], 0, (0,0,255), 3)


                ret, buffer = cv.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == "__main__":
    context = ('localhost.pem', 'localhost.key')
    app.run(host='0.0.0.0', debug=True, ssl_context=context)
 


