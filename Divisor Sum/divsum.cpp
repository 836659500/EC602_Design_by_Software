#include <iostream>
using namespace std;

int main(){
	int m; 
	while (true){
		cin >> m;
		if(m!=0){
			int sum=0;
			int largest=1;
			cout << m << ": ";
			for(int a=1; a<m;a++)
				if (m%a==0){
					largest=a;
				}
			for(int a=1; a<largest;a++)
				if (m%a==0){
					cout<<a<<"+";
					sum=sum+a;
				}
			sum=sum+largest;
			cout<<largest<<" = "<<sum<<endl;
		}
		else return 0;
	}
}
