import random
class lift:
    def get_lift(self):
        '''
        This function initializes a random String array for lift and provides the
        lift that is fastest to reach.
        :return:
        '''
        a=[]
        choicee=["","U","D"]
        for i in range(5):
            a.append(str(random.randint(0,20))+str(random.choices(choicee)[0]))
        self.list_array=a
    def get_user_position(self,temp):
        '''
        :param temp: position of the person on the floor
        :return: returns the position of the person on the floor
        '''
        self.user_position=temp
    def output(self):
        a=["-1"]*20
        for i in self.list_array:
            if i[-1]!='U' and i[-1]!='D':
                a[int(i)]=i
            if i[-1] == 'U':
                a[int(i[:-1])] = i
            if i[-1] == 'D':
                a[int(i[:-1])] = i
        user_prefernce=self.user_position[-1]
        i,j=int(self.user_position[:-1]),int(self.user_position[:-1])
        while(True):
            if i==-1:
                i=int(self.user_position[:-1])-1
            if j==20:
                j = int(self.user_position[:-1])+1
            if a[i][-1] != "U" and a[i][-1]!="D" and int(a[i])!=-1:
                result=a[i]
                break
            if a[j][-1] != "U" and a[j][-1]!="D" and int(a[j])!=-1:
                result=a[j]
                break
            if user_prefernce=="U":
                if a[i][-1]=="U":
                    result = a[i]
                    break
            else:
                if a[j][-1]=="D":
                    result = a[j]
                    break
            i+=-1
            j-=-1
        final_result=""
        for index in range(len(self.list_array)):
            if result==self.list_array[index]:
                final_result=index
        print("Lift #"+str(final_result+1))
if __name__=="__main__":
    cl=lift()
    cl.get_lift()
    cl.get_user_position(input("Enter a request?"))
    cl.output()