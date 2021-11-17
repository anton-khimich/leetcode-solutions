#include <iostream>
#include <vector>

double calculate_median(std::vector<int> &sorted) {
   if (sorted.size() & 1) {      
      return sorted.at(sorted.size() / 2);
   } else {
      return (sorted.at(sorted.size() / 2 - 1) + sorted.at(sorted.size() / 2)) / 2.0;
   }
}

double find_median_sorted_arrays(std::vector<int> &nums1, std::vector<int> &nums2) {
   if (nums1.size() == 0) {
      return calculate_median(nums2);
   } else if (nums2.size() == 0) {
      return calculate_median(nums1);
   } else if (nums1.size() == 1 && nums1.size() == nums2.size()) {
      return (*nums1.begin() + *nums2.begin()) / 2.0;
   }

   std::vector<int> shorter, longer;
   if (nums1.size() <= nums2.size()) {
      shorter = nums1;
      longer = nums2;
   } else {
      shorter = nums2;
      longer = nums1;
   }

   int low = 0;
   int high = shorter.size() - 1;
   int mid;
   int shorter_left;
   int shorter_right;
   int longer_idx;
   int longer_left;
   int longer_right;
   while (low < high) {
      mid = (low + high) / 2;
      shorter_left = shorter.at(mid);
      shorter_right = shorter.at(mid + 1);
      longer_idx = (longer.size() + 1) / 2 - 1 + shorter.size() - 2 - 2 * mid;
      longer_left = longer.at(longer_idx);
      longer_right = longer.at(longer_idx + 1);
      if (shorter_left > longer_right) {
         // Move partition to the left
         high = mid - 1;
      } else if (longer_left > shorter_right) {
         // Move partition to the right
         low = mid + 1;
      } else {
         // Found the correct partition
         if ((shorter.size() + longer.size()) & 1) {
            std::cout << "INNER 1\n";
            return std::max(shorter_left, longer_left);
         } else {
            std::cout << "INNER 2\n";
            return (std::max(shorter_left, longer_left) + std::min(shorter_right, longer_right)) / 2.0;
         }
      }
   }
   // Didn't enter loop, what does that mean
   // if (high == low) {
   // }
   // If we're here, then the partition index is at one of the edges of shorter.
   if (high <= 0) {
   // Partition index is all the way at the left.
      std::cout << "FIRST OUTER ";
      if ((shorter.size() + longer.size()) & 1) {
         std::cout << "1\n";
         return longer.at((shorter.size() + longer.size()) / 2);
      } else if (shorter.size() == longer.size()) {
         std::cout << "2\n";
         return (*(longer.end() - 1) + *shorter.begin()) / 2.0;
      } else {
         std::cout << "3\n";
         return (longer.at((shorter.size() + longer.size()) / 2 - 1) + std::min(*shorter.begin(), longer.at((shorter.size() + longer.size()) / 2))) / 2.0;
      }
   } else if (low >= shorter.size() - 1) {
      std::cout << "SECOND OUTER ";
   // Partition index is all the way at the right.
      if ((shorter.size() + longer.size()) & 1) {
         std::cout << "1\n";
         return longer.at((longer.size() - shorter.size()) / 2);
      } else if (shorter.size() == longer.size()) {
         std::cout << "2\n";
         return (*longer.begin() + *(shorter.end() - 1)) / 2.0;
      } else {
         std::cout << "3\n";
         return (std::max(*(shorter.end() - 1), longer.at((longer.size() - shorter.size()) / 2 - 1) + longer.at((longer.size() - shorter.size()) / 2))) / 2.0;
      }
   }
   return 0;
}

int main() {
   int size, temp;
   std::vector<int> nums1;
   std::vector<int> nums2;
   scanf("%d", &size);
   for (int i = 0; i < size; i++) {
      scanf("%d", &temp);
      nums1.push_back(temp);
   }
   scanf("%d", &size);
   for (int i = 0; i < size; i++) {
      scanf("%d", &temp);
      nums2.push_back(temp);
   }
   std::cout << find_median_sorted_arrays(nums1, nums2) << "\n";
}
