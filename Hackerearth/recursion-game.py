# def winner(mem,song,pos,N):
#     par=0
#     slen=len(song)
#     print('pos')
#     if(len(mem)==1):
#         return mem[0]
#     while(pos<len(song)):
#         print('in')
        
#         if(song[pos]=='y'):
#             mem.pop(par)
        
#         par=par+1
#         pos=(pos+1)%slen
#         print('pos={},par={}'.format(pos,par))
#         if(par==N-1):
#             winner(mem,song,pos,len(mem))
    
#         # if(pos==len(song)-1):
#         #     pos=0
call=1
import sys
sys.setrecursionlimit(10**6)
def winner(mem,song,pos,par,N):
    # print('pos= {} N={}'.format(pos,N))
    global call
    slen=len(song)
    # print(call)
    call=call+1
    # smem=len(mem)
    # print('sizemem={},pos={},par={}'.format(smem,pos,par))
    if(N==1):
        return mem[0]
    if(song[pos]=='x'):
        return winner(mem,song,((pos+1)%slen),((par+1)%N),N)
    else:
        mem.pop(par)
        if(par==N-1):
            par=(par+1)%N
        return winner(mem,song,((pos+1)%slen),par,N-1)


def main():
    n=int(input())
    mem=[x for x in range(1,n+1)]
    song=input()
    song=[each for each in song]
    # print(mem,song)
    print(winner(mem,song,0,0,len(mem)))
    print(call)
    
main()