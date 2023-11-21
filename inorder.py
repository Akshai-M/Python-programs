max_size=20
bt=[0]*max_size
    def inorder(index):
        if bt[index]!=0:
            inorder(index*2+1)
            print(bt[index],end=' ')
            inorder(index *2+2)
    
    def crate(i,r):
        bt[i]=r
        ch=int(input("\nLeft child available for %d:press y/n\t:"%r))
        if ch == 'y':
            value=int(input)
    