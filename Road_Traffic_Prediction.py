import csv
import pandas as pd

import ast
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import folium
from folium.features import DivIcon
from datetime import datetime
from pytz import timezone 
import json
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def finmethod(date_time):
  file = pd.read_csv("file.csv")
  conn = pd.read_csv("Connected_data.csv")
  data = pd.read_csv("data.csv")
  road_data = file['edgeId']
  col_dat = list(file.columns)
  col_dat = col_dat[1:]
  y_pr = []
  for _ in range(len(road_data)):
    k = file.iloc[_]
    road_links = []
    for i in range(1,len(k)):
      if k[i] == '1':
        road_links.append(i)
    road_cont = len(road_links)
    road_link = []
    for i in range(road_cont):
      road_link.append(road_data[road_links[i]-1])
    edgeids_conn = conn['edgeId']
    len_conn_iloc = data.iloc[1]
    lists = {}
    for i in range(len(road_link)):
      lists[f"list_{i+1}"] = []
    for i in range(len(road_link)):
      temp = "list_" + str(i+1)
      lists[temp] = data.iloc[i]
    fin_list = []
    road_input_dat = data.iloc[_]
    for i in range(1,len(len_conn_iloc)):
      lst = []
      tp = 0
      for i1 in range(len(road_link)):
        temp = 'list_' + str(i1+1)
        if np.isnan(lists[temp][i]):
          tp = 1
          pass
        else:
          lst.append(lists[temp][i])
      if np.isnan(road_input_dat[i]) or tp == 1:
        pass
      else:
        lst.append(road_input_dat[i])
        fin_list.append(lst)
    # print(type(road_data[_]))
    Data = np.array(fin_list)
    X=Y=[]
    X = Data[:,0:len(road_link)]
    Y = Data[:,len(road_link)]
    from sklearn.model_selection import train_test_split
    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 1/4, random_state = 0)
    I_H_WM= np.random.rand(len(road_link),len(road_link))
    C = np.matmul(X_Train,I_H_WM)
    H_O_WH=np.matmul(np.linalg.pinv(C),Y_Train)
    TS_H_OP=np.matmul(X_Test,I_H_WM)
    Y_Pred = np.matmul(TS_H_OP,H_O_WH)
    from sklearn.metrics import mean_squared_error
    RMSE = pow(mean_squared_error(Y_Test,Y_Pred),0.5)
    con = []
    for i in range(len(edgeids_conn)):
      if edgeids_conn[i] == road_data[_]:
        con = conn.iloc[i]
    y_pr.append(Y_Pred[0])
  con_list = list(conn['edge_coordinates'])
  con_lists = []
  for _ in range(len(con_list)):
    con_lists.append(ast.literal_eval(con_list[_]))
  my_map5 = folium.Map(location = [24.6071, 54.8801], zoom_start=9) 
  a2 = []
  now_time = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
  # current_time = now.strftime("%H:%M:%S")
  Edge_id = con_lists
  Connected_Edges = [[(24.454154, 54.390017), (24.455404, 54.391593)], [(24.455517, 54.391751), (24.455877, 54.391985)]]

  for edge in Connected_Edges:
      for i in edge:
          a2.append(i)
  for _ in range(len(Edge_id)):
    folium.PolyLine(locations = Edge_id[_], line_opacity = 2, popup='Edge', tiles='OpenStreetMap',color = "red").add_to(my_map5)
    folium.PolyLine(locations = a2, line_opacity = 2, tiles='OpenStreetMap', popup='Connected_Edges').add_to(my_map5)
    tp = str(y_pr[_])
    html_text = '<div style="font-size: 8pt">' + tp[:5] + '</div>'
    folium.map.Marker(
        list(Edge_id[_][len(Edge_id[_])//2]),
        icon=DivIcon(
            icon_size=(80,10),
            icon_anchor=(0,0),
            html=html_text,
            )
        ).add_to(my_map5)
  my_map5.save('my_map.html')
  list_json = []
  for _ in range(len(Edge_id)):
    ele = {
        "id":road_data[_],
        "speed":y_pr[_]
    }
    list_json.append(ele)
  print(list_json)
  out_file = open('Road_Data.json','w')
  json.dump(list_json,out_file,indent = 4)
  out_file.close()

  return list_json


print(finmethod("26/05/2022 10/20/55"))
