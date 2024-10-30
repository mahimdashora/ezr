import sys
from ezr import *

def fetchdoneandtodo(train_file):
    d = DATA().adds(csv(train_file))
    done = d.activeLearning()
    print(f"Number of done rows: {len(done)}")
    compare_predictions_with_clustering(d, done, d.cols.y)

def compare_predictions_with_clustering(d, done_rows, goals):
    somes = []
    mid1s = stats.SOME(txt="mid-leaf")
    somes.append(mid1s)

    for row in d.rows:
        # Cluster based on the done set
        clusters = d.cluster(done_rows)
        for k in [1, 2, 3, 4, 5]:  # Different k-values for clustering
            ks = stats.SOME(txt=f"k{k}")
            somes.append(ks)
            
            leaf = clusters.leaf(d, row)
            cluster_rows = leaf.data.rows
            predictions = d.predict(row, cluster_rows, k=k)

            # Update stats for comparison
            mid1 = leaf.data.mid()
            for at, pred in predictions.items():
                actual_val = row[at]
                sd = d.cols.all[at].div()
                mid1s.add((actual_val - mid1[at]) / sd)
                ks.add((actual_val - pred) / sd)

    stats.report(somes)

if __name__ == "__main__":
    fetchdoneandtodo(sys.argv[1])
