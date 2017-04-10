#include<iostream>
#include<map>
#include<string>
using namespace std;
#define MAXN 11000
char str[MAXN];
map<string,int> mp;

int main()
{
	freopen("title.txt","r",stdin);
	freopen("title2.txt","w",stdout);
	int cnt=0;
	while(~scanf("%s",str))
	{
		printf("%s#%d\n",str,++cnt);
		mp[str]=cnt;
	}
}
