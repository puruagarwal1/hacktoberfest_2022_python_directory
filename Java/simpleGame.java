package simplegame;
import java.util.Scanner;

/
public class SimpleGame {

	/**
	 * @param seconds to convert
	 * @return string for the converted seconds in the format: 23:59:59
	 */
	public String convertTime(int seconds){
		// TODO: Your code goes here
		if(seconds>=0){
		String a =  Integer.toString(seconds/3600)+":"+Integer.toString((seconds/60)%60)+":"+Integer.toString(seconds%60);
		System.out.println(a);
		return a;
		}if(seconds<0){
			String b = "-1:-1:-1";
			System.out.println(b);
			return b;
		}

		return null;
	}

	/**
	 * @param integer to add digits
	 * @return integer in which all the digits in the given non-negative integer are added.
	 * 
	 */
	public int digitsSum(int input){
		// TODO: Your code goes here
		int sum =0;
		for (int i=0;input>0;i++){
			sum +=input%10;
			input=input/10;
		}System.out.println(sum);
		return sum;
	}
	
	public static void main(String[] args) {
		
		SimpleGame game = new SimpleGame();
		Scanner sc = new Scanner(System.in);

		System.out.println("Game type convertTime[1] and digitsSum[2]: ");
		int u = sc.nextInt();
		if (u==1){
			System.out.println("Enter time in seconds: ");
			int u2 = sc.nextInt();
			String time = game.convertTime(u2);
		}if (u==2){
			System.out.println("Enter number : ");
			int u3 =sc.nextInt();
			int sum = game.digitsSum(u3);
		}

		sc.close();
	}	
}
