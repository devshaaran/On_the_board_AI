import os
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import time
from pydarknet import Detector, Image
import cv2
import numpy as np
# global constants
img = None
tl_list = (2,2)
br_list = (2,2)

# sys.path.insert(0, '/home/shaaran/PycharmProjects/om/YOLO3-4-Py')



def yolo():

    if __name__ == "__main__":
        # Optional statement to configure preferred GPU. Available only in GPU version.
        # pydarknet.set_cuda_device(0)

        net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                       bytes("cfg/coco.data", encoding="utf-8"))

        cap = cv2.VideoCapture(0)
        r,cropper = cap.read()
        targeter(cropper)

        while True:
            r, frame = cap.read()
            if r:
                frame_cropped = frame[tl_list[1]:br_list[1],tl_list[0]:br_list[0]]
                start_time = time.time()
                y,x,w = frame_cropped.shape
                print(x,y)
                # Only measure the time taken by YOLO and API Call overhead

                dark_frame = Image(frame)
                results = net.detect(dark_frame)
                del dark_frame

                end_time = time.time()
                print("Elapsed Time:", end_time - start_time, 'final_result',results)

                for cat, score, bounds in results:
                    x, y, w, h = bounds
                    cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)),
                                  (255, 0, 0))
                    cv2.putText(frame, str(cat.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (255, 255, 0))


                cv2.imshow("preview", frame)
                cv2.imshow('hey',frame_cropped)

            k = cv2.waitKey(1)
            if k == 0xFF & ord("q"):
                break


def mycode():
    #TODO make a folder and check for it - read components

    if os.path.exists(os.path.join(os.getcwd(),'on_the_board')):
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(),'on_the_board'))

    # tf code

    x = ['''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>New project</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
        <script src="main.js"></script>
    </head>
    <body>
    
    '''
    ,
    ''' 
    </body>
    </html>''']

    html_tool = {'searchbar':'''<nav>
                        <div class="nav-wrapper z-depth-4">
                          <form>
                            <div class="input-field z-depth-4">
                              <input id="search" type="search" required>
                              <label class="label-icon right" for="search"><i class="material-icons">maps</i></label>
                              <i class="material-icons">close</i>
                            </div>
                          </form>
                        </div>
                    </nav>''',
                 'button':'<button class="btn btn-large black">Read More</button>',
                 'random_para':'<h4 class="truncate">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit porro eius esse, qui sequi tempore impedit ea, similique nulla neque ad velit minus deleniti quibusdam laborum voluptatem explicabo! Blanditiis, expedita.</h4>',
                 'list':'''<ul class="collection">
              <li class="collection-item">Item 1</li>
              <li class="collection-item">Item 2</li>
              <li class="collection-item">Item 3</li>
              <li class="collection-item">Item 4</li>
            </ul>''',
                 'header':'''<h2 style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Header</h2>''',
                 'input_text':'''<div class="input-field">
               <input type="text" id="label">
               <label class="active" for="name">here</label>
             </div>''',
                 'input_textarea':'''<div class="input-field">
               <textarea type="textarea" id="textarea" class="materialize-textarea"></textarea>
               <label class="active" for="textarea">Textarea</label>
             </div>''',
                 'grid_div2':'''<div class="row">
           <div class="col s6"><div class="card-panel grey">boop</div></div>
         </div>''',
                 'navig':'''<nav>
            <div class="nav-wrapper blue">
              <h3 class="center"> heading </h3>
              </div>
          </nav>'''
                 }



    # writer
    # with open(os.path.join(os.getcwd(),'on_the_board','index.html'),'w') as f:
    #     f.read()
    #     f.write('''<!DOCTYPE html>
    # <html>
    # <head>
    #     <meta charset="utf-8" />
    #     <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #     <title>New project</title>
    #     <meta name="viewport" content="width=device-width, initial-scale=1">
    #     <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    #     <script src="main.js"></script>
    # </head>
    # <body>
    #
    # </body>
    # </html>''')


def line_select_callback(clk, rls):
    global tl_list
    global br_list

    tl_list = (int(clk.xdata), int(clk.ydata))
    br_list = (int(rls.xdata), int(rls.ydata))



def onkeypress(event):

    global tl_list
    global br_list
    global img
    if event.key == 'q':
        print(tl_list,':',br_list)



def toggle_selector(event):
    toggle_selector.RS.set_active(True)

def targeter(image):
    if __name__ == '__main__':

        fig, ax = plt.subplots(1)
        # mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry(250, 120, 1280, 1024)
        imagey = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(imagey)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()


yolo()
