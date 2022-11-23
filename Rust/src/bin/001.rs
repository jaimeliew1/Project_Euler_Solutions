fn solve() -> u64 {
    (1..1001)
        .into_iter()
        .filter(|x| x % 3 == 0 || x % 5 == 0)
        .sum()
}

ProjectEuler::problem!(solve);
