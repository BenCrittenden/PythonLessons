#Lesson11_ExamStats

#custom functions that calculate the sum, mean, variance and standard deviation
#of a list of numbers called grades.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade
    
print_grades(grades)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  
  print total
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  
  print average
  return average

def grades_variance(grades_input):
  average = grades_average(grades_input)
  variance = 0
  
  for g in grades_input:
    variance += (average - g) ** 2
    
  variance /= float(len(grades_input))
  
  return variance

print grades_variance(grades)

def grades_std_deviation(variance):
  std = variance ** 0.5
  return std

variance = grades_variance(grades)
print grades_std_deviation(variance)