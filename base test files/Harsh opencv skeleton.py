# # import cv2
# # import multiprocessing
# # cars_lane_1, cars_lane_2,cars_lane_3,cars_lane_4,set_lane_1,set_lane_2,set_lane_3,set_lane_4 = 0,0,0,0,4,4,4,4
# # lane_order=[]
# # flag1,flag2,flag3,flag4=0,0,0,0
# # threshold=15
# # car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect
# #
# #
# # class Harsh:
# #     global cars_lane_1
# #     global set_lane_1
# #     global cars_lane_2
# #     global set_lane_2
# #     global cars_lane_3
# #     global set_lane_3
# #     global cars_lane_4
# #     global set_lane_4
# #
# #     def lane_check_1(self,q1,fg1):
# #         global cars_lane_1
# #         global set_lane_1
# #         global cars_lane_2
# #         global set_lane_2
# #         global cars_lane_3
# #         global set_lane_3
# #         global cars_lane_4
# #         global set_lane_4
# #         set_lane_1=set()
# #         cap = cv2.VideoCapture(0)
# #
# #         while True:
# #             ret, frames = cap.read()                                    # reads frames from a video
# #             gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
# #             cars = car_cascade.detectMultiScale(gray, 1.1, 1)
# #             cars_lane_1=len(cars)
# #             set_lane_1.add(cars_lane_1)
# #             q1.put(max(set_lane_1))
# #         ######################################################################### last commit made a list to store max value
# #             for (x,y,w,h) in cars:
# #                 cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
# #
# #             cv2.imshow('video2', frames)                                # Display frames in a window
# #             if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold: #threshold ki jagah 10 dala hai
# #                 break
# #         fg1.put(1)
# #         cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
# #
# #     def lane_check_2(self,q2,fg2):
# #         global cars_lane_1
# #         global set_lane_1
# #         global cars_lane_2
# #         global set_lane_2
# #         global cars_lane_3
# #         global set_lane_3
# #         global cars_lane_4
# #         global set_lane_4
# #         set_lane_2=set()
# #         cap = cv2.VideoCapture('videos/jan28.avi')
# #
# #         while True:
# #             ret, frames = cap.read()                                    # reads frames from a video
# #             gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
# #             cars = car_cascade.detectMultiScale(gray, 1.1, 1)
# #             cars_lane_2=len(cars)
# #             set_lane_2.add(cars_lane_2)
# #             q2.put(max(set_lane_2))
# #         ###############################################################commit change 2
# #             for (x,y,w,h) in cars:
# #                 cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
# #             cv2.imshow('video2', frames)                                # Display frames in a window
# #             if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:   #threshold ki jagah 10 dala hai                                   # Wait for Esc key to stop
# #                 break
# #         fg2.put(1)
# #         cv2.destroyAllWindows()                                         # De-allocate any associated memory usag
# #
# #     def lane_check_3(self,q3,fg3):
# #         global cars_lane_1
# #         global set_lane_1
# #         global cars_lane_2
# #         global set_lane_2
# #         global cars_lane_3
# #         global set_lane_3
# #         global cars_lane_4
# #         global set_lane_4
# #         set_lane_3=set()
# #         cap = cv2.VideoCapture('videos/march9.avi')
# #
# #         while True:
# #             ret, frames = cap.read()                                    # reads frames from a video
# #             gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
# #             cars = car_cascade.detectMultiScale(gray, 1.1, 1)
# #             cars_lane_3=len(cars)
# #             set_lane_3.add(cars_lane_3)
# #             print(max(set_lane_3))
# #             q3.put(max(set_lane_3))
# #
# #
# #             for (x,y,w,h) in cars:
# #                 cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
# #
# #             cv2.imshow('video2', frames)                                # Display frames in a window
# #             if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:            #threshold ki jagah 10 dala hai                       # Wait for Esc key to stop
# #                 break
# #         fg3.put(1)
# #         cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
# #
# #     def lane_check_4(self,q4,fg4):
# #         global cars_lane_1
# #         global set_lane_1
# #         global cars_lane_2
# #         global set_lane_2
# #         global cars_lane_3
# #         global set_lane_3
# #         global cars_lane_4
# #         global set_lane_4
# #         set_lane_4=set()
# #         cap = cv2.VideoCapture('videos/april21.avi')
# #
# #         while True:
# #             ret, frames = cap.read()                                    # reads frames from a video
# #             gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
# #             cars = car_cascade.detectMultiScale(gray, 1.1, 1)
# #             cars_lane_4=len(cars)
# #             set_lane_4.add(cars_lane_4)
# #             q4.put(max(set_lane_4))
# #             print(max(set_lane_4))
# #
# #             for (x,y,w,h) in cars:
# #                 cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
# #
# #             cv2.imshow('video2', frames)                                # Display frames in a window
# #             if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold or max(set_lane_2)>threshold or max(set_lane_1)>threshold or max(set_lane_4)>threshold:            #threshold ki jagah 10 dala hai                       # Wait for Esc key to stop
# #                 break
# #         fg4.put(1)
# #         cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
# #
# #
# # if __name__ == '__main__':
# #     h=Harsh()
# #     q1=multiprocessing.Queue()
# #     q2 = multiprocessing.Queue()
# #     q3 = multiprocessing.Queue()
# #     q4 = multiprocessing.Queue()
# #     fg1 = multiprocessing.Queue()
# #     fg2 = multiprocessing.Queue()
# #     fg3 = multiprocessing.Queue()
# #     fg4 = multiprocessing.Queue()
# #
# #     process1=multiprocessing.Process(target=h.lane_check_1,args=(q1,fg1,))
# #     process2=multiprocessing.Process(target=h.lane_check_2,args=(q2,fg2,))
# #     process3=multiprocessing.Process(target=h.lane_check_3,args=(q3,fg3,))
# #     process4=multiprocessing.Process(target=h.lane_check_4,args=(q4,fg4,))
# #     process1.start(),process2.start(), process3.start(), process4.start()
# #     flag1 = fg1.get()
# #     flag2 = fg2.get()
# #     flag3 = fg3.get()
# #     flag4 = fg4.get()
# #
# #     if flag1==1 or flag2==1 or flag3==1 or flag4==1:
# #
# #         process1.terminate()
# #         process2.terminate()
# #         process3.terminate()
# #         process4.terminate()
# #         print("hello")
# #         print(q4.get())
# #         lane_order.append(q1.get())
# #         lane_order.append(q2.get())
# #         lane_order.append(q3.get())
# #         lane_order.append(q4.get())
# #
# # '''flag updation to be performed'''
# #
# import cv2,multiprocessing,time,math
# import RPi.GPIO as GPIO
# cars_lane_1, cars_lane_2,cars_lane_3,cars_lane_4,set_lane_1,set_lane_2,set_lane_3,set_lane_4,flag1,flag2,flag3,flag4 = 0,0,0,0,0,0,0,0,0,0,0,0
# lane_order=[]
# threshold=16
# car_cascade = cv2.CascadeClassifier('cars121004.xml')           # Trained XML classifiers describes some features of some object we want to detect
# initial_timer_1,initial_timer_2,initial_timer_3,initial_timer_4=40,40,40,40
#
# def lane_check_1(q1,fg1,order):
#     global cars_lane_1,set_lane_1
#     set_lane_1=set()
#     cap = cv2.VideoCapture(0)
#     t_end=time.time()+10
#     queue_value=0
#
#
#     while True:
#         ret, frames = cap.read()                                    # reads frames from a video
#         gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
#         cars = car_cascade.detectMultiScale(gray, 1.1, 1)
#         cars_lane_1=len(cars)
#         set_lane_1.add(cars_lane_1)
#
#         for (x,y,w,h) in cars:
#             cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
#
#         cv2.imshow('video2', frames)                                # Display frames in a window
#         if cv2.waitKey(33) == 27 or max(set_lane_1)>threshold:                              #threshold ki jagah 10 dala hai
#             queue_value=1
#             order.put(1)
#             break
#         elif time.time()>=t_end:
#             order.put(0)
#             break
#     q1.put(max(set_lane_1))
#     fg1.put(queue_value)
#     cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
#
#
# def lane_check_2(q2,fg2,order):
#     global cars_lane_2, set_lane_2
#     set_lane_2=set()
#     cap = cv2.VideoCapture('videos/jan28.avi')
#     t_end=time.time()+10
#     queue_value=0
#     while True:
#         ret, frames = cap.read()                                    # reads frames from a video
#         gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
#         cars = car_cascade.detectMultiScale(gray, 1.1, 1)
#         cars_lane_2=len(cars)
#         set_lane_2.add(cars_lane_2)
#
#         for (x, y,w,h) in cars:
#             cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.imshow('video2', frames)                                # Display frames in a window
#         if cv2.waitKey(33) == 27 or max(set_lane_2)>threshold:                                # Wait for Esc key to stop
#             queue_value=1
#             order.put(2)
#             break
#         elif time.time()>=t_end:
#             order.put(0)
#             break
#     q2.put(max(set_lane_2))
#     fg2.put(queue_value)
#     cv2.destroyAllWindows()                                         # De-allocate any associated memory usag
#
#
# def lane_check_3(q3,fg3,order):
#     global cars_lane_3, set_lane_3
#     set_lane_3=set()
#     cap = cv2.VideoCapture('videos/march9.avi')
#     t_end = time.time() + 10
#     queue_value=0
#     while True:
#         ret, frames = cap.read()                                    # reads frames from a video
#         gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
#         cars = car_cascade.detectMultiScale(gray, 1.1, 1)
#         cars_lane_3=len(cars)
#         set_lane_3.add(cars_lane_3)
#
#         for (x,y,w,h) in cars:
#             cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.imshow('video2', frames)                                # Display frames in a window
#         if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold:                       # Wait for Esc key to stop
#             queue_value=1
#             order.put(3)
#             break
#         elif time.time()>=t_end:
#             order.put(0)
#             break
#     q3.put(max(set_lane_3))
#     fg3.put(queue_value)
#     cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
#
#
# def lane_check_4(q4,fg4,order):
#     global cars_lane_4,set_lane_4
#     set_lane_4=set()
#     cap = cv2.VideoCapture('videos/april21.avi')
#     t_end = time.time() + 10
#     queue_value=0
#     while True:
#         ret, frames = cap.read()                                    # reads frames from a video
#         gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
#         cars = car_cascade.detectMultiScale(gray, 1.1, 1)
#         cars_lane_4=len(cars)
#         set_lane_4.add(cars_lane_4)
#
#         for (x,y,w,h) in cars:
#             cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
#
#         cv2.imshow('video2', frames)                                # Display frames in a window
#         if cv2.waitKey(33) == 27 or max(set_lane_4)>threshold:      # Wait for Esc key to stop
#             queue_value=1
#             order.put(4)
#             break
#         elif time.time()>=t_end:
#             order.put(0)
#             break
#     q4.put(max(set_lane_4))
#     fg4.put(queue_value)
#     cv2.destroyAllWindows()                                         # De-allocate any associated memory usage
#
#
# def light_lane_1(initial_timer1=40):
#     initial_timer_1= time.time()+initial_timer1
#     GPIO.cleanup()
#     GPIO.setmode(GPIO.BOARD)
#     LED = 11
#     GPIO.setup(LED, GPIO.OUT)
#     while time.time()<initial_timer_1:
#         GPIO.output(LED,True)
#         time.sleep(1)
#     GPIO.cleanup()
#
# def light_lane_2(initial_timer2=40):
#     initial_timer_2 = time.time() + initial_timer2
#     GPIO.cleanup()
#     GPIO.setmode(GPIO.BOARD)
#     LED = 12
#     GPIO.setup(LED, GPIO.OUT)
#     while time.time() < initial_timer_2:
#         GPIO.output(LED, True)
#         time.sleep(1)
#     GPIO.cleanup()
#
# def light_lane_3(initial_timer3=40):
#     initial_timer_3 = time.time() + initial_timer3
#     GPIO.cleanup()
#     GPIO.setmode(GPIO.BOARD)
#     LED = 13
#     GPIO.setup(LED, GPIO.OUT)
#     while time.time() < initial_timer_3:
#         GPIO.output(LED, True)
#         time.sleep(1)
#     GPIO.cleanup()
#
# def light_lane_4(initial_timer4=40):
#     initial_timer_4 = time.time() + initial_timer4
#     GPIO.cleanup()
#     GPIO.setmode(GPIO.BOARD)
#     LED = 14
#     GPIO.setup(LED, GPIO.OUT)
#     while time.time() < initial_timer_4:
#         GPIO.output(LED, True)
#         time.sleep(1)
#     GPIO.cleanup()
#
#
# def red_light(initial_timer_r=40):
#     initial_timer_red = time.time() + initial_timer_r
#     GPIO.cleanup()
#     GPIO.setmode(GPIO.BOARD)
#     LED = 15
#     GPIO.setup(LED, GPIO.OUT)
#     while time.time() < initial_timer_red:
#         GPIO.output(LED, True)
#         time.sleep(1)
#     GPIO.cleanup()
#
#
#
# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         value = manager.list()
#         q1 = multiprocessing.Queue()
#         q2 = multiprocessing.Queue()
#         q3 = multiprocessing.Queue()
#         q4 = multiprocessing.Queue()
#         fg1 = multiprocessing.Queue()
#         fg2 = multiprocessing.Queue()
#         fg3 = multiprocessing.Queue()
#         fg4 = multiprocessing.Queue()
#         order = multiprocessing.Queue()
#
#         while True:
#             process5 = multiprocessing.Process(target=light_lane_1, args=())
#             process6 = multiprocessing.Process(target=light_lane_2, args=())
#             process7 = multiprocessing.Process(target=light_lane_3, args=())
#             process8 = multiprocessing.Process(target=light_lane_4, args=())
#             process1 = multiprocessing.Process(target=lane_check_1,args=(q1,fg1,order,))
#             process2 = multiprocessing.Process(target=lane_check_2,args=(q2,fg2,order,))
#             process3 = multiprocessing.Process(target=lane_check_3,args=(q3,fg3,order,))
#             process4 = multiprocessing.Process(target=lane_check_4,args=(q4,fg4,order,))
#             process1.start(),process2.start(), process3.start(), process4.start()
#             flag1 = fg1.get()
#             flag2 = fg2.get()
#             flag3 = fg3.get()
#             flag4 = fg4.get()
#
#             a1,a2,a3,a4=q1.get(),q2.get(),q3.get(),q4.get()
#
#             print(flag1,flag2,flag3,flag4)
#             process1.terminate()
#             process2.terminate()
#             process3.terminate()
#             process4.terminate()
#             lane_order.append(a1)
#             lane_order.append(a2)
#             lane_order.append(a3)
#             lane_order.append(a4)
#
#             if a1==0:
#                 a1=1
#             elif a2==0:
#                 a2=1
#             elif a3==0:
#                 a3=0
#             elif a4==0:
#                 a4=1
#             else:
#                 pass
#
# ###########################################################################################################
#
#             """VALUE UPDATES"""
#
#             value_1=a1/ (a1+a2+a3+a4)
#             value_2 = a2 / (a1 + a2 + a3 + a4)
#             value_3 = a3 / (a1 + a2 + a3 + a4)
#             value_4 = a4 / (a1 + a2 + a3 + a4)
#             update_1 = initial_timer_1 + initial_timer_1 * value_1 * (math.log(value_1/0.25 , 10))
#             update_2 = initial_timer_2 + initial_timer_2 * value_2 * (math.log(value_2/0.25 , 10))
#             update_3 = initial_timer_3 + initial_timer_3 * value_3 * (math.log(value_3/0.25 , 10))
#             update_4 = initial_timer_4 + initial_timer_4 * value_4 * (math.log(value_4/0.25 , 10))
#             initial_timer_1=update_1
#             initial_timer_2=update_2
#             initial_timer_3=update_3
#             initial_timer_4=update_4
#
# ###########################################################################################################
#
#             print(update_1,update_2,update_3,update_4)
#             for i in range(order.qsize()):
#                 z=order.get()
#                 print("value is ",z)
#                 if z == 1:
#                     process9 = multiprocessing.Process(target=red_light, args=())
#                     process9.start()
#                     light_lane_1(update_1)
#                     process9.join()
#                     process9.terminate()
#                 elif z == 2:
#                     process9 = multiprocessing.Process(target=red_light, args=())
#                     process9.start()
#                     light_lane_1(update_2)
#                     process9.join()
#                     process9.terminate()
#                 elif z == 3:
#                     process9 = multiprocessing.Process(target=red_light, args=())
#                     process9.start()
#                     light_lane_1(update_3)
#                     process9.join()
#                     process9.terminate()
#                 elif z == 4:
#                     process9 = multiprocessing.Process(target=red_light, args=())
#                     process9.start()
#                     light_lane_1(update_4)
#                     process9.join()
#                     process9.terminate()
#                 else :
#                     pass
#                 print(lane_order)
#                 print(lane_order.index(max(lane_order)))
#
# ###################################################################################################################
#
# '''flag updation to be performed'''
#
# # LANE DETECTION PARTIALLY PERFORMED INSTEAD OF FLAG PUSH IN QUEUE AND GET BACK VALUES
#
# # LANE DETECTION DONE LANE TIMER PARTIALLY PERFORMED
# # VALUE UPDATE LEFT
#
#
# # Make sure program raspberry pi GPIO in accordance to the timer values of specific function
#
# # REFER GPIO PROGRAMMING OF RASPBERRY PI FOR LIGHT BLINKING

import cv2,multiprocessing,time,math
import RPi.GPIO as GPIO
number_of_cars=[]
threshold=16
initial_timer_1,initial_timer_2,initial_timer_3,initial_timer_4=40,40,40,40
car_cascade = cv2.CascadeClassifier('cars121004.xml')     #CARS CLASSIFIER


def lane_check_1(q1,fg1,order):
    set_lane_1=set()
    cap = cv2.VideoCapture(0)
    t_end=time.time()+20
    queue_value=0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_1=len(cars)
        set_lane_1.add(cars_lane_1)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_1)>threshold:                              #threshold ki jagah 10 dala hai
            queue_value=1
            order.put(1)
            break
        elif time.time()>=t_end:
            #order.put(0)
            break
    q1.put(max(set_lane_1))
    fg1.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def lane_check_2(q2,fg2,order):
    set_lane_2=set()
    cap = cv2.VideoCapture('videos/jan28.avi')
    t_end=time.time()+20
    queue_value=0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_2=len(cars)
        set_lane_2.add(cars_lane_2)

        for (x, y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_2)>threshold:                                # Wait for Esc key to stop
            queue_value=1
            order.put(2)
            break
        elif time.time()>=t_end:
            #order.put(0)
            break
    q2.put(max(set_lane_2))
    fg2.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usag


def lane_check_3(q3,fg3,order):
    set_lane_3=set()
    cap = cv2.VideoCapture('videos/march9.avi')
    t_end = time.time() + 20
    queue_value=0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_3=len(cars)
        set_lane_3.add(cars_lane_3)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_3)>threshold:                       # Wait for Esc key to stop
            queue_value=1
            order.put(3)
            break
        elif time.time()>=t_end:
            #order.put(0)
            break
    q3.put(max(set_lane_3))
    fg3.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def lane_check_4(q4,fg4,order):
    set_lane_4=set()
    cap = cv2.VideoCapture('videos/april21.avi')
    t_end = time.time() + 20
    queue_value=0
    while True:
        ret, frames = cap.read()                                    # reads frames from a video
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars_lane_4=len(cars)
        set_lane_4.add(cars_lane_4)

        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('video2', frames)                                # Display frames in a window
        if cv2.waitKey(33) == 27 or max(set_lane_4)>threshold:      # Wait for Esc key to stop
            queue_value=1
            order.put(4)
            break
        elif time.time()>=t_end:
            #order.put(0)
            break
    q4.put(max(set_lane_4))
    fg4.put(queue_value)
    cv2.destroyAllWindows()                                         # De-allocate any associated memory usage


def algorithm(a1,a2,a3,a4):                          # FUNCTION FOR ALGORITHM
    global initial_timer_1,initial_timer_2,initial_timer_3,initial_timer_4
    value_1 = a1 / (a1 + a2 + a3 + a4)
    value_2 = a2 / (a1 + a2 + a3 + a4)
    value_3 = a3 / (a1 + a2 + a3 + a4)
    value_4 = a4 / (a1 + a2 + a3 + a4)
    update_1 = initial_timer_1 + initial_timer_1 * value_1 * (math.log(value_1 / 0.25, 10))
    update_2 = initial_timer_2 + initial_timer_2 * value_2 * (math.log(value_2 / 0.25, 10))
    update_3 = initial_timer_3 + initial_timer_3 * value_3 * (math.log(value_3 / 0.25, 10))
    update_4 = initial_timer_4 + initial_timer_4 * value_4 * (math.log(value_4 / 0.25, 10))
    initial_timer_1 = update_1
    initial_timer_2 = update_2
    initial_timer_3 = update_3
    initial_timer_4 = update_4
    return initial_timer_1,initial_timer_2,initial_timer_3,initial_timer_4


def normal_timer(z):
    z = z + 1
    if z >= 40:
        z = 0
    if z % 4 == 1:
        print("lane1 green baaki saare red")
        normal_time_lane_1 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        LED = 11
        GPIO.setup(LED, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        while time.time() < normal_time_lane_1:
            GPIO.output(LED, True)
            GPIO.output(22, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            time.sleep(1)
        GPIO.cleanup()

    elif z % 4 == 2:
        print("lane2 green baaki saare red")
        normal_time_lane_2 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        LED = 13
        GPIO.setup(LED, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        while time.time() < normal_time_lane_2:
            GPIO.output(LED, True)
            GPIO.output(18, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            time.sleep(1)
        GPIO.cleanup()

    elif z % 4 == 3:
        print("lane3 green baaki saare red")
        normal_time_lane_3 = time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        LED = 15
        GPIO.setup(LED, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        while time.time() < normal_time_lane_3:
            GPIO.output(LED, True)
            GPIO.output(18, True)
            GPIO.output(22, True)
            GPIO.output(36, True)
            time.sleep(1)
        GPIO.cleanup()

    else:
        print("lane 4 green baaki saare red")
        normal_time_lane_4= time.time() + 40
        GPIO.setmode(GPIO.BOARD)
        LED = 16
        GPIO.setup(LED, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        while time.time() < normal_time_lane_4:
            GPIO.output(LED, True)
            GPIO.output(18, True)
            GPIO.output(22, True)
            GPIO.output(32, True)
            time.sleep(1)
        GPIO.cleanup()


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        value = manager.list()
        q1 = multiprocessing.Queue()
        q2 = multiprocessing.Queue()
        q3 = multiprocessing.Queue()
        q4 = multiprocessing.Queue()
        fg1 = multiprocessing.Queue()
        fg2 = multiprocessing.Queue()
        fg3 = multiprocessing.Queue()
        fg4 = multiprocessing.Queue()
        order = multiprocessing.Queue()

        while True:
            process1 = multiprocessing.Process(target=lane_check_1,args=(q1,fg1,order,))
            process2 = multiprocessing.Process(target=lane_check_2,args=(q2,fg2,order,))
            process3 = multiprocessing.Process(target=lane_check_3,args=(q3,fg3,order,))
            process4 = multiprocessing.Process(target=lane_check_4,args=(q4,fg4,order,))
            process1.start(),process2.start(), process3.start(), process4.start()
            flag1 = fg1.get()
            flag2 = fg2.get()
            flag3 = fg3.get()
            flag4 = fg4.get()

            a1, a2, a3, a4 = q1.get(), q2.get(), q3.get(), q4.get()

            print(flag1, flag2, flag3, flag4)
            process1.terminate()
            process2.terminate()
            process3.terminate()
            process4.terminate()

            if a1 == 0:
                a1 = 1
            elif a2 == 0:
                a2 = 1
            elif a3 == 0:
                a3 = 0
            elif a4 == 0:
                a4 = 1
            else:
                pass

            number_of_cars.append(a1)
            number_of_cars.append(a2)
            number_of_cars.append(a3)
            number_of_cars.append(a4)
            print(number_of_cars)
            time1,time2,time3,time4=algorithm(a1,a2,a3,a4)

            print(algorithm(a1,a2,a3,a4))
            z = 0
            for i in range(order.qsize()):
                z = order.get()
                print("value is ", z)
                if z == 1:
                    time_1 = time.time() + time1
                    GPIO.setmode(GPIO.BOARD)
                    LED = 11
                    GPIO.setup(LED, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_1:
                        GPIO.output(LED, True)
                        GPIO.output(22, True)
                        GPIO.output(32, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                    GPIO.cleanup()
                    print("green on lane 1")
                    print("red on other lanes")

                elif z == 2:
                    time_2 = time.time() + time2
                    GPIO.setmode(GPIO.BOARD)
                    LED = 13
                    GPIO.setup(LED, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_2:
                        GPIO.output(LED, True)
                        GPIO.output(18, True)
                        GPIO.output(32, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                    GPIO.cleanup()
                    # print("green on lane 2")
                    # print("red on other lanes")

                elif z == 3:
                    time_3 = time.time() + time3
                    GPIO.setmode(GPIO.BOARD)
                    LED = 15
                    GPIO.setup(LED, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(36, GPIO.OUT)
                    while time.time() < time_3:
                        GPIO.output(LED, True)
                        GPIO.output(18, True)
                        GPIO.output(22, True)
                        GPIO.output(36, True)
                        time.sleep(1)
                    GPIO.cleanup()
                    # print("green on lane 3")
                    # print("red on other lanes")

                elif z == 4:
                    time_4 = time.time() + time4
                    GPIO.setmode(GPIO.BOARD)
                    LED = 16
                    GPIO.setup(LED, GPIO.OUT)
                    GPIO.setup(22, GPIO.OUT)
                    GPIO.setup(18, GPIO.OUT)
                    GPIO.setup(32, GPIO.OUT)
                    while time.time() < time_4:
                        GPIO.output(LED, True)
                        GPIO.output(18, True)
                        GPIO.output(22, True)
                        GPIO.output(32, True)
                        time.sleep(1)
                    GPIO.cleanup()
                    # print("green on lane 4")
                    # print("red on other lanes")
            else:
                normal_timer(z)
                print("function call back to processing")

"""YAAD RAKHNA KI 4 FUNCTIONS BANANE HAI AND HAR FUNCTION ME RESPECTIVE GREEN KARKE BAAKI SAARE RED KARNE HAI"""
