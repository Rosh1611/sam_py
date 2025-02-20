from multipledispatch import dispatch
@dispatch(str,float,float,float,float)
def pretty_print(s1,s2,s3,s4,s5):
    s='|'+'{}'.center(20)+'|'+'{:.2f}'.center(20)+'|'+'{:.2f}'.center(20)+'|'+'{:.2f}'.center(20)+'|'+'{:.2f}'.center(20)+'|'
    print(s.format(s1,s2,s3,s4,s5))
@dispatch(str,str,str,str,str)
def pretty_print(s1,s2,s3,s4,s5):
    s='|'+'{}'.center(20)+'|'+'{}'.center(20)+'|'+'{}'.center(20)+'|'+'{}'.center(20)+'|'+'{}'.center(20)+'|'
    print(s.format(s1,s2,s3,s4,s5))

pretty_print("Crop","Production Rate","Yield","Selling Price","Sales")
pretty_print("Tomato",11.4,182400.0,float(7),1276800.0)

