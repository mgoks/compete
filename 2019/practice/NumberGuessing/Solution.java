import java.util.Scanner;

public class Solution {
  static void guessNumber(Scanner scan, int low, int high) {
    int mid = (low + high)/2;
    System.out.println(mid);
    String response = scan.next();
    if (response.equals("TOO_SMALL")) 
      guessNumber(scan, mid+1, high);
    else if (response.equals("TOO_BIG"))
      guessNumber(scan, low, mid-1);
    else 
      return;
  }
  
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int t = scan.nextInt();
    while (t-- > 0) {
      int a = scan.nextInt(); // exlusive
      int b = scan.nextInt(); // inclusive
      scan.next(); // max number of attempts redundant
      guessNumber(scan, a+1, b);
    }
  }
}