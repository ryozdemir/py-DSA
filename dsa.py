# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
#
#     for k in range(n):
#         print(k)
#
# # print_items(10)
#
#
# def add_items(n):
#     return n + n

#
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is ', cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
#
#
#
# class LinkList:
#     def __init__(self):
#       create new Node
#     def append(self, value):
#       create new Node
#       add Node the end
#     def pop(self):
#
#     def prepend(self, value):
#       create new Node
#       add Node to beginning
#     def insert(self, index, value):
#       create new Node
#       insert Node
#
#     def remove(self, index):
#
#
# n = 123123
# myArray = []
# for i in range(n):
#     myArray.append(i)
#
# print(myArray[123122])

head = {
            "value": 11,
            "next": {
                    "value": 3,
                    "next": {
                            "value": 23,
                            "next": {
                                    "value": 7,
                                    "next": {
                                            "value": 4,
                                            "next": None
                                    }
                            }
                    }
            }
}

print(head['next']['next']['value'])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)


my_linked_list.reverse()

my_linked_list.print_list()



        ### DOUBLY LINK LISTS ###

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp.value
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1
#         return True
#
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             temp.next = None
#         self.length -= 1
#         return temp.value
#
#     def get(self, index):
#          if index < 0 or index >= self.length:
#              return None
#          temp = self.head
#          if index < self.length/2:
#              for _ in range(index):
#                  temp = temp.next
#          else:
#              temp = self.tail
#              for _ in range(self.length - 1, index, -1):
#                  temp = temp.prev
#          return temp.value
#
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
#
#     def insert(self, index, value):
#         if index < 0 or index >= self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#
#         new_node = Node(value)
#         before = self.get(index - 1)
#         after = before.next
#
#         new_node.prev = before
#         new_node.next = after
#         before.next = new_node
#         after.prev = new_node
#
#         self.length += 1
#         return True
#
#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1:
#             return self.pop()
#
#         temp = self.get(index)
#
#         temp.next.prev = temp.prev
#         temp.prev.next = temp.next
#         temp.next = None
#         temp.prev = None
#
#         self.length -= 1
#         return temp
#
#
# my_doubly_linked_list = DoublyLinkedList(0)
# my_doubly_linked_list.append(1)
# my_doubly_linked_list.append(2)
#
# print(my_doubly_linked_list.remove(1), '\n')
#
# my_doubly_linked_list.print_list()

      ### DATA STRUCTURES: Stacks and Queues ###
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1
#
#     def print_stack(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def push(self, value):
#         new_node = Node(value)
#         if self.height == 0:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1
#
#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = self.top.next
#         temp.next = None
#         self.height -= 1
#         return temp.value
#
# my_stack = Stack(7)
# my_stack.push(23)
# my_stack.push(3)
# my_stack.push(11)
#
# print(my_stack.pop(), '\n')
#
# my_stack.print_stack()


        ### DATA STRUCTURES: TREES ###
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while (True):
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right
#
#     def contains(self, value):
#         temp = self.root
#         while (temp is not None):
#             if value < temp.value:
#                 temp = temp.left
#             elif value > temp.value:
#                 temp = temp.right
#             else:
#                 return True
#         return False
#
#
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
#
# print(my_tree.contains(27))
# print(my_tree.contains(17))

            ### DATA STRUCTURES: HASH TABLES ###
#
# class HashTable:
#     def __init__(self, size = 7):
#         self.data_map = [None] * size
#
#     def __hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash
#
#     def print_table(self):
#         for i, val in enumerate(self.data_map):
#             print(i, ": ", val)
#
#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] == None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])
#
#     def get_item(self, key):
#         index = self.__hash(key)
#         if self.data_map[index] is not None:
#             for i in range(len(self.data_map[index])):
#                 if self.data_map[index][i][0] == key:
#                     return self.data_map[index][i][1]
#         return None
#
#     def keys(self):
#         all_keys = []
#         for i in range(len(self.data_map)):
#             if self.data_map[i] is not None:
#                 for j in range(len(self.data_map[i])):
#                     all_keys.append(self.data_map[i][j][0])
#         return all_keys
#
# my_hash_table = HashTable()
#
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
#
#
# print(my_hash_table.keys())


# Example: O(n2)

# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False
#
# list1 = [1, 3, 5]
# list2 = [2, 4, 5]
#
# print(item_in_common(list1,  list2))

# Example O(n)
# def item_in_common(list1, list2):
#     my_dict = {}
#     for i in list1:
#         my_dict[i] = True
#
#     for j in list2:
#         if j in my_dict:
#             return True
#
#     return False
#
# list1 = [1, 3, 5]
# list2 = [2, 4, 5]
#
# print(item_in_common(list1, list2))

        ### DATA STRUCTURES: GRAPHS ###
#
# class Graph:
#     def __init__(self):
#         self.adj_list = {}
#
#     def print_graph(self):
#         for vertex in self.adj_list:
#             print(vertex, ':', self.adj_list[vertex])
#
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
#
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False
#
#     def remove_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             try:
#                 self.adj_list[v1].remove[v2]
#                 self.adj_list[v2].remove[v1]
#             except ValueError:
#                 pass
#             return True
#         return False
#
#     def remove_vertex(self, vertex):
#         if vertex in self.adj_list.keys():
#             for other_vertex in self.adj_list[vertex]:
#                 self.adj_list[other_vertex].remove(vertex)
#             del self.adj_list[vertex]
#             return True
#         return False
#
# my_graph = Graph()
#
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
#
# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('B', 'D')
# my_graph.add_edge('C', 'D')
#
# my_graph.remove_vertex('D')
#
# my_graph.print_graph()

        ### ALGORITHMS: RECURSION ###
#
# def funcThree():
#     print('Three')
#
# def funcTwo():
#     funcThree()
#     print('Two')
#
# def funcOne():
#     funcTwo()
#     print('One')
#
# funcOne()
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(4))


        ### ALGORITHMS: Bubble Sort ###
#
# def bubble_sort(my_list):
#     for i in range(len(my_list) - 1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j+1]:
#                 temp = my_list[j]
#                 my_list[j] = my_list[j+1]
#                 my_list[j+1] = temp
#     return my_list
#
# print(bubble_sort([4, 2, 6, 5, 1, 3]))
#
#         ### Selection Sort ###
#
# def selection_sort(my_list):
#     for i in range(len(my_list)-1):
#         min_index = i
#         for j in range(i+1, len(my_list)):
#             if my_list[j] < my_list[min_index]:
#                 min_index = j
#         if i != min_index:
#                 temp = my_list[i]
#                 my_list[i] = my_list[min_index]
#                 my_list[min_index] = temp
#     return my_list
#
# print(selection_sort([4, 2, 6, 5, 1, 3]))
#
#         ### Insertion Sort ###
#
# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i-1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list
#
# print(insertion_sort([4, 2, 6, 5, 1, 3]))

        ### Merge Sort ###
#
# def merge(array1, array2):
#     combined = []
#     i = 0
#     j = 0
#     while i < len(array1) and j < len(array2):
#         if array1[i] < array2[j]:
#             combined.append(array1[i])
#             i += 1
#         else:
#             combined.append(array2[j])
#             j += 1
#
#     while i < len(array1):
#         combined.append(array1[i])
#         i += 1
#
#     while j < len(array2):
#         combined.append(array2[j])
#         j += 1
#
#     return combined
#
# # print(merge([1, 2, 7, 8], [3, 4, 5, 6]))
#
# def merge_sort(my_list):
#     if len(my_list) == 1:
#         return my_list
#     mid = int(len(my_list)/2)
#     left = my_list[:mid]
#     right = my_list[mid:]
#     return merge(merge_sort(left), merge_sort(right))
#
# print(merge_sort([3, 1, 4, 2]))

        ### Quick Sort ###

    ### Pivot ###    ### Quick Sort ###
#
#
# def swap(my_list, index1, index2):
#     temp = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = temp
#
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#
#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index
#
# def quick_sort_helper(my_list, left, right):
#     if left < right:
#         pivot_index = pivot(my_list, left, right)
#         quick_sort_helper(my_list, left, pivot_index-1)
#         quick_sort_helper(my_list, pivot_index+1, right)
#     return my_list
#
# def quick_sort(my_list):
#     return quick_sort_helper(my_list, 0, len(my_list) - 1)
#
# print(quick_sort([4, 6, 1, 7, 3, 2, 5]))


            ### Algorithms: Tree Traversal ###

    ### Breadth First Search ###
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False




    def BFS(self):
        current_node = self.root
        results = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
#
# print(my_tree.BFS())

        ### Depth First Search  PreOrder ###

    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
#
# print(my_tree.dfs_pre_order())

        ### Depth First Search PostOrder

    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
#
# print(my_tree.dfs_post_order())


            ### Depth First Search InOrder ###


    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_in_order())

