# pyqt-sort

![preview](/preview.gif?raw=true "Preview")

A simple GUI program built with PyQt5 that visualizes various sorting algorithms. Currently the program supports:

- Three different sample sizes: 128, 256, and 512

- 9 different sorting algorithms: <small>*n = length of the array / k = biggest value in the array*</small>

| Algorithm                      | Time (Average)       | Time (Worst)         | Time (Best)          | Space           |
| :-----------------------------:|:--------------------:|:--------------------:|:--------------------:|:---------------:|
| Bubble Sort                    | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( *n* )             | O( 1 )          |
| Selection Sort                 | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( 1 )          |
| Insertion Sort                 | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( *n* )             | O( 1 )          |
| Insertion Sort - Binary Search | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( *n log(n)* )      | O( 1 )          |
| Cycle Sort                     | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( *n<sup>2</sup>* ) | O( 1 )          |
| Cycle Sort - Optimized         | O( *n* )             | O( *n* )             | O( *n* )             | O( 1 )          |
| Quick Sort                     | O( *n log(n)* )      | O( *n<sup>2</sup>* ) | O( *n log(n)* )      | O( *n log(n)* ) |
| Merge Sort                     | O( *n log(n)* )      | O( *n log(n)* )      | O( *n log(n)* )      | O( *n* )        |
| Heap Sort                      | O( *n log(n)* )      | O( *n log(n)* )      | O( *n log(n)* )      | O( 1 )          |
| Counting Sort                  | O( *n + k* )         | O( *n + k* )         | O( *n + k* )         | O( *k* )        |

#### To do list
- ~~Add Counting Sort~~ (09/12/2020)
- Add Radix Sort (MSD * LSD)
- Support for multithreading so that two sorting can start simultaneously for real-time comparison 
