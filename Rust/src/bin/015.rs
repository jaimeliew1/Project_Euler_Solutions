fn solve() -> u64 {
    (1..21)
        .into_iter()
        .fold(1.0, |acc, i| acc * (20.0 + i as f64) / (i as f64)) as u64
}

ProjectEuler::problem!(solve);
