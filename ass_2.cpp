#include <iostream>
#include <iomanip>
using namespace std;

int main()

{
	// VARIABLE DEFINITIONS
	string grade1,grade2,grade3,grade4,grade5,grade6;
	int credithour1,credithour2,credithour3,credithour4,credithour5,credithour6;
	float point1,point2,point3,point4,point5,point6;
	float gradepoint1,gradepoint2,gradepoint3,gradepoint4,gradepoint5,gradepoint6;
	float gradePoint1,gradePoint2,gradePoint3,gradePoint4,gradePoint5,gradePoint6;
	
	//ACCEPTING USER'S INPUT
	cout<<"***WELCOME TO OUR G.P.A. CALCULATOR***\n"<<endl;
	cout<<"Enter the grade for course 1"<<endl;
	cin>>grade1;
	cout<<"Enter the credit hour for course 1"<<endl;
	cin>>credithour1;
	cout<<"\n";
	cout<<"Enter the grade for course 2"<<endl;
	cin>>grade2;
	cout<<"Enter the credit hour for course 2"<<endl;
	cin>>credithour2; 
	cout<<"\n";
	cout<<"Enter the grade for course 3"<<endl;
	cin>>grade3;
	cout<<"Enter the credit hour for course 3"<<endl;
	cin>>credithour3;
	cout<<"\n";
	cout<<"Enter the grade for course 4"<<endl;
	cin>>grade4;
	cout<<"Enter the credit hour for course 4"<<endl;
	cin>>credithour4;
	cout<<"\n";
	cout<<"Enter the grade for course 5"<<endl;
	cin>>grade5;
	cout<<"Enter the credit hour for course 5"<<endl;
	cin>>credithour5;
	cout<<"\n";
	cout<<"Enter the grade for course 6"<<endl;
	cin>>grade6;
	cout<<"Enter the credit hour for course 6"<<endl;
	cin>>credithour6;
	cout<<"\n";
	
	//CONVERTING GRADE1 TO POINT1
	if(grade1=="A")
	{
		point1=4.0;
	}
	else if(grade1=="B+")
	{
		point1=3.5;
	}
	else if(grade1=="B")
	{
		point1=3.0;
	}
	else if(grade1=="C+")
	{
		point1=2.5;
	}
	else if(grade1=="C")
	{
		point1=2.0;
	}
	else if(grade1=="D+")
	{
		point1=1.5;
	}
	else if(grade1=="D")
	{
		point1=1.0;
	}
	else if(grade1=="E")
	{
		point1=0.5;
	}
	else if(grade1=="F")
	{
		point1=0.0;
	}
	
	//CONVERTING GRADE2 TO POINT2
	if(grade2=="A")
	{
		point2=4.0;
	}
	else if(grade2=="B+")
	{
		point2=3.5;
	}
	else if(grade2=="B")
	{
		point2=3.0;
	}
	else if(grade2=="C+")
	{
		point2=2.5;
	}
	else if(grade2=="C")
	{
		point2=2.0;
	}
	else if(grade2=="D+")
	{
		point2=1.5;
	}
	else if(grade2=="D")
	{
		point2=1.0;
	}
	else if(grade2=="E")
	{
		point2=0.5;
	}
	else if(grade2=="F")
	{
		point2=0.0;
	}
	
	//CONVERTING GRADE3 TO POINT3
	if(grade3=="A")
	{
		point3=4.0;
	}
	else if(grade3=="B+")
	{
		point3=3.5;
	}
	else if(grade3=="B")
	{
		point3=3.0;
	}
	else if(grade3=="C+")
	{
		point3=2.5;
	}
	else if(grade3=="C")
	{
		point3=2.0;
	}
	else if(grade3=="D+")
	{
		point3=1.5;
	}
	else if(grade3=="D")
	{
		point3=1.0;
	}
	else if(grade3=="E")
	{
		point3=0.5;
	}
	else if(grade3=="F")
	{
		point3=0.0;
	}
	
	//CONVERTING GRADE4 TO POINT4
	if(grade4=="A")
	{
		point4=4.0;
	}
	else if(grade4=="B+")
	{
		point4=3.5;
	}
	else if(grade4=="B")
	{
		point4=3.0;
	}
	else if(grade4=="C+")
	{
		point4=2.5;
	}
	else if(grade4=="C")
	{
		point4=2.0;
	}
	else if(grade4=="D+")
	{
		point4=1.5;
	}
	else if(grade4=="D")
	{
		point4=1.0;
	}
	else if(grade4=="E")
	{
		point4=0.5;
	}
	else if(grade4=="F")
	{
		point4=0.0;
	}
	
	//CONVERTING GRADE5 TO POINT5
	if(grade5=="A")
	{
		point5=4.0;
	}
	else if(grade5=="B+")
	{
		point5=3.5;
	}
	else if(grade5=="B")
	{
		point5=3.0;
	}
	else if(grade5=="C+")
	{
		point5=2.5;
	}
	else if(grade5=="C")
	{
		point5=2.0;
	}
	else if(grade5=="D+")
	{
		point5=1.5;
	}
	else if(grade5=="D")
	{
		point5=1.0;
	}
	else if(grade5=="E")
	{
		point5=0.5;
	}
	else if(grade5=="F")
	{
		point5=0.0;
	}
	
	//CONVERTING GRADE6 TO POINT6
	if(grade6=="A")
	{
		point6=4.0;
	}
	else if(grade6=="B+")
	{
		point6=3.5;
	}
	else if(grade6=="B")
	{
		point6=3.0;
	}
	else if(grade6=="C+")
	{
		point6=2.5;
	}
	else if(grade6=="C")
	{
		point6=2.0;
	}
	else if(grade6=="D+")
	{
		point6=1.5;
	}
	else if(grade6=="D")
	{
		point6=1.0;
	}
	else if(grade6=="E")
	{
		point6=0.5;
	}
	else if(grade6=="F")
	{
		point6=0.0;
	}
	
	//CALCULATING INDIVIDUAL GRADE POINT
	gradePoint1 = point1 * credithour1;
	gradePoint2 = point2 * credithour2;
	gradePoint3 = point3 * credithour3;
	gradePoint4 = point4 * credithour4;
	gradePoint5 = point5 * credithour5;
	gradePoint6 = point6 * credithour6;
	
	float totalGP = gradePoint1+gradePoint2+gradePoint3+gradePoint4+gradePoint5+gradePoint6;
	
	
	int totalCreditHours = credithour1+credithour2+credithour3+credithour4+credithour5+credithour6;
	
	float GPA = totalGP/totalCreditHours;
	
	
	if(GPA >= 3.60 && GPA <=4.0)
	{
		cout<<"CONGRATULATIONS!!  You had First Class with a GPA of "<<setprecision(3)<< GPA<<endl;
	}
	else if(GPA >= 3.00 && GPA <=3.59)
	{
		cout<<"CONGRATULATIONS!!  You had Second Class Upper with a GPA of "<<setprecision(3)<<  GPA<<endl;
	}
    else if(GPA >= 2.00 && GPA <=2.99)
	{
		cout<<"CONGRATULATIONS!!  You had Second Class Lower with a GPA of "<<setprecision(3)<<  GPA<<endl;
	}
	else if(GPA >= 1.50 && GPA <=1.99)
	{
		cout<<"CONGRATULATIONS!!  You had Third Class with a GPA of "<<setprecision(3)<<  GPA<<endl;
	}
	else if(GPA >= 1.00 && GPA <=1.49)
	{
		cout<<"CONGRATULATIONS!!  You had Pass with a GPA of "<<setprecision(3)<<  GPA<<endl;
	}
	else 
	{
		cout<<"Sorry!!  You have Failed the Program  with a GPA of "<<setprecision(3)<<  GPA<<endl;
	}
	
	cout<<endl<<endl<<"**** Thank You for using Mascara's Application. Byeee ****\n";


	
return 0;	
	
}

