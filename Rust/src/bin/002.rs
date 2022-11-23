fn fibonacci(up_to: u64) -> Vec<u64> {
    let (mut a, mut b) = (1, 2);
    let mut fib_list: Vec<u64> = vec![1, 2];
    (b, a) = (a + b, b);
    while b < up_to {
        fib_list.push(b);
        (b, a) = (a + b, b);
    }
    fib_list
}

fn solve() -> u64 {
    fibonacci(4000000).into_iter().filter(|x| x % 2 == 0).sum()
}
ProjectEuler::problem!(solve);
