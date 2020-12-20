class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord
        
    def get_x(self):
        ''' (Point)->number
        Returns x coordinate of point to xcoord'''
        return self.x
    
    def get_y(self):
        ''' (Point)->number
        Returns y coordinate of point to ycoord'''
        return self.y
    
    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


##########################################################################################################################
##########################################################################################################################
class Rectangle(Point):
    def __init__(self, a, b, color):
        '''(Rectangle, Point, Point, str)->None'''
        
        #super().__init__(xcoord=0, ycoord=0)
        
        self.bottomleft = a
        self.topright = b
        self.color = color


    def get_bottom_left(self):
        '''(Rectangle)->Point'''
        return self.bottomleft

    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.topright

    def get_color(self):
        '''(Rectangle)->str'''
        return self.color

    def reset_color(self, new_color):
        '''(Rectangle, str)->None'''
        self.color = new_color

    def get_perimeter(self):
        '''(Rectangle)->int'''
        x1 = self.bottomleft.get_x()
        x2 = self.topright.get_x()

        y1 = self.bottomleft.get_y()
        y2 = self.topright.get_y()

        dx = x2 - x1
        dy = y2 - y1
        
        return (dx + dy) * 2
    

    def get_area(self):
        '''(Rectangle)->int'''
        x1 = self.bottomleft.get_x()
        x2 = self.topright.get_x()

        y1 = self.bottomleft.get_y()
        y2 = self.topright.get_y()

        dx = x2 - x1
        dy = y2 - y1

        return dx * dy

    def move(self, dx, dy):
        '''(Rectangle, int, int)->int'''
        self.bottomleft.move(dx, dy)
        self.topright.move(dx, dy)

    def intersects(self, rec2):
        '''(Rectangle, Rectangle)->bool'''
        x1 = self.bottomleft.get_x()
        y1 = self.bottomleft.get_y()

        x2 = self.topright.get_x()
        y2 = self.topright.get_y()


        xx1 = rec2.bottomleft.get_x()
        yy1 = rec2.bottomleft.get_y()

        xx2 = rec2.topright.get_x()
        yy2 = rec2.topright.get_y()

        c1 = xx1 > x2
        c2 = xx2 < x1
        c3 = yy1 > y2
        c4 = yy2 < y1
        
        return not(c1 or c2 or c3 or c4)



    def contains(self, x_point2, y_point2):
        '''(Rectangle, int, int)->bool'''
        x1 = self.bottomleft.get_x()
        y1 = self.bottomleft.get_y()

        x2 = self.topright.get_x()
        y2 = self.topright.get_y()


        if (x2 >= x_point2 >= x1 and y2 >= y_point2 >= y1):
            return True

        else:
            return False

    def __eq__(self, other):
        '''(Rectangle, Rectangle)->bool'''
        return self.bottomleft == other.bottomleft and self.topright == other.topright and self.color == other.color


    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle(' + str(self.bottomleft) + ', ' + str(self.topright) + ', ' + "'" + str(self.color)+ "'" + ')'


    def __str__(self):
        '''(Rectangle)->str'''
        return 'I am a ' + str(self.color) + ' rectangle with bottom left corner at (' + str(self.bottomleft.get_x()) + ', ' + str(self.bottomleft.get_y()) + ') and top right corner at (' + str(self.topright.get_x()) + ', ' + str(self.topright.get_y()) + ').'





class Canvas(Rectangle, list):

    def __init__(self):
        '''(Canvas)->None'''
        
        #super().__init__(a, b, color)
        
        self.list = []


    def add_one_rectangle(self, rec):
        '''(Canvas, Rectangle)->None'''
        self.list = self.list + [rec]

    def __len__(self):
        '''(Canvas)->int'''
        counter = 0
        for ch in self.list:
            counter += 1
        return counter

    def count_same_color(self, color):
        '''(Canvas, str)->int'''
        colors = []
        for ch in self.list:
            colors.append(ch.get_color())
        return colors.count(color)
    
    def total_perimeter(self):
        '''(Canvas)->int'''
        totalP = 0
        for ch in self.list:
            totalP += ch.get_perimeter()
        return totalP
    
    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        x = []
        y = []
        for ch in self.list:
            x.append(ch.get_bottom_left().get_x())
            x.append(ch.get_top_right().get_x())

            y.append(ch.get_bottom_left().get_y())
            y.append(ch.get_top_right().get_y())

        return Rectangle(Point(min(x), min(y)), Point(max(x), max(y)), 'red')
    
    def common_point(self):
        '''(Canvas)->bool'''
        for i in range(len(self.list) - 1):
            for j in range(len(self.list[i + 1: ])):
                if not self.list[i].intersects(self.list[j]):
                    return False
        return True


    def __repr__(self):
        '''(Canvas)->str'''
        return 'Canvas(' + str(self.list) +')'
        
    def __str__(self):
        '''(Canvas)->str'''
        return 'Canvas(' + str(self.list) +')'












