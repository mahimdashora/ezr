import sys,random #some imports 
from ezr import * #import everything from ezr 

# something that will hold all the data files we will analyze 
Low_dim_data_list = [
"data/optimize/misc/auto93.csv", 
"data/optimize/config/SS-H.csv", 
"data/optimize/config/SS-B.csv",
"data/optimize/config/SS-G.csv",
"data/optimize/config/SS-F.csv",
"data/optimize/config/SS-D.csv",
"data/optimize/config/wc+wc-3d-c4-obj1.csv",
"data/optimize/config/wc+sol-3d-c4-obj1.csv",
"data/optimize/config/wc+rs-3d-c4-obj1.csv",
"data/optimize/config/SS-I.csv",
"data/optimize/config/SS-C.csv",
"data/optimize/config/SS-A.csv",
"data/optimize/config/SS-E.csv",
"data/optimize/hpo/healthCloseIsses12mths0011-easy.csv",
"data/optimize/hpo/healthCloseIsses12mths0001-hard.csv" ] #lowdim dfig/SS-S.csv
""""
fig/Apache_AllMeasurements.csv
fig/SS-P.csv
fig/SS-L.csv
fig/SS-O.csv
c/Wine_quality.csv
cess/pom3d.csv
fig/SS-S.csv
fig/SS-J.csv
fig/SS-K.csv
fig/rs-6d-c3_obj2.csv
fig/rs-6d-c3_obj1.csv
fig/wc-6d-c1-obj1.csv
fig/sol-6d-c2-obj1.csv
fig/SS-X.csv
cess/pom3c.csv
cess/pom3b.csv
cess/pom3a.csv
cess/nasa93dem.csv
fig/SQL_AllMeasurements.csv
fig/SS-U.csv
cess/coc1000.csv
fig/SS-M.csv
fig/X264_AllMeasurements.csv
fig/SS-R.csv
fig/HSMGP_num.csv
fig/SS-Q.csv
cess/xomo_osp2.csv
cess/xomo_osp.csv
cess/xomo_ground.csv
cess/xomo_flight.csv
fig/SS-N.csv
fig/SS-W.csv
fig/SS-V.csv
fig/SS-T.csv
"""
High_dim_data_list = [
    "data/optimize/config/Apache_AllMeasurements.csv",
    "data/optimize/config/SS-P.csv",
    "data/optimize/config/SS-L.csv",
    "data/optimize/config/SS-O.csv",
    "data/optimize/misc/Wine_quality.csv",
    "data/optimize/process/pom3d.csv",
    "data/optimize/config/SS-S.csv",
    "data/optimize/config/SS-J.csv",
    "data/optimize/config/SS-K.csv",
    "data/optimize/config/rs-6d-c3_obj2.csv",
    "data/optimize/config/rs-6d-c3_obj1.csv",
    "data/optimize/config/wc-6d-c1-obj1.csv",
    "data/optimize/config/sol-6d-c2-obj1.csv",
    "data/optimize/config/SS-X.csv",
    "data/optimize/process/pom3c.csv",
    "data/optimize/process/pom3b.csv",
    "data/optimize/process/pom3a.csv",
    "data/optimize/process/nasa93dem.csv",
    "data/optimize/config/SQL_AllMeasurements.csv",
    "data/optimize/config/SS-U.csv",
    "data/optimize/process/coc1000.csv",
    "data/optimize/config/SS-M.csv",
    "data/optimize/config/X264_AllMeasurements.csv",
    "data/optimize/config/SS-R.csv",
    "data/optimize/config/HSMGP_num.csv",
    "data/optimize/config/SS-Q.csv",
    "data/optimize/process/xomo_osp2.csv",
    "data/optimize/process/xomo_osp.csv",
    "data/optimize/process/xomo_ground.csv",
    "data/optimize/process/xomo_flight.csv",
    "data/optimize/config/SS-N.csv",
    "data/optimize/config/SS-W.csv",
    "data/optimize/config/SS-V.csv",
    "data/optimize/config/SS-T.csv"
]


def report():
  
  for data in High_dim_data_list:
    print(f"THE DATA {data} ----")
    for N in (20, 30, 40, 50): # for N in (20,30,40,50)
      somes = []
      # d = DATA().new().csv(data) # d = DATA.new().csv(data)
      d = DATA().adds(csv(data))
      dumb = [guess(N,d) for _ in range(20)] # dumb = [guess(N,d) for _ in range(20)]
      dumb = [d.chebyshev(lst[0]) for lst in dumb] # dumb = [d.chebyshev( lst[0] ) for lst in dumb]
      dumb.sort()  # Sort the dumb results
      
      the.Last = N # the.Last = N
      smart = [d.shuffle().activeLearning() for _ in range(20)] # smart = [d.shuffle().activeLearning() for _ in range(20)]
      smart = [d.chebyshev(lst[0]) for lst in smart] # smart = [d.chebyshev( lst[0] ) for lst in smart]
      smart.sort()
      somes += [stats.SOME(dumb, f"dumb,{N}")]
      
      somes += [stats.SOME(smart, f"smart,{N}")]
      # print the usual files, one file per data set (so the results should have
          # dumb,20
          # dumb,30
          # dumb.40
          # dumb,50
          # smart,20
          # smart,30
          # smart.40
          # smart,50
      stats.report(somes)
    print("------")
def guess(N,d):# function guess(N,d)
    some = random.choices(d.rows, k=N) # pick N rows at random
          # hint some = random.choices(d.rows,k=N)
    return d.clone().adds(some).chebyshevs().rows # sort them on chebyshev
          # hint: d.clone().adds(some).chebyshevs().rows
    # return the rows of some, sorted on chebyshev.
report()
