#include <iostream>
#include <algorithm>
#include <vector>

std::vector<int> two_sum(std::vector<int> &nums, int target) {
   std::vector<int> ret;
   std::vector<int> sorted_nums = nums;
   std::sort(sorted_nums.begin(), sorted_nums.end());
   for (auto i = sorted_nums.begin(), j = sorted_nums.end() - 1; i != j; ) {
      if (*i + *j == target) {
         auto i_it = std::find(nums.begin(), nums.end(), *i);
         auto j_it = std::find(nums.begin(), nums.end(), *j);
         if (*i == *j) {
            j_it = std::find(i_it + 1, nums.end(), *j);
         }
         ret.push_back(i_it - nums.begin());
         ret.push_back(j_it - nums.begin());
         return ret;
      } else if (*i + *j < target) {
         i++;
      } else {
         j--;
      }
   }
   return ret;
}

int main() {
   std::vector<int> nums;
   int size, target;
   scanf("%d", &size);
   for (int i = 0; i < size; i++) {
      int in;
      scanf("%d", &in);
      nums.push_back(in);
   }
   scanf("%d", &target);
   for (int i: two_sum(nums, target)) {
      std::cout << i << " ";
   }
   std::cout << "\n";
}
