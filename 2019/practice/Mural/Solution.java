import java.util.Scanner;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int t = scan.nextInt();
    for (int i = 1; i <= t; i++) {
      int n = scan.nextInt();
      int[] scores = toIntArray(scan.next());
      int b = maxBeautyScore(scores);
      System.out.format("Case #%d: %d%n", i, b);
    }
  }

  static int maxBeautyScore(int[] scores) {
    int n = scores.length;
    int m = n/2 + (n % 2 == 1? 1 : 0);  // max length of mural
    int maxScore = 0;
    int curScore = 0;
    for (int i = 0; i < m; i++) {
      curScore += scores[i];
    }
    maxScore = curScore;
    for (int i = m; i < n; i++) {
      curScore = curScore - scores[i-m] + scores[i];
      maxScore = Math.max(maxScore, curScore);
    }
    return maxScore;
  }

  static int[] toIntArray(String s) {
    int[] array = new int[s.length()];
    for (int i = 0; i < s.length(); i++) {
      array[i] = s.charAt(i) - '0';
    }
    return array;
  }
}