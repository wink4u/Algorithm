#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> sides) {
    // 가장 긴 변의 길이는 다른 두변의 길이의 합보다 작아야 함
    int answer = 0;
    sort(sides.begin(), sides.end());
        
    for (int i = sides[1] + 1; i < sides[0] + sides[1]; i++)
    {
        answer++;
    }
    
    for (int i = sides[1] - sides[0] + 1; i <= sides[1]; i++)
    {
        answer++;
    }
    
    return answer;
}