#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    int temp = 0;
    
    vector<int> test;
    my_string += 'A';
    for (int i = 0 ; i < my_string.length(); i++)
    {
        if (my_string[i] >= '0' && my_string[i] <= '9') { 
            test.push_back(my_string[i] - '0'); 
            
        }
        else{
            int cnt = test.size() - 1;
            if (cnt >= 0)
            {
                for(int j = 0; j < test.size(); j ++)
                {
                    answer += test[j] * pow(10, cnt);
                    cnt--;
                }
                test.clear();    
            }
                    
        }
    }
    return answer;
}