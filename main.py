import os
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import time
from pydarknet import Detector, Image
import cv2
from operator import itemgetter
from pyautogui import size
import html_headers

import numpy as np
# global constants
img = None
tl_list = (2,2)
br_list = (2,2)
label = 0
text = 1
header = 2
block_text = 3
button = 4
image = 5
paragraph = 6
textarea = 7
x_res,y_res = size()



# sys.path.insert(0, '/home/shaaran/PycharmProjects/om/YOLO3-4-Py')
# x.sort(key=itemgetter(1))
# this is what you use for it

def yolo():

    if __name__ == "__main__":
        # Optional statement to configure preferred GPU. Available only in GPU version.
        # pydarknet.set_cuda_device(0)
        # fourcc = cv2.VideoWriter_fourcc(*'MJPG')


        net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                       bytes("cfg/coco.data", encoding="utf-8"))

        cap = cv2.VideoCapture('projectile.mp4')
        # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (848, 480))

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
                total_list = []
                reg_decider = []
                x_val = []
                item_space = []

                for cat, score, bounds in results:

                    x, y, w, h = bounds
                    cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)),
                                  (255, 0, 0))
                    cv2.putText(frame, str(cat.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (255, 255, 0))



                    if cat.decode("utf-8") == 'label':
                        main_param  = 0
                    elif cat.decode("utf-8") == 'text':
                        main_param  = 1
                    elif cat.decode("utf-8") == 'header':
                        main_param  = 2
                    elif cat.decode("utf-8") == 'block_text':
                        main_param  = 3
                    elif cat.decode("utf-8") == 'button':
                        main_param  = 4
                    elif cat.decode("utf-8") == 'image':
                        main_param  = 5
                    elif cat.decode("utf-8") == 'paragraph':
                        main_param  = 6
                    else:
                        main_param  = 7


                    total_list.append([main_param,int(y - h / 2),int(y + h / 2)])
                    item_space.append(int(y + h / 2)-int(y - h / 2))
                    x_val.append([int(x - w / 2),int(x + w / 2)])

                    left_x = int(x - w / 2)
                    right_x = int(x + w / 2)

                    reg0 = 0
                    reg1 = (x_res / 2) - (x_res / 2.2)
                    reg2 = (x_res / 2) - (x_res / 4)
                    reg3 = (x_res / 2)
                    reg4 = (x_res / 2) + (x_res / 4)
                    reg5 = (x_res / 2) + (x_res / 2.2)
                    reg6 = x_res

                    if left_x < reg1 and right_x > reg5:
                        reg_decider.append(0)

                    elif left_x < reg2 and left_x > reg1 and right_x < reg3:
                        reg_decider.append(1)


                total_list.sort(key=itemgetter(1))
                space_list = []
                space_percent = []
                computer_res_fixture = []

                content_list = []


                label_turner = False

                for i in range(0,len(total_list)-1):
                    if i == 0:

                        space_list.append(total_list[i][1]-0)
                        space_percent.append((space_list[0]/y)*100)
                        computer_res_fixture.append(x_res-(x_res/8)*space_percent[0])
                        space_list.append(total_list[i+1][1]-total_list[i][2])
                        space_percent.append((space_list[i+1] / y) * 100)
                        computer_res_fixture.append(x_res - (x_res / 8) * space_percent[i+1])

                    else:

                        space_list.append(total_list[i + 1][1] - total_list[i][2])
                        space_percent.append((space_list[i + 1] / y) * 100)
                        computer_res_fixture.append((x_res - (x_res / 8)) * (space_percent[i+1]/100))

                        if label_turner == True:
                            continue

                        if total_list[i][0] == 0 or total_list[i][0] == 1:
                            if space_percent[i+1] < 0 and total_list[i][0] != total_list[i+1][0] :
                                content_list.append(html_headers.html_tools('style = margin-top: '+ computer_res_fixture[i]+ 'vh' )['input_text_label'])
                                label_turner = True
                                continue

                        if total_list[i][0] == 0 or total_list[i][0] == 7:
                            if space_percent[i + 1] < 0 and total_list[i][0] != total_list[i + 1][0]:
                                content_list.append(html_headers.html_tools('style = margin-top: '+ computer_res_fixture[i]+ 'vh')['input_textarea_label'])
                                label_turner = True
                                continue

                        if total_list[i][0] == 0 :
                            content_list.append(html_headers.html_tools('style = margin-top: '+ computer_res_fixture[i]+ 'vh')['label'])

                        elif total_list[i][0] == 1:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'input_text'])
                        elif total_list[i][0] == 2:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'header'])
                        elif total_list[i][0] == 3:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'block_text'])
                        elif total_list[i][0] == 4:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'button'])
                        elif total_list[i][0] == 5:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'image'])
                        elif total_list[i][0] == 0:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'paragraph'])
                        else:
                            content_list.append(
                                html_headers.html_tools('style = margin-top: ' + computer_res_fixture[i] + 'vh')[
                                    'input_textarea'])

                print(space_percent)

                # out.write(frame)
                cv2.imshow("preview", frame)
                # cv2.imshow('hey',frame_cropped)


                k = cv2.waitKey(1)
                if k == 0xFF & ord("q"):
                    break


def mycode(style):

    #TODO make a folder and check for it - read components

    if os.path.exists(os.path.join(os.getcwd(),'on_the_board')):
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(),'on_the_board'))



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
