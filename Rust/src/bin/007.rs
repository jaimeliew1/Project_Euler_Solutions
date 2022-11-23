use ProjectEuler::prime_list;

fn solve() -> u64 {
    *prime_list(1000000)
        .get(10001 - 1)
        .expect("not enough primes!")
}

ProjectEuler::problem!(solve);
