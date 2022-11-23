use itertools::Itertools;

pub fn is_palindrome(x: u64) -> bool {
    if x < 10 {
        return false;
    }
    let (mut reverse, mut original) = (0, x);

    while original > 0 {
        reverse = (reverse * 10) + original % 10;
        original /= 10;
    }
    reverse == x
}

fn solve() -> u64 {
    (100..1000)
        .tuple_combinations()
        .filter(|(a, b)| is_palindrome(a * b))
        .map(|(a, b)| a * b)
        .max()
        .unwrap()
}

ProjectEuler::problem!(solve);

#[test]
fn test_palindrome() {
    assert_eq!(false, is_palindrome(2));
    assert_eq!(true, is_palindrome(22));
    assert_eq!(true, is_palindrome(232));
    assert_eq!(true, is_palindrome(2332));
    assert_eq!(false, is_palindrome(2432));
    assert_eq!(false, is_palindrome(332));
}
