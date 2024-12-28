
def merge_sort(ls):
    if len(ls)>1:
        ls1=ls[:len(ls)//2]
        ls2=ls[len(ls)//2:]

        merge_sort(ls1)
        merge_sort(ls2)

        i=0
        j=0
        k=0
        while i<len(ls1) and j<len(ls2):
            if ls1[i]<ls2[j]:
                ls[k]=ls1[i]
                i+=1
                k+=1
            else:
                ls[k]=ls2[j]
                j+=1
                k+=1
        while i<len(ls1):
            ls[k] = ls1[i]
            i+=1
            k+=1
        while j<len(ls2):
            ls[k] = ls2[j]
            j+=1
            k+=1


lst=[7,2,10,5,3,9,4,8,6,1]
merge_sort(lst)
print("sorted list:",lst)