# --- Node Structure for the Huffman Tree (Unchanged) ---
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # Character (None for internal nodes)
        self.freq = freq  # Frequency/Weight
        self.left = None  # Left child node
        self.right = None # Right child node

    # Define comparison based on frequency for the heap.
    # Nodes with lower frequency have higher priority (are 'smaller').
    def __lt__(self, other):
        if not isinstance(other, HuffmanNode):
            return NotImplemented
        return self.freq < other.freq

    def __eq__(self, other):
        if not isinstance(other, HuffmanNode):
            return NotImplemented
        return self.freq == other.freq

    # Optional: For printing the node (useful for debugging)
    def __repr__(self):
        return f"Node({self.char}, {self.freq})"

# --- Custom MinHeap Implementation ---
class MinHeap:
    def __init__(self):
        """Initializes an empty min-heap."""
        self.heap = [] # Use a list to store the heap elements

    def _parent_index(self, i):
        """Returns the index of the parent of node at index i."""
        return (i - 1) // 2

    def _left_child_index(self, i):
        """Returns the index of the left child of node at index i."""
        return 2 * i + 1

    def _right_child_index(self, i):
        """Returns the index of the right child of node at index i."""
        return 2 * i + 2

    def _swap(self, i, j):
        """Swaps the elements at indices i and j in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        """
        Maintains the min-heap property by moving the node at index i upwards
        until it's in the correct position.
        """
        parent = self._parent_index(i)
        # While the node is not the root and is smaller than its parent
        while i > 0 and self.heap[i] < self.heap[parent]:
            self._swap(i, parent)
            i = parent # Move up to the parent's index
            parent = self._parent_index(i)

    def _heapify_down(self, i):
        """
        Maintains the min-heap property by moving the node at index i downwards
        until it's in the correct position.
        """
        n = len(self.heap)
        smallest = i # Assume current node is the smallest
        left = self._left_child_index(i)
        right = self._right_child_index(i)

        # Check if left child exists and is smaller than the current smallest
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if right child exists and is smaller than the current smallest
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest node found is not the current node, swap and recurse
        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest) # Continue heapifying down from the new position

    def insert(self, node):
        """Inserts a HuffmanNode into the heap."""
        self.heap.append(node) # Add node to the end
        self._heapify_up(len(self.heap) - 1) # Heapify up from the last element

    def extract_min(self):
        """Removes and returns the HuffmanNode with the minimum frequency."""
        if not self.heap:
            return None # Heap is empty
        if len(self.heap) == 1:
            return self.heap.pop() # Only one element

        min_node = self.heap[0] # The root is the minimum element
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        # Restore the heap property starting from the root
        self._heapify_down(0)

        return min_node

    def __len__(self):
        """Returns the number of elements currently in the heap."""
        return len(self.heap)

    def is_empty(self):
        """Checks if the heap is empty."""
        return len(self.heap) == 0

