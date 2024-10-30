import sys
from ezr import *

def fetch_done_and_todo(train_file):
    d = DATA().adds(csv(train_file))
    done = d.activeLearning()
    print(f"Number of done rows: {len(done)}")
    compare_predictions(d, d.rows, done, d.cols.y)

"""
for each column we will extract if it is a NUM or SYM (we need to know whether to use a regression result or classification)
for each we come up with some accuracy metric. MAYBE: from that we need to combine that for each row to see how "off" it is from the result
we then output these numbers. 
"""
def calculate_accuracy(actual, predicted):
    return None

def compare_predictions(d, rows, labeledRows, goals):
    result = 0
    for row in rows:
        actual = {col.at: row[col.at] for col in goals}
        predicted = d.predict(row, labeledRows, cols=goals)
        print(f"\nRow: {row}")
        for col in goals:
            actual_value = actual[col.at]
            predicted_value = predicted[col.at]   
            print(f"Goal: {col.txt}")
            print(f"  Actual: {actual_value}")
            print(f"  Predicted: {predicted_value}")
            if isinstance(actual_value, (int, float)) and abs(actual_value - predicted_value) < 0.001:
                result += 1
            elif actual_value == predicted_value:
                result += 1
    print(f"Number of Matched Labels: {result}")
    print(f"Total Number of labels: {len(d.rows) * len(d.cols.y)}")


if __name__ == "__main__":
    fetch_done_and_todo(sys.argv[1]) # puts the .csv file to be trained


# implement scott-knot and any visualizations
# 