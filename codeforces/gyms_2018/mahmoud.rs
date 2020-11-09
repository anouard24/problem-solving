// problem name: Mahmoud and Longest Uncommon Subsequence
// date:         21/01/2018

use std::io::{self,BufRead};
use std::cmp as c;
fn main() {
	let __=io::stdin();
	let mut s=String::new();
	__.lock().read_line(&mut s).ok();
	let mut S=String::new();
	__.lock().read_line(&mut S).ok();
	println!("{}",if s==S{1}else{
	c::max(s.len(),S.len())}as i64-2);
}

