import amino
clint =amino.Client()
e = input ('email:')
p = input ('password:')
clint.login(email=e,password=p)
c = input ('comid:')
subclint =amino.SubClient(comId=c,profile=clint.profile)
subclint.get_all_users( start= 0, size= 25)