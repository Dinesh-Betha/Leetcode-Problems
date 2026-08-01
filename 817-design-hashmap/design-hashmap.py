class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key, value):
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                self.arr[i][1] = value
                break
        else:
            self.arr.append([key,value])

    def get(self, key):
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
               return self.arr[i][1]
        
        return -1
        

    def remove(self, key):
       remove_index = -1
       for i in range(len(self.arr)):
        if self.arr[i][0] == key:
             remove_index = i
       if remove_index != -1:

        self.arr.pop(remove_index)
    
          



