fn solve() -> u64 {
    let sum_of_squares: u64 = (1..100+1).map(|x: u64| x.pow(2)).sum();
    let square_of_sum: u64 = (1..100+1).sum::<u64>().pow(2);
    square_of_sum - sum_of_squares
}

ProjectEuler::problem!(solve);
