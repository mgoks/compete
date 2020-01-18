import java.util.Scanner;

public class Solution {
  String guessNumber(Scanner scan, int lowerBound, int upperBound) {
    int mid = (lowerBound + upperBound)/2;  // both exclusive
    System.out.println(mid);
    String response = scan.nextLine();
    if (response.equals("TOO_SMALL"))
      return guessNumber(scan, mid, upperBound);
    else if (response.equals("TOO_BIG"))
      return guessNumber(scan, lowerBound, mid);
    else
      return response;
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    Solution guesser = new Solution();
    int t = Integer.parseInt(scan.nextLine()); // number of test cases
    while (t-- > 0) {
      int lowerBound = scan.nextInt(); // exclusive
      int upperBound = scan.nextInt(); // inclusive 
      scan.nextLine();
      int n = Integer.parseInt(scan.nextLine()); // max number of guesses
      if (!guesser.guessNumber(scan, lowerBound, upperBound+1).equals("CORRECT"))
        return; // something went wrong
    }
  }
}