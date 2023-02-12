# -*- coding: utf-8 -*-
"""fun.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1abN9uR52lVld32H4lr3lnFjbt3UofT4X
"""

# LEVEL 1 (solar-doomsday)


import numpy as np
import math


# better: dont go through whole sequence, round down to integer immediately
def find_next_square(valid_area):
    for curr in range(valid_area, 0, -1):
      curr_root = math.sqrt(curr)
      if curr_root == int(curr_root):
        return curr


def solution(area):
  squares = []
  remaining_area = area

  while remaining_area > 0:
    found_square = find_next_square(remaining_area)
    squares.append(found_square)
    remaining_area = remaining_area - found_square

  return squares

'''
#v_solution = np.vectorize(solution)

areas = np.arange(1, 13, 1)
print('inputs', areas)

#v_solution(areas);

for _, a in enumerate(areas):
  print('FIN!', solution(a))

#print('FIN!', result)

maximum = 999999#1000000
solution(maximum)
'''

# LEVEL 2, Task 1 (elevator-meintenance)


from functools import cmp_to_key


def solution(l):
  # 2darray
  version_numbers = [[int(nr) for nr in version.split('.')] for version in l]
  version_numbers = [augment(item) for item in version_numbers]
  # sort
  version_numbers_sorted = sorted(version_numbers, key=cmp_to_key(compare))

  # concatenate
  result = [[str(item) for item in version if item != -1] for version in version_numbers_sorted]
  result = ['.'.join(item) for item in result]

  return result


def compare(item1, item2):
  # compare major
  major = item1[0] - item2[0]

  if major == 0:
    # compare minor
    minor = item1[1] - item2[1]

    if minor == 0:
      # compare revision
      revision = item1[2] - item2[2]
      return revision

    return item1[1] - item2[1]

  return item1[0] - item2[0]


def augment(item):
  length = len(item)
  if length > 2:
    return item
  item.append(-1)
  if(length > 1):
    return item
  item.append(-1)
  return item

'''
l1 = ["1.0.12", "0.42.3", "0.31.4", "2.0.77", "2.0.8"]
l2 = ["0"]
l3 = ["1.0.0", "1.0", "1", "0"]
l4 = [f"{str(x)}.4" for x in np.arange(100,0,-1)]
#print(l4)

lp1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
lp2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

print(solution(lp1))
'''

# LEVEL 2, Task 2 (en-route-salute)


def solution(s):
  moving_right = 0
  total_salutes = 0

  for c in s:
    if c == '>':
      moving_right += 1
    if c == '<':
      total_salutes += moving_right*2
  
  return total_salutes

'''
s1 = ">----<"
s2 = "<<>><"

print(solution(s2))
'''

# LEVEL 3, Task 1 (bomb-baby)


def solution(x, y):
  m = int(x)
  f = int(y)
  cycles = 0
  fail = 'impossible'

  while m > 0 and f > 0:
    if m == 1:
      cycles += (f-1)
      return str(cycles)
    if f == 1:
      cycles += (m-1)
      return str(cycles)

    q, r = 0, 0
    if m > f:
      q, r = div(m, f)
      m = r
    else:
      q, r = div(f, m)
      f = r

    cycles += q

  return fail


def div(divident, divisor):
  quotient = int(divident / divisor)
  remainder = divident - (quotient * divisor)
  return quotient, remainder

'''
s1 = '2', '1'
s2 = '4', '7'
s3 = '2', '4'
s4 = '1000', '1000'
s5 = '-10', '-9'
s_exp = '120000000', '2'

print(solution(*s_exp))
'''

# LEVEL 3, Task 2 (fuel-injection-perfection)


def solution(n):
  n = int(n)
  operations = 0

  while n > 1:
    if n % 2 == 0:
      n = int(n / 2)
    else:
      left = n - 1
      right = n + 1 

      bits_l = bin(left)
      bits_r = bin(right)

      len_l = len(bits_l) - 2
      len_r = len(bits_r) - 2

      # tip: dont count number of 0, just check if the second rightmost digit is 0 or 1
      ones_l = bits_l.count('1')
      zeros_l = len_l - ones_l
      ones_r = bits_r.count('1')
      zeros_r = len_r - ones_r

      if ones_l == ones_r == 1 or zeros_l > zeros_r:
        n = left
      else:
        n = right
  
    operations += 1

  return str(operations)


'''
n1 = "4" # -> 2
n2 = "15" # -> 5
n_309 = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
n_exp = "12"

print('solution:', solution(n_309))
'''

# LEVEL 3, Task 3 (find-the-access-codes)

# Dynamic

import numpy as np
from time import process_time


# length of l is between 2 and 2000
# list elements are between 1 and 999999
def solution(l):
  triple_count = 0
  divisor_number_list = len(l)*[0]
  
  if len(l) < 3:
    return triple_count

  for i in range(0, len(l)):
    for j in range(0, i):
      if l[i] % l[j] == 0:
        divisor_number_list[i] += 1
        triple_count += divisor_number_list[j]

  return triple_count


'''
l1 = [1,1,1] # -> 1
l2 = [1,2,3,4,5,6] # -> 3
l3 = [6,5,4,3,2,1] # -> 0
l4 = [1,3,2,5,4,6] # -> 3
l5 = np.arange(1,2001)
l6 = np.arange(2000,0, -1)
l7 = [1]*2000
l8 = [2**i for i in range(0,20)]
l9 = l8*10
l_exp = [2,2,2,4,4,4,8,8,8,2,2,4,4,8,8]

t1 = process_time()
s = solution(l5)
t2 = process_time()
print('solution', s, 'time:', t2-t1)
'''

# LEVEL 4, Task 1 (escape-pods)


from time import process_time


# flow network
# Ford-Fulkerson Algorithm
def solution(entrances, exits, path):
  total = 0
  max_cap = 2000000
  size = len(path)

  # augment path with single source and single sink with maximum capacity connections to each source/sink
  size_aug = size + 2
  for i, row in enumerate(path):
    row.append(0)
    row.append(max_cap if i in exits else 0)

  source_row = [max_cap if r in entrances else 0 for r in range(0, size_aug)]
  sink_row = (size_aug) * [0]
  path.append(source_row)
  path.append(sink_row)

  source_idx = size_aug - 2
  sink_idx = size_aug - 1

  feasible_path = []
  while feasible_path != None:
    feasible_path, bunny_number = find_feasible_path(path, source_idx, sink_idx, max_cap)
    if feasible_path != None:
      total += bunny_number
      for i in range(0, len(feasible_path) - 1):
        path[feasible_path[i]][feasible_path[i+1]] -= bunny_number
        path[feasible_path[i+1]][feasible_path[i]] += bunny_number

  return total


def find_feasible_path(adj_matrix, start, end, max_cap):
  """Find feasible path through graph and maximum number of bunnies that can fit through.

  Args:
    adj_matrix (list): adjacency matrix of rooms and corridor capacities
    start (int): source index
    end (int): sink index
    max_cap (int): maximum possible number of bunnies

  Returns:
    list: room indices forming a path from source to sink
    int: the maximum number of bunnies that can fit along the path
  """
  path_with_capacities = dfs(adj_matrix, start, end, max_cap)

  bunny_number = None
  feasible_path = None
  if path_with_capacities != None:
    bunny_number = min([el[1] for el in path_with_capacities])
    feasible_path = [el[0] for el in path_with_capacities]

  return feasible_path, bunny_number


def dfs(graph, start_idx, end_idx, max_cap):
  """Depth First Search from source to sink.

  Args:
    graph (list): adjacency matrix of rooms and corridor capacities
    start_idx (int): source index
    end_idx (int): sink index
    max_cap (int): maximum possible number of bunnies

  Returns:
    list: list of room indices and incoming corridor capacities forming path from source to sink
  """
  stack = [(start_idx, [(start_idx, max_cap)])]
  visited = set()
  while stack:
    (curr_idx, curr_path) = stack.pop()
    if curr_idx not in visited:
      if curr_idx == end_idx:
        return curr_path
      visited.add(curr_idx)
      for next_idx, capacity in enumerate(graph[curr_idx]):
        if capacity != 0:
          stack.append((next_idx, curr_path + [(next_idx, capacity)]))


'''
n1 = ([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) # -> 6
n2 = ([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) # -> 16

t1 = process_time()
s = solution(*n1)
t2 = process_time()
print('solution', s, 'time:', t2-t1, 'seconds')
'''

# LEVEL 4, Task 2 (running-with-bunnies)


from time import process_time
from itertools import combinations, permutations


# Reduction to a version of TSP that preserves the triangle inequality
def solution(times, time_limit):  
  n = len(times)
  times_sp = arcs_to_shortest_distances(times, n)

  # early return for negative weight cycle case (all worker ids)
  if times_sp == None:
    return list(range(0, n-2))

  most_locations = []
  all_bunny_locations = list(range(1, n-1))

  # iterate through bunny location number ranging from zero bunnies to all bunnies
  for i in range(1, n-1):
    feasible_locations = find_feasible_locations(times_sp, time_limit, i, all_bunny_locations, n)

    # early stopping (there is no feasible solution of greater size beause of triangle inequality)
    if feasible_locations is None:
      break

    most_locations = feasible_locations

  # bunny ids start from 0, bunny locations start from 1
  worker_ids = [l-1 for l in most_locations]
  worker_ids.sort()
  return worker_ids


def find_feasible_locations(adj_matrix, limit, location_number, all_bunny_locations, n):
  """Find list of bunny locations of given size that are feasible to visit within time limit.

  Args:
    adj_matrix (list): adjacency matrix of locations and travel times between them
    limit (int): time limit
    location_number (int): number of bunny locations attempted to visit during search
    all_bunny_locations (list): list of all bunny locations (omit start and finish)
    n (int): total number of locations

  Returns:
    list: list of bunny locations of given size that is possible to visit within time limit
          or None in case the given number of locations is not feasible within time limit
  """
  loc_combinations = list(combinations(all_bunny_locations, location_number))

  for _, loc_list in enumerate(loc_combinations):
    loc_list_permutations = list(permutations(loc_list))

    for _, locs in enumerate(loc_list_permutations):
      path = [0] + list(locs) + [n-1]
      total_dist = 0
      for i in range(len(path)-1):
        total_dist += adj_matrix[path[i]][path[i+1]]
      
      if total_dist <= limit:
        return locs
    
  return None


def arcs_to_shortest_distances(adj_matrix, n):
  """Replace graph arcs with shortest distances (preserving the trinagle inequality, no need to revisit locations).

  Args:
    adj_matrix (list): adjacency matrix of locations and travel times between them
    n (int): total number of locations

  Returns:
    list: adjacency matrix of locations and travel times between them preserving the triangle inequality
          or None in case of negative length cycle
  """
  adj_matrix_shortest = []
  for i, _ in enumerate(adj_matrix):
    distances = shortest_distances(adj_matrix, i, n)

    # negative length cycle case
    if distances == None:
      return None

    adj_matrix_shortest.append(distances)
  
  return adj_matrix_shortest


def shortest_distances(adj_matrix, start, n):
  """Bellman-Ford lite version (no path calculation).

  Args:
    adj_matrix (list): adjacency matrix of locations and travel times between them
    start (int): starting location for the search
    n (int): total number of locations

  Returns:
    list: shortest path distances from start to all locations or None in case of negative length cycle
  """
  dist = n*[float('inf')]
  dist[start] = 0

  for _ in range(n-1):
    for i, row in enumerate(adj_matrix):
      for j, col in enumerate(row):
        if dist[i] + col < dist[j]:
          dist[j] = dist[i] + col

  # detect negative length cycle
  for i, row in enumerate(adj_matrix):
    for j, col in enumerate(row):
      if dist[i] + col < dist[j]:
        return None

  return dist


'''
n1 = ([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) # -> [0, 1]
n2 = ([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) # -> [1, 2]
n3 = ([], 1) # -> []
n4 = ([[0, 2, 1], [9, 0, 1], [9, -3, 0]], 0) # -> [0]
n5 = ([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 0) # -> [0, 1, 2, 3, 4]

t1 = process_time()
s = solution(*n2)
t2 = process_time()
print('solution', s, 'time:', t2-t1, 'seconds')
'''

# LEVEL 5, Task 1 (dodge-the-lasers)



from time import process_time
from math import sqrt, floor



# LINEAR TIME
def solution(s):
  time_steps = int(s)
  acceleration = sqrt(2)

  total_distance = 0
  for i in range(1, time_steps+1):
    curr_distance = int(i*acceleration)
    total_distance += curr_distance

  return str(total_distance)


'''
s1 = '77' # -> 4208
s2 = '5' # -> 19

t1 = process_time()
s = solution(s1)
t2 = process_time()
print('solution', s, 'time:', t2-t1, 'seconds')
'''

# LEVEL 5, Task 1 (dodge-the-lasers)



from time import process_time
from decimal import Decimal, localcontext



# BEATTY SEQUENCE
def solution(s):
  with localcontext() as context:
    context.prec = 201

    time_steps = Decimal(s)
    acceleration = Decimal(2).sqrt()
    acceleration_fraction = acceleration % 1

    def calculate_sum(n, acc_frac):
      """sum of a Beatty sequence generated by an irrational number r, where 1 < r < 2

      Args:
        n (Decimal): number until which the sum should be calculated (including n)
        acc_frac (Decimal): fractional part of the irrational number r

      Returns:
        Decimal: sum of the sequence
      """
      if n == 0:
        return 0

      overflow = floored_product(n, acc_frac)
      g_sum = gauss_summation(n + overflow)
      return g_sum - calculate_complement_sum(overflow, acc_frac)

    def calculate_complement_sum(n, acc_frac):
      """sum of a Beatty sequence generated by an irrational number s, where s >= 2

      Args:
        n (Decimal): number until which the sum should be calculated (including n)
        acc_frac (Decimal): fractional part of the irrational number r, where r = s/(s-1)

      Returns:
        Decimal: sum of the sequence
      """
      g_sum = gauss_summation(n)
      return 2*g_sum + calculate_sum(n, acc_frac)

    def gauss_summation(n):
      """sum of integers [1, n].

      Args:
        n (Decimal): number until which the sum should be calculated (including n)

      Returns:
        Decimal: sum of integers from 1 to n (inclusive)
      """
      return n*(n + 1)/Decimal(2)

    def floored_product(n, irrational):
      """product of an integer and an irrational number rounded down to the nearest integer.

      Args:
        n (Decimal): integer part of the product
        irrational (Decimal): irrational part of the product

      Returns:
        Decimal: product of inputs rounded down
      """
      return int(irrational*n)

    calculated_distance = calculate_sum(time_steps, acceleration_fraction)
    return str(int(calculated_distance))


'''
s1 = '77' # -> 4208
s2 = '5' # -> 19
s_exp = '10000'

t1 = process_time()
s = solution(s1)
t2 = process_time()
print('solution', s, 'time:', t2-t1, 'seconds')
'''

import base64

ENCRYPTED_MESSAGE = "C0IHEBFNFxkSRUNJRUkMHRUEAEJeDlUJDg4PFgQJHgpXRU5FVUsBHgQHDhYBSUdPVwASAx1cBhlG QllTQgcFDAIAEAwQQhdNTUJEEgYGAgoGABkAHFpVSltCRAYLAgQMGwAQQl4OVRgAAAEaER1MT0pF UxYTSBdNTUJEFQoBTE9KRVMSG0BTTRw="
KEY = 'peter.rjabcsenko'

result = []
for i, c in enumerate(base64.b64decode(ENCRYPTED_MESSAGE)):
  result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

# util
from functools import reduce
def print_network(network):
  print(reduce(lambda acc, p: f'{acc}\n{p[0]} -> {p[1]}', enumerate(network), ''))