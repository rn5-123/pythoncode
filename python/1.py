import  time
start=time.time()
print("Lists")
List = [1,2,"ABC",3,"xyz",2,3]
print (List)
print("\n Dictionary")
Dict={"a":1,"b":2,"c":3}
print (Dict)
print("\n Tuples")
Tup=(1,2,3,4,5)
print (Tup)
print("\n Sets")
s=(1,1,2,2,3,3,4,4,5,5)
print (s)
end =time.time()
print(f"Runtime of Program in {end-start}")


