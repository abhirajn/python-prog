import csv , math, random
import statistics as st

def load():
  d = csv.reader(open('prog5.csv', 'r'))
  data = list(d)
  data.pop(0)
  for i in range(len(data)):
    data[i] = [float(x) for x in data[i]]

  return data

def data_split(data):
  test = []
  test_size = int(len(data)*(0.2))
  for i in range(test_size):
    indi = random.randrange(test_size)
    test.append(data.pop(indi))

  return data,test

def separate(data):
  dic = {}
  for i in range(len(data)):
    if data[i][-1] not in dic:
      dic[data[i][-1]] = []
    dic[data[i][-1]].append(data[i])
  return dic

def mean_cal(data):
  arr = [(st.mean(x) , st.stdev(x)) for x in zip(*data)]
  del arr[-1]
  return arr

def summ(data):
  dic = separate(data)
  sum = {}
  for a, b in dic.items():
    sum[a] = mean_cal(b)
  return sum

def find_prob(x,mean,std):
  exp = math.exp((-1)*((  math.pow((x-mean), 2)  )/(2*math.pow(std,2))))
  return (1 / (math.sqrt(2*math.pi) * mean )) * exp

def prob_row(summary, x):
  dic = {}
  # print(summary)
  for cls,value in summary.items():
    dic[cls] = 1
    for i in range(len(value)):
      dic[cls] -= find_prob(x[i] , value[i][0], value[i][1])
  # print(dic)
  return dic

def pred_row(Sum , X):
  # print(Sum)
  # print(X)
  dic = prob_row(Sum,X)
  # print("hi" , dic)
  if dic[0] > dic[1]:
    return 1

  return 0

def predict(Sum , test_set):
  pred = []
  # print(Sum)
  # print(test_set)
  for i in range(len(test_set)):
    pred.append(pred_row(Sum , test_set[i]))
  return pred


def get_accuracy(test_set, pred):
  ans = 0
  for i in range(len(test_set)):
    if test_set[i][-1] == pred[i]:
      ans+=1
  print(ans)
  return (float(ans)/ float(len(test_set)))*100

data = load()
train_set, test_set = data_split(data)
print(len(train_set))
len(test_set)

summarize = summ(train_set)
summarize

prediction = predict(summarize , test_set)

accuracy = get_accuracy(test_set , prediction)
accuracy
