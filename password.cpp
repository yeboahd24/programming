// C++ implementation of the approach 
// Tested with password = "Geeks12345for69708"
#include <bits/stdc++.h> 
using namespace std; 
  
const int MAX = 10; 
  
// Function that returns true 
// if ch is a digit 
bool isDigit(char ch) 
{ 
    if (ch >= '0' && ch <= '9') 
        return true; 
    return false; 
} 
  
// Function that returns true 
// if str contains all the 
// digits from 0 to 9 
bool allDigits(string str, int len) 
{ 
  
    // To mark the present digits 
    bool present[MAX] = { false }; 
  
    // For every character of the string 
    for (int i = 0; i < len; i++) { 
  
        // If the current character is a digit 
        if (isDigit(str[i])) { 
  
            // Mark the current digit as present 
            int digit = str[i] - '0'; 
            present[digit] = true; 
        } 
    } 
  
    // For every digit from 0 to 9 
    for (int i = 0; i < MAX; i++) { 
  
        // If the current digit is 
        // not present in str 
        if (!present[i]) 
            return false; 
    } 
  
    return true; 
} 
  
// Driver code 
int main() 
{ 
    string str;
	cout<<"password: ";
	cin>>str; 
    int len = str.length(); 
  
    if (allDigits(str, len)) 
        cout << "Password is valid: "<<str; 
    else
        cout << "Password is not valid"; 
  
    return 0; 
} 

