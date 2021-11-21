#include <iostream>
#include <algorithm>

int length_of_longest_substring(std::string s) {
   int max_len = 0;
   int start = -1;
   std::vector<int> dict(256, -1);
   for (auto i = s.begin(); i != s.end(); i++) {
      if (dict[*i] > start) {
         start = dict[*i];
      }
      dict[*i] = i - s.begin();
      max_len = std::max(max_len, (int)(i - s.begin() - start));
   }
   return max_len;
}

int main() {
   std::string in;
   std::cin >> in;
   std::cout << length_of_longest_substring(in) << "\n";
}
