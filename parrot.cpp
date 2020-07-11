#include <iostream>

// This code is By Dominic

using namespace std;

int main() {
	float GeneralFare = 60;
	float Percentage = 100;
	float Student = 20;
	float Couples = 15;
	float AboveAge = 35;
	float LIMIT = 3;
	float user;
	float age;
	float TotalFare;
	
	
	cout<<"Student or Couples or OlderPerson [1-3] respectively: ";
	cin>>user;
	
	while(user > LIMIT) {
		cout<<"Out of range..";
		break;
	} 
	
	if(user == 1) {
		cout<<"age: ";
		cin>>age;
		if(age < 20) {
			TotalFare = (Student/Percentage)*GeneralFare;
			cout<<"Your total discount is: " <<endl;
			cout<<TotalFare;
		
		}
	}
	
	else if(user == 2) {
		cout<<"age: ";
		cin>>age;
		if(age > 60) {
			TotalFare = (AboveAge/Percentage)*GeneralFare;
			cout<<"Your total discount is: " <<endl;
			cout<<TotalFare;
		}
	}
	
	else {
		TotalFare = (Couples/Percentage)*GeneralFare;
		cout<<"Your total discount is: " <<endl;
		cout<<TotalFare;
	}
	
	return 0;
}
