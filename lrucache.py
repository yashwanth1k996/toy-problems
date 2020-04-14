class LRU:
  def __init__(self, capacity):
      self.capacity = capacity
      self.elements = {}
      self.elementKey = []
      pass
  

  def put(self, key, value):
        if (len(self.elementKey) == self.capacity):
              # x = elementKey.get(0)
              x = self.elementKey.pop(0)
              del self.elements[x]
              self.elements[key] = value
              self.elementKey.append(key)
        else:
              self.elements[key] = value
              self.elementKey.append(key)   
  pass
        

  def get(self, key):
        if(key in self.elements):
              self.elementKey.remove(key)
              self.elementKey.append(key)
              val = self.elements[key]
              del self.elements[key]
              self.elements[key] = val
              return self.elements[key]
              
        else:
              return -1
      
  pass


def main():
      x1 = LRU(3)
      x1.put('a', 2)
      x1.put('b', 3)
      x1.put('c', 4)
      x1.put('d', 5)
      print(list(x1.elements.keys()))
      y = x1.get('b')
      print(y)
      print(list(x1.elements.keys()))
      k = x1.get('c')
      print(k)
      print(list(x1.elements.keys()))


pass

if __name__ == '__main__':
    main()
    
