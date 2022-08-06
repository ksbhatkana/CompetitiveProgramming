void subString(string s, int n, string cur)
{
	if(n==s.size())
    {
      	cout<<cur<<endl;
      	return;
    }
  	subString(s,n+1,cur+s[n]);
  	subString(s,n+1,cur);
}

// Driver program to test above function
int main()
{
	string s = "abcd";
  string cur;
	subString(s,0, cur);
	return 0;
}
