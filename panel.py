def loginadmin(u,p,username_list,password_list):
    if u in username_list:
        index_pos=username_list.index(u)
        if p==password_list[index_pos]:
            return True
    return False
    
    
user_list=["admin","user1"]
password_list=["@dmin23","123"]
system=True
print('----------------------')
print('welcome to admin panel')
print('----------------------')
while system:
    x=3
    status=False
    while  x>1 and status==False:
        u=input("Give username:")
        p=input("Give password:")
        
        if loginadmin (u,p,user_list,password_list):
            print('----------------------')
            print("Your login is successful")
            print('----------------------')
            status=True
            current_user=u
        else:
            x=x-1
            if x>0:
                print('----------------------')
                print("wrong password you can have only",x,"more try")
                print('----------------------')
            else:
                print('----------------------')
                print ("your acount banned")
                print('----------------------')
    while status:
        if current_user=='admin':
            print('hi',current_user)
            print('----------------------')
            print('1. change username')
            print('2.log out')
            print('3.exit system')
            print('4.show users')
            print('5.add user')
            print('6.delete user')
            print('----------------------')

        else:
            print('1. change username')
            print('2.log out')
            print('3.exit system')
            print('----------------------')
        choice=input('choose (1-6):')
        print('----------------------')
        if choice=='1':
            current_index=user_list.index(current_user)
            newname=input('yeni adinizi giriniz:')
            user_list[current_index]=newname
            print('your saves have been changed')
            print('----------------------')
        elif choice=='2':
            print('you have been logged out')
            print('----------------------')
            status=False
        elif choice=='3':
            print('you have been logged out')
            print('----------------------')
            status=False
            system=False
        elif choice=='4'and current_user=='admin':
            print('users:',user_list)
        elif choice=='5'and current_user=='admin':
            new_user=input('new user name:')
            new_password=input('new password:')
            user_list.append(new_user)
            password_list.append(new_password)
            print('new user added')
            print('----------------------')
        elif choice=='6' and current_user=='admin':
            del_user=input('delete user name:')
            print('----------------------')
            if del_user in user_list:
                index_pos=user_list.index(del_user)
                user_list.pop(index_pos)
                password_list.pop(index_pos)
                print('user deleted')
                print('----------------------')

        else:
            print('your choice',choice,'is not valid') 
        