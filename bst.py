class BST:
    def init(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            return
        if self.key == data:
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
          if self.key < data:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
    def pre_order(self):
        print(self.key,end="")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
    def in_order(self):
      if self.l_child:
        self.l_child.in_order()
      print(self.key,end="")
      if self.r_child:
        self.r_child.in_order()
    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key,end="")
root=BST(30)
root.insert_node(20)
root.insert_node(40)
root.insert_node(15)
root.insert_node(25)
root.insert_node(35)
root.insert_node(70)
