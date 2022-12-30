

print("\n\t\t\t\tWELCOME TO LIBRARY")
i=1
while i==1:

    lib=['c','c++','java']
    print("books in library",lib)
    print("no. of books in library currently",len(lib))
    a=int(input("Enter the pos no:"))
    element=input("Enter the book name to insert:")
    lib.insert(a,element)
    print("After insertion updated a list ",lib)
    print("no of book in library currently",len(lib))
    o=int(input("enter a book position  to take:"))
    lib.pop(o)
    print("After deletion updated a list ",lib)
    print("no of book in library currently",len(lib))
    lib.sort()
    print("\n\n after sorting",lib)
    ex=int(input("would you like to exit:1.yes  2.no"))
    if ex==1:
        i=909
    else:
        i=1
