#coding:utf-8

import turtle
import random

#キャンバスを描画
kame = turtle.Turtle()

#カメを描画
kame.shape('turtle')
kame.shapesize(2,2,3)

#カメを初期座標に戻す
kame.home()
kame.clear()
kame.penup()

#200pixelの円を描画
kame.forward(200)
kame.left(90)
kame.pendown()
kame.circle(200)
kame.penup()
kame.home()
kame.pendown()

#カメの自動描画ループ
while True:
	kame.left(random.randint(1,360))
	kame.forward(random.randint(15,50))
	if kame.distance(0,0) > 200:
		kame.undo()

#script end
