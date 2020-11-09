// problem name: Keyboard
// date:         16/01/2018

import java.util.Scanner;
public class K {
	private static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		String keys =  "qwertyuiopasdfghjkl;zxcvbnm,./";
		String dir = sc.nextLine().trim();
		String msg = sc.nextLine().trim();
		int d = 0;
		if(dir.contains("R"))
			d = -1;
		if(dir.contains("L"))
			d = 1;
		char[] c = keys.toCharArray();
		char[] m = msg.toCharArray();
		int i = 0;
		for(i=0;i<m.length;i++) {
			int ind = indice(c,m[i]);
			if(d>0) {
				if(ind==c.length)
					ind = -1;
			}
			if(d<0) {
				if(ind==0)
					ind = c.length;
			}
			m[i] = c[ind+d];
		}
		String out = new String(m);
		System.out.print(out);
	}
	public static int indice(char[]arr,char a) {
		int i = 0;
		for(i=0;i<arr.length;i++) {
			if(a==arr[i]) return i;
		}
		return -1;
	}
}


/*

qwertyuiopasdfghjkl;zxcvbnm,./

*/

