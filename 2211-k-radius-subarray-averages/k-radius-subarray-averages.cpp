class Solution {
public:
    vector<int> getAverages(vector<int>& arr, int k) {
       
         int n = arr.size();
    vector<int> v(n, -1);
    int windowSize = 2 * k + 1;

    if (windowSize > n) return v;

    long long sum = 0;  // ✅ fix overflow

    for (int i = 0; i < windowSize; i++) {
        sum += arr[i];
    }

    for (int i = k; i <= n - k - 1; i++) {
        v[i] = static_cast<int>(sum / windowSize);
        if (i + k + 1 < n) {
            sum -= arr[i - k];
            sum += arr[i + k + 1];
        }
    }

    return v;
    }
};