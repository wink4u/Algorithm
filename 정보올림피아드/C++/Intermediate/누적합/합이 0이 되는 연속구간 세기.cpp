#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
int main() {
    int N;
    if (!(cin >> N)) return 0;

    unordered_map<long long, long long> sum_count;
    sum_count[0] = 1;

    long long current_sum = 0;
    long long zero_sum_count = 0;

    for (int i = 0; i < N; i++) {
        long long num;
        cin >> num;

        current_sum += num;

        if (sum_count.find(current_sum) != sum_count.end()) {
            zero_sum_count += sum_count[current_sum];
        }

        sum_count[current_sum]++;
    }

    cout << zero_sum_count << "\n";

    return 0;
}