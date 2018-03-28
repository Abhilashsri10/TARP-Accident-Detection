# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 03:45:06 2018

@author: Abhilash Srivastava
"""
#sms part
import plotly.plotly as py
from plotly.graph_objs import *
import plotly
from plotly.offline import plot
from twilio.rest import Client
def sms():
    account_sid = "ACfb32763b6b8d047b86df7534a70245e0"
    auth_token = "f4e3fd3210a3e056d355d17eec5dad82"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
            to="+918072344306",
            from_="+15024437038 ",
            body="An Accident has occures at the location: (12.9718° N, 79.1589° E) Click the link for location https://goo.gl/maps/uXN9wmh9tMv")


    plotly.tools.set_credentials_file(username='aakashvarma18', api_key='tFCB65mxaAx9tFel2hDf')

    mapbox_access_token = 'pk.eyJ1IjoiYWFrYXNoMTgiLCJhIjoiY2pka21xMzdzMDI1cTMzczN5MG9ic3c0eCJ9.-Jf_342u6cWFfCCAfWMJjQ'

    lats=[12.9718] #12.9718° N, 79.1589° E
    lons=[79.1589]

    plots=[]
    for i,j in zip(lats,lons):
        data = Data([
                Scattermapbox(
                        lat=[str(i)],
                        lon=[str(j)],
                        mode='markers',
                        marker=Marker(
                                size=14
                                ),
                                text=['Accident has occured here, please reash the location as fast as possible'],
                                )
                        ])

        layout = Layout(
                autosize=True,
                hovermode='closest',
                mapbox=dict(
                        accesstoken=mapbox_access_token,
                        bearing=0,
                        center=dict(
                                lat=12.9718,
                                lon=79.1589
                                ),
                                pitch=0,
                                zoom=20
                                ),
                                )
        fig = dict(data=data, layout=layout)
        print (fig)
    plot(fig,"plot.html")

# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
#from math import ceil
# capture frames from a video
cap = cv2.VideoCapture('acc3.mp4')
 
# Trained XML classifiers describes some features of some object we want to detect
direct='C:\\Users\\Abhilash Srivastava\\Desktop\\study materials\\two-way_traffic-monitoring\\two-way_traffic-monitoring\\two_way_traffic\\dataset\\cars.xml'
car_cascade = cv2.CascadeClassifier(direct)
 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars[1:2]:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
    if(len(cars)>2):
        if((cars[0][0])<((cars[2][0])-200) or (cars[0][0])<=(cars[1][0]-156)):
            print('accident')
            #sms()
    # Display frames in a window
    cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Output', 320,240)
    cv2.imshow('output', frames)
    # Wait for Esc key to stop

    if cv2.waitKey(50)==27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()



