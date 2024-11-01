import sys 
from stats import * 
from ezr import * 

# train file 
def train_file(train_file): return DATA().adds(csv(train_file))

# get done rows
def fetch_done(d): return d.activeLearning() 

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
                        r[c.at] += np.random.normal(0, noise_strength)
                    else: # must be an int 
                        r[c.at] += m.ceil(np.random.normal(0, noise_strength)) 
                elif False: # MUST BE A SYM
                    listOfSyms = getAllSyms(data, c) # get possible sym values
                    if(rand.randint(0, 10) < 1): # some low probability that it changes to some class 
                        r[c.at] = rand.choice(listOfSyms)
    return data

# grab todo
def fetch_todo(allRows, done): return [row for row in allRows if row not in done]
    
# fetch actual goals 
def fetch_actual_goals(data): return [{col.at: row[col.at] for col in data.cols.y} for row in data.rows] # actual goals

# fetch predicted goals 
def fetch_predicted_goals(data, done): return [data.predict(row, done, cols=data.cols.y) for row in data.rows] # predicted goals

# construct somes
def construct_somes(data, done, todo):
    return 0

# compare the predictions
def compare_predictions(rows, goals, actualRows, predictedRows):
    result = 0
    for i in range(len(rows)):
        for goal in goals:
            actual_value = actualRows[i][goal.at]
            predicted_value = predictedRows[i][goal.at] 
            #print(f"  Actual: {actual_value}")
            #print(f"  Predicted: {predicted_value}")
            if isinstance(actual_value, (int, float)) and abs(actual_value - predicted_value) < 0.001:
                result += 1
            elif actual_value == predicted_value:
                result += 1
    return result

# compare the predictions
def compare_predictions_distance(rows, goals, actualRows, predictedRows):
    total_distance = 0
    for i in range(len(rows)):
        for goal in goals:
            actual_value = actualRows[i][goal.at]
            predicted_value = predictedRows[i][goal.at] 
            #print(f"  Actual: {actual_value}")
            #print(f"  Predicted: {predicted_value}")
            total_distance += goal.dist1(actual_value, predicted_value)
    return total_distance

# show scott-knott
def scott_knott(data, done, todo):
    # construct somes 
    return 0

# main function
if __name__ == "__main__":
    data = train_file(sys.argv[1]) # puts the .csv file to be trained
    done = fetch_done(data) # snag done
    todo = fetch_todo(data.rows, done) # snag todo
    print(todo)
    actual = fetch_actual_goals(data) # actual goals
    predicted = fetch_predicted_goals(data, done) # predicted goals
    total_goals = len(data.cols.y) * len(data.rows) # get the total number of goals
    print(f"Total goals: {total_goals}")
    number_of_goals = compare_predictions(data.rows, data.cols.y, actual, predicted)
    print(f"Number of correctly assigned goals: {number_of_goals}")
    total_distance = compare_predictions_distance(data.rows, data.cols.y, actual, predicted) # gets the total normalized distance
    print(f"Total distance of all goals (normalized): {total_distance}")
    print(f"Avg of distance {total_distance/total_goals}")
    scott_knott(data, done, todo) # get scott knott and visualizations

# test1: experiment with noise and without noise 

# normal data and see the output 

# significance test - for nonparametric 
