from collections import defaultdict

scores = [("Math", "80"), ("Science", "60"), ("Programming", "70"), ("Dance", "10")]
calculate_score = defaultdict(list)



average = 0
for subject, score in scores: 
  average = average + int(score); 
  calculate_score[subject].append(score)


print("test: ", average)
