from ezr import the, DATA, csv, stats
import time
#import numpy as np
from math import exp

#def experiment_for_one_dataset(dataset_path, repeats=20):
dataset_path = "data/optimize/config/SS-A.csv"
repeats=20
d = DATA().adds(csv(dataset_path))
b4 = [d.chebyshev(row) for row in d.rows]
somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]
#Then you need to loop through some options to collect some numbers into a list. This gets added to SOME with a name that identiges the treatment. In the following ,see some +=:

rnd = lambda z: z
scoring_policies = [
  ('exploit', lambda B, R,: B - R),
  ('explore', lambda B, R :  (exp(B) + exp(R))/ (1E-30 + abs(exp(B) - exp(R))))]

for what,how in scoring_policies:
  for the.Last in [0,20, 30, 40]:
    for the.branch in [False, True]:
      start = time.time()
      result = []
      runs = 0
      for _ in range(repeats):
         tmp=d.shuffle().activeLearning(score=how)
         runs += len(tmp)
         result += [rnd(d.chebyshev(tmp[0]))]

      pre=f"{what}/b={the.branch}" if the.Last >0 else "rrp"
      tag = f"{pre},{int(runs/repeats)}"
      print(tag, f": {(time.time() - start) /repeats:.2f} secs")
      somes +=   [stats.SOME(result,    tag)]
pre=f"{what}/b={the.branch}" if the.Last >0 else "rrp"
tag = f"{pre},{int(runs/repeats)}"
somes +=   [stats.SOME(result,    tag)]


stats.report(somes, 0.01)

