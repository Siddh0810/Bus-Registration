import random
class main:
    def start(self):
        l=input("you want to login or signup:-")
        if l=="login":
                self.user=input("enter your name:")
                self.pas=input("enter password:")
                f1=open("user.txt","r")
                for i in f1.readlines():
                    if i.split("-")[0]==self.user and i.split("-")[1]==self.pas:
                        self.page()
                else:
                    print("incorrect password")
                    self.start()
        elif l=="signup":
            self.user=input("enter your name:")
            self.pas=input("enter password:")
            w=self.user+"-"+self.pas
            f3=open("user.txt",'r')
            flag=0
            for i in f3.readlines():
                    if i.strip("\n")==w:
                        print("User already exits")
                        flag=1
                        break;
            if flag==1:
                self.start()
            else:
                
                f3.close()
                num=[0,1,2,3,4,5,6,7,8,9]
                unique=''
                for i in range(5):
                    unique+=str(random.choice(num))
                print(unique)   
                f2=open("user.txt","a")
                w=self.user+"-"+self.pas+"-"+unique
                f2.write("\n"+w)
                f2.close()
                self.page()        
        else:
            print("enter valid input")
    def page(self):
        print("1.Registration\n2.Bus timetable\n3.Ticket cancelation\n4.your booking\n5.exit")
        ch=int(input("enter your choice"))
        if ch==1:
            registration()
        if ch==2:
            registration()
        if ch==3:
            cnl=cancel()
            cnl.ticket_cancel()
        if ch==4:
            a=yourbook()
            a.show()
        else:
            print("Thanks for your visit")
            
            
class registration:
    def _init_(self):
        self.to=input("enter the pickup point:")
        self.des=input("enter destination:")
        self.location="location"+"-"+self.to+"-"+self.des
        self.display()
    def display(self):
        f=open("businfo.txt","r")
        s=[]
        j=0
        c=""
        for i in f.readlines():
            i1=i.split()
            if i1[0]==self.location:
                s.append(i)
                print(j+1," ",i1[0]," ",i1[1]," ",i1[2])
                j+=1
        y=input("enter yes if you want to book ticket else enter any key:")
        if y!="yes" and y!="YES":
            n=main()
            n.page()
        l=int(input("enter bus index number you want to display:"))
        j=1
        r=0
        for k in range(1,25):
            if r==2:
                print("  ",end="")
                r+=1
            elif str(j) in s[l-1].split()[4].split(",")[1:]:
                if k%6==0:
                    print("  0")
                    r=0
                else:
                    print("   0",end="")
                    r+=1
                j+=1
            elif k%6==0:
                if j in (0,1,2,3,4,5,6,7,8,9):
                    print("  ",j)
                else:
                    print(" ",j)
                j+=1
                r=0
            else:
                if j in (0,1,2,3,4,5,6,7,8,9):
                    print("  ",j,end="")
                else:
                    print(" ",j,end="") 
                j+=1
                r+=1
        self.name=input("enter your name:-")
        self.gender=input("enter gender:-")
        self.mo=input("enter your mobile number:-")
        self.age=input("enter your age:-")
        g=int(input("enter total number of sit you want to book"))
        f1=""
        sit=""
        c=s[l-1].split()[4].split(",")[1:]
        for i in range(0,g):
            t=input("enter sit number you want to book:-")
            if t in c:
                print("this sit is booked")
                self.display()
                break;
            sit=sit+","+t
        f.close()
        print("---your tick book sucessfully---")
        print("name:-",self.name,end="       ")
        print("      age:-",self.age)
        print("gender:-",self.gender,end="       ")
        print("     mobile no.:-",self.mo)
        print("busid:-",s[l-1].split()[3].split("-")[1],end="      ")
        print("     sit no.:-",sit[1:])
        print("bus pickup point:-",self.to,end="    ")
        print("    bus destination:-",self.des)
        o=open("businfo.txt","r")
        for i in o.readlines():
            if i.split()[3]==s[l-1].split()[3]:
                cost=int(i.split()[2].split("-")[1])
                print("cost=",(g*cost))
                print("-------------------------------")
                f1=f1+i.strip("\n")+sit+"\n"
            else:
                f1=f1+i
        o.close()
        #print("f1=",f1)
        v=open("businfo.txt","w")
        v.write(f1)
        v.close()
        q=open(self.name+".txt","a")
        si=sit[1:]
        cost=int(i.split()[2].split("-")[1])
        q.write("pickup point: "+self.to+"\n"+"destination: "+self.des+"\n"+"tic="+s[l-1].split()[3].split("-")[1]+"\n"+"total sit="+str(g)+"\n"+"no of sit="+si+"\n"+"cost="+str(g*cost))
        q.close()
        n=main()
        n.page()
class cancel:
    def ticket_cancel(self):
        user1=input("enter your name")
        y=open(user1+'.txt','r')
        u_id=int(input("enter your tic no: "))
        seat=int(input("enter seat no: "))
        bus=open("businfo.txt",'r')
        l=[]
        for i in bus.readlines():
                i1=i.split()
                l.append(i1)
        #print(l)
        bus.close()
        if int(l[u_id-1][3].split("-")[1])==u_id:
                seat_list=l[u_id-1][4].split(",")
                #print(seat_list)
        else:
            print("sorry ticket no is not matched.")
        seat_list.remove(str(seat))
        a=",".join(seat_list)
        #print(a)
        #print(seat_list)
        if int(l[u_id-1][3].split("-")[1])==u_id:
                l[u_id-1][4]=a
        #print(l)
        bus1=open("businfo.txt","w")
        for i in l:
            temp=''
            temp=" ".join(i)
            #print(temp)
            bus1.write(temp)
            bus1.write('\n')
        bus1.close()
        j=open(user1+'.txt','r')
        data=j.read()
        j.close()
        k=open(user1+".txt",'w')
        k.write(data+"\n")
        k.write("Cancel")
        k.close()
        x=main()
        x.page()
class yourbook:
    def show(self):
        name=input("enter your name: ")
        name=name+".txt"
        try:
            s=open(name,'r')
            data=s.read()
            print(data)
            x=main()
            x.page()
        except:
            print("file not found")
            x=main()
            x.page()


A=main()
A.start()