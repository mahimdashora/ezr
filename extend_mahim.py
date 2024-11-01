import sys
from ezr import *
import numpy as np
import math as m
import random as rand
from collections import Counter

def add_noise_to_data(data, noise_strength):
    # Loop through each row and cell in the data
    #print("hello")
    for r in data.rows:
        for c in data.cols.x:
            if r[c.at] != "?":
                if c.txt[0].isupper() and c.txt[-1]!="X": # checks if NUM
                    #print(f"  c's {c.txt[0]} {c.txt[-1]}")
                    # Add Gaussian noise to each cell
                    if isinstance(r[c.at], (float)): # its a float
                        r[c.at] += r[c.at]*np.random.normal(0, noise_strength)
                    else: # must be an int 
                        r[c.at] += m.ceil(r[c.at]*np.random.normal(0, noise_strength)) 
                elif False: # MUST BE A SYM
                    listOfSyms = getAllSyms(data, c) # get possible sym values
                    if(rand.randint(0, 10) < 1): # some low probability that it changes to some class 
                        r[c.at] = rand.choice(listOfSyms)
    return data


def getAllSyms(data, c):
    unique_values = set()  # Set to store unique symbols

    # Loop through rows and collect unique symbols for the column `c`
    for r in data.rows:
        value = r[c.at]
        if value != "?":  # Exclude missing values
            unique_values.add(value)

    return list(unique_values)  # Convert to list if needed


"""def getAllSyms(columns, c):
    for q in columns: 
        print(q)
    return 0"""


def fetchdoneandtodo(train_file,noise=0):
    d = DATA().adds(csv(train_file))
    #print(f"Data before: {d.rows[:5]}")
    #print(noise)
    #print(noise > 0)
    #print(isinstance(noise, (float)))
    if noise > 0:
        d=add_noise_to_data(d,noise)
    #print(f"Data After: {d.rows[:5]}")
    done = d.activeLearning()
    #print(f"Number of done rows: {len(done)}")
    #compare_predictions_with_clustering(d, done, d.cols.y)
    todo=fetch_todo(d.rows,done)
    #print(f"D cols: {d.cols.y}")
    clusters2(d,done,todo)

def fetch_todo(allRows, done): return [row for row in allRows if row not in done]

def clusters2(d,done,todo):
    somes  = []
    mid1s  = stats.SOME(txt="mid-leaf")
    #mid0s  = stats.SOME(txt="mid-all")
    somes += [mid1s]
    for k in [1,2,3,4,5]:
        ks   = stats.SOME(txt=f"k{k}")
        somes += [ks]
        #for _ in range(len(d.rows)):
        #for train,test in xval(d.rows):
        #all = d.clone(done)
        cluster = d.cluster(done)
        #d1 = d.clone(done)
        #mid0  = d1.mid()
        
        for want in todo:
         
          #for col in d1.cols.y: mid0s.add((mid0[col.at] - want[col.at])/col.div()) 
          leaf = cluster.leaf(d, want)#leaf is closest cluster to that want row
          rows = leaf.data.rows
          got  = d.predict(want, rows, k=k) 
          mid1  = leaf.data.mid()
          for at,got1 in got.items():
            sd = d.cols.all[at].div()
            mid1s.add(abs(want[at] - mid1[at])/sd)
            ks.add(  abs(want[at] - got1   )/sd)
    stats.report(somes)
    # print(f"accuracy: {accuracy(d)}") # print accuracy

"""
 NOTE: THIS IDEA IS NOT WORKING
"""
def accuracy(d):
    correct = 0  # To count correctly labeled rows
    total = 0    # To count all rows

    # iterate through every label
    for label in d.cols.y:
        print(f"label_index: {label}")

        # Traverse nodes, focusing on leaf clusters
        root_cluster = d.cluster()
        for node, is_leaf in root_cluster.nodes():
            if is_leaf:
                # Extract labels in the target column for the leaf node
                labels = [row[label.at] for row in node.data.rows if row[label.at] != "?"]
                print(f"labels: {labels}")
                # Find the most common label and count correct matches
                if labels:
                    most_common_label, count = Counter(labels).most_common(1)[0]
                    correct += count
                    total += len(labels)

        # Calculate accuracy as the proportion of correctly labeled rows
        accuracy = correct / total if total > 0 else 0
    return accuracy

if __name__ == "__main__":
    fetchdoneandtodo(sys.argv[1],float(sys.argv[2]))
