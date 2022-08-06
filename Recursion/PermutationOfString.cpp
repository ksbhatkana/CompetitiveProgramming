#include<bits/stdc++.h>
using namespace std;

void permute(string s, int l, int r)
{
	if(l==r)
    {
        cout<<s<<endl;
      	return;
    }
    for(int i=l;i<=r;i++)
    {
        swap(s[l],s[i]);
        permute(s,l+1,r);
        swap(s[l],s[i]);
    }
}

// Driver program to test above function
int main()
{
	string s = "ab";
  	permute(s, 0, s.size()-1);
	return 0;
}
