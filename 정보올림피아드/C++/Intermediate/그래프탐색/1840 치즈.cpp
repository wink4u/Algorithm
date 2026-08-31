#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<vector<int>> arr;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs() {
    int count = 0;
    queue<pair<int, int>> q;

    q.push({0, 0});

    vector<vector<bool>> visit(n, vector<bool>(m, false));
    visit[0][0] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;

        q.pop();

        for (int d = 0; d < 4; d++){
            int nx = x + dx[d], ny = y + dy[d];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (visit[nx][ny]) continue;

            if (arr[nx][ny] == 0) {
                visit[nx][ny] = true;
                q.push({nx, ny});
            } else if (arr[nx][ny] == 1) {
                visit[nx][ny] = true;
                arr[nx][ny] = 0;
                count++;
            }
        }
    }

    return count;
}


int main() {
    cin >> n >> m;
    arr.assign(n, vector<int>(m));

    int time = 0;
    int total = 0;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> arr[i][j];

            if (arr[i][j] == 1) total++;
        }
    }

    while (true) {
        int result = bfs();
        time++;

        if (result == total) break;

        total -= result;
    }

    cout << time << '\n';
    cout << total << endl;

    return 0;
}