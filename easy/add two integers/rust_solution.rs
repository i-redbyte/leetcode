struct Solution;

impl Solution {
    pub fn sum(num1: i32, num2: i32) -> i32 {
        num1 + num2
    }
}

fn main() {
    println!("{}", Solution::sum(9990, 999));
}