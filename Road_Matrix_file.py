import csv
import pandas as pd
import ast
from timeit import default_timer as timer


def file():
  conn = pd.read_csv("connected_data.csv")
  data = pd.read_csv("data.csv")

  edgeids_conn = conn['edgeId']
  conn_edges = conn['connected_edges']

  col_cont_data = len(data['edgeId'])

  # first = edgeids_conn[0]
  # first = ast.literal_eval(first)

  fin = []
  for i in range(col_cont_data):
    lst = []
    lst.append(edgeids_conn[i])
    for _ in range(col_cont_data):
      if edgeids_conn[_] == edgeids_conn[i]:
        lst.append("X")
      elif str(edgeids_conn[_]) in ast.literal_eval(conn_edges[i]):
        lst.append("1")
      elif edgeids_conn[_] in ast.literal_eval(conn_edges[i]):
        lst.append("1")
      else:
        lst.append("-")
    fin.append(lst)
    
  edgeids_con = []
  # edgeids_conn[:0] = ["edgeId"]
  edgeids_con.append("edgeId")

  for _ in edgeids_conn:
    edgeids_con.append(_)

  return edgeids_con,fin

start = timer()
print("Time start:",start)
edgeids_con,fin = file()
print("with CPU:", timer()-start)
new = "file.csv"

with open(new, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(edgeids_con)
    # writing the data rows 
    csvwriter.writerows(fin)


