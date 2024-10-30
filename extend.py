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


import sys
# from ezr import *

# def fetchdoneandtodo(train_file):
#     d = DATA().adds(csv(train_file))
#     done = d.activeLearning()
#     print(f"Number of done rows: {len(done)}")

#     # Step 1: Create initial clusters based on the `done` set
#     clusters = d.cluster(done, sortp=True)  # Using `done` rows to initialize clusters

#     # Step 2: Assign each row in `d.rows` to the nearest cluster
#     for row in d.rows:
#         # Find the closest cluster based on distance
#         #closest_cluster = min(clusters.nodes(), key=lambda cluster: d.dist(row, cluster.mid))
#         #closest_cluster = min((node.mid for node, leafp in clusters.nodes() if leafp),key=lambda mid: d.dist(row, mid))
#         closest_cluster = min((node for node, leafp in clusters.nodes() if leafp), key=lambda node: d.dist(row, node.mid))
#         closest_cluster.data.add(row)  # Add this row to the closest cluster

#     # Step 3: Compare predictions or other metrics for accuracy
#     compare_predictions(d, d.rows, done, d.cols.y)

#     # # Print statistics for each cluster
#     # for cluster_id, cluster in enumerate(clusters.nodes()):
#     #     print(f"\nCluster {cluster_id + 1}")
#     #     stats.report(cluster.data.somes)  # Show cluster statistics
#     # Now report the statistics for each cluster
#     for node, leafp in clusters.nodes():
#         if leafp:  # Only if it's a leaf node
#             if hasattr(node, 'data'):  # Check if node has data attribute
#                 # Assuming 'somes' should be within the node's data or similar structure
#                 stats.report(node.data.somes if hasattr(node.data, 'somes') else [])
#             else:
#                 print("Node has no data attribute")  # Debugging output

# def calculate_accuracy(actual, predicted):
#     # Add your accuracy calculation method here as needed
#     return None

# def compare_predictions(d, rows, labeledRows, goals):
#     result = 0
#     for row in rows:
#         actual = {col.at: row[col.at] for col in goals}
#         predicted = d.predict(row, labeledRows, cols=goals)
#         print(f"\nRow: {row}")
#         for col in goals:
#             actual_value = actual[col.at]
#             predicted_value = predicted[col.at]
#             print(f"Goal: {col.txt}")
#             print(f"  Actual: {actual_value}")
#             print(f"  Predicted: {predicted_value}")
#             if isinstance(actual_value, (int, float)) and abs(actual_value - predicted_value) < 0.001:
#                 result += 1
#             elif actual_value == predicted_value:
#                 result += 1
#     print(f"Number of Matched Labels: {result}")
#     print(f"Total Number of labels: {len(d.rows) * len(d.cols.y)}")

# if __name__ == "__main__":
#     fetchdoneandtodo(sys.argv[1])  # Pass the .csv file to be trained
