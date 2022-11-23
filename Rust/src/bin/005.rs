fn solve() -> u64 {
    let mut x = 20;
    loop {
        if (2..21).into_iter().all(|d| x % d == 0) {
            return x;
        }
        x += 20;
    }
}
ProjectEuler::problem!(solve);
