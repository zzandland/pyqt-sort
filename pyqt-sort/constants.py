from algorithms import insertion_sort, bubble_sort, selection_sort, quick_sort, merge_sort, heap_sort, cycle_sort

ALGORITHMS = {
    'bubble': ('Bubble Sort', bubble_sort.BubbleSort),
    'insertion': ('Insertion Sort', insertion_sort.InsertionSort),
    'selection': ('Selection Sort', selection_sort.SelectionSort),
    'quick': ('Quick Sort', quick_sort.QuickSort),
    'merge': ('Merge Sort', merge_sort.MergeSort),
    'heap': ('Heap Sort', heap_sort.HeapSort),
    'cycle': ('Cycle Sort', cycle_sort.CycleSort),
    'optimized_cycle': ('Cycle Sort (Optimized)', cycle_sort.OptimizedCycleSort)
}
