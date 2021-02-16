#!/usr/bin/env python


def read_file(name):
    """
    Given the path/name of the file, return nthe jobs list with jobs[][0]: weight and jobs[][1]: length.
    """
    with open(name, 'r') as f:
        data = [list(map(int, line.split())) for line in f.readlines()[1:]]
    return data


### according to weight - length(difference) or weight/length(ratio)
def find_order(jobs, key='difference' or 'ratio'):
    """
    Find the order of jobs according to different key(priority).
    """
    
    # find the key of the priority
    if key == 'difference':
        priority = [(item[0] - item[1],item[0]) for item in jobs]
    else:
        priority = [(item[0]/item[1], item[0]) for item in jobs]
    
    order = sorted(range(len(priority)), key = priority.__getitem__)
    order.reverse()
    return order
 

def compute_sum(jobs, order):
    """Given the jobs list and order, find the weighted sum of the jobs.
    """
    finish_time = 0
    weighted_sum = 0
    for i in order:
        
        finish_time += jobs[i][1]
        weighted_sum += finish_time*jobs[i][0]
    return weighted_sum


if __name__ == '__main__':
    jobs = read_file('data.txt')
    ratio_order = find_order(jobs, 'ratio')
    difference_order = find_order(jobs, 'difference')
    
    ratio_sum = compute_sum(jobs, ratio_order)
    difference_sum = compute_sum(jobs, difference_order)
    print('result from ratio: ', ratio_sum)
    print('result from difference: ', difference_sum)
