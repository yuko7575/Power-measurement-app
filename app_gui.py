################ ライブラリの導入 ####################
import sys
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
###################### 変数 #########################
windowWidth = 1000
windowHeight = 800
##############################################
#class 
################### 画面の設定 ######################
window = tk.Tk() # 画面の表示
window.title("電力測定グラフ") # 画面のタイトル
window.geometry(f"{windowWidth}x{windowHeight}") # 画面の大きさ
window.iconbitmap("./icon/analysis-analytics-graph.ico") # 画面のアイコン

# aaaaaa

window.mainloop() # 画面表示命令