#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import numpy as np
from numpy.lib.stride_tricks import as_strided
import random


class Scenario:
    def __init__(self, location=None, time=None, weather=None, vehicle=None, drivingMode=None):
        self.location = location #[x,y]
        self.time = time #[hour, minute]
        self.weather = weather #string
        self.vehicle = vehicle #string
        self.drivingMode = drivingMode #[drivingMode, setSpeed]

class Dataset:
    def __init__(self, rate=None, frame=None, vehicles=None, peds=None, trafficSigns=None, direction=None, reward=None, 
            throttle=None, brake=None, steering=None, speed=None, yawRate=None, drivingMode=None, location=None, time=None):
        self.rate = rate #Hz
        self.frame = frame #[width, height]
        self.vehicles = vehicles #boolean
        self.peds = peds #boolean
        self.trafficSigns = trafficSigns #boolean
        self.direction = direction #[x,y,z]
        self.reward = reward #[id, p1, p2]
        self.throttle = throttle #boolean
        self.brake = brake #boolean
        self.steering = steering #boolean
        self.speed = speed #boolean
        self.yawRate = yawRate #boolean
        self.drivingMode = drivingMode #boolean
        self.location = location #boolean
        self.time = time #boolean

class Start:
    def __init__(self, scenario=None, dataset=None):
        self.scenario = scenario
        self.dataset = dataset

    def to_json(self):
        _scenario = None
        _dataset = None

        if (self.scenario != None):
            _scenario = self.scenario.__dict__

        if (self.dataset != None):
            _dataset = self.dataset.__dict__            
        #return json.dumps({'mymessage':'HelloWorld2'})
        return json.dumps({'start':{'scenario': _scenario, 'dataset': _dataset}})


class Config:
    def __init__(self, scenario=None, dataset=None):
        self.scenario = scenario
        self.dataset = dataset

    def to_json(self):
        _scenario = None
        _dataset = None

        if (self.scenario != None):
            _scenario = self.scenario.__dict__

        if (self.dataset != None):
            _dataset = self.dataset.__dict__            

        return json.dumps({'config':{'scenario': _scenario, 'dataset': _dataset}})

class Stop:
    def to_json(self):
        return json.dumps({'stop':None}) #super dummy

class Commands:
    def __init__(self, throttle=None, brake=None, steering=None):
        self.throttle = throttle #float (0,1)
        self.brake = brake #float (0,1)
        self.steering = steering #float (-1,1)

    def to_json(self):
        return json.dumps({'commands':self.__dict__})
        
def frame2numpy(frame, frameSize):
    buff = np.fromstring(frame, dtype='uint8')
    # Scanlines are aligned to 4 bytes in Windows bitmaps
    strideWidth = int((frameSize[0] * 3 + 3) / 4) * 4
    # Return a copy because custom strides are not supported by OpenCV.
    return as_strided(buff, strides=(strideWidth, 3, 1), shape=(frameSize[1], frameSize[0], 3)).copy()

class MyMessage:
    def __init__(self, scenario=None, dataset=None):
        self.scenario = scenario
        self.dataset = dataset
        self.i=0
        self.num=0
        self.j=0


    def to_json(self):

        if(self.j>=12):
            self.j=0

        if(self.i>=13):
            self.i=0
            self.j=self.j+1

        self.i=self.i+1

        #side=random.randint(0,1)
        #row=random.randint(0,11)
        #place = random.randint(0, 12)
        color = random.randint(0, 150)
        #model= random.randint(0,12)

        self.num = self.num + 1

        if(self.num<200):
            return json.dumps({'mymessage':{'model':'sultan','row':self.j,'place':self.i-1,'side':0,'color':color,'num':self.num}})
            #return json.dumps({'mymessage': {'model': 'airtug', 'row': row, 'place': place, 'side': side,'color': color, 'num': self.num,'modelnum':model}})
        else:
            #print("Is car in : row",row,"place",place)
            return json.dumps({'iscar': {'row': row, 'place': place}})

class SetCamera:
    def __init__(self):
        self.px=-1660
        self.py=-903
        self.pz=79
        self.rx=-90
        self.ry=0
        self.rz= -40.3241

    def to_json(self):
        return json.dumps({'setcamera':{'px':self.px,'py':self.py,'pz':self.pz,'ry':self.ry,'rz':self.rz,'rz':self.rz}})