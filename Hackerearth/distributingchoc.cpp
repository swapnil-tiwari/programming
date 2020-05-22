#include <iostream>

using namespace std;
// long long int min(int n,int key,int c)
// {
// 	long long int sum=((n*(n+1))/2)+ ((key-1)*n);
// 	// cout<<n<<","<<key<<","<<sum<<endl;
// 	if(sum<=c)
// 	{
// 		return min(n,key+1,c);
// 	}
// 		return (key-1);
	
	 

// }
int main() {
	int t;
	cin>>t;
	while(t--)
	{
		long long int c,n;
		cin>>c>>n;
		// cout<<c<<" "<<n;
		long long int fact=c/n+1;
		// cout<<fact;
		long long int sum=0,key;
		long long int sum2=(n*(n+1))/2;
		key=c-sum2;
		if(key<0)
		{
			cout<<c<<endl;
		}
		else
		{
			cout<<key%n<<endl;
		}
		// key=min(n,1,c);
		
	
	}

}










