#!/usr/bin/env python

import heapq


def get_data(name):
    with open(name, 'r') as f:
        return [int(d.strip()) for d in f.readlines()]
  

def insert(h_low, h_high, m):
    """
    Insert the item m to the heap.
    """
    # Push the m in the heap
    if m < h_low[0]:
        h_low.append(m)
        heapq._siftdown_max(h_low,0,len(h_low)-1)
    else:
        heapq.heappush(h_high, m)
    
    # Balance the two heaps
    size_diff = len(h_low) - len(h_high)
    
    if size_diff > 1:
        item = heapq._heappop_max(h_low)
        heapq.heappush(h_high,item)
    elif size_diff < -1:
        item = heapq.heappop(h_high)
        h_low.append(item)
        heapq._siftdown_max(h_low,0,len(h_low)-1)


def median_heap(data):
    """
    Output a list with all the medians in nsequennce.
    """
    median = []
    
    # initialize empty heaps
    h_low = []
    h_high = []
    heapq._heapify_max(h_low)
    heapq.heapify(h_high)
    
    # Push the first item into the h_low
    h_low.append(data[0])
    median.append(data[0])
    
    # Loop over all other items in data
    for d in data[1:]:
        insert(h_low, h_high, d)
        
        # Find the median
        if len(h_low) < len(h_high):
            median.append(h_high[0])
        else:
            median.append(h_low[0])
    return median


def main():
    d = get_data('data.txt')
    median = median_heap(d)
    result = sum(median) % 10000
    return result
    

if __name__ == '__main__':
    result = main()
    print(result)
