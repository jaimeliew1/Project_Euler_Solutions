use ProjectEuler::prime_list;

fn prime_factors(x: u64) -> Vec<u64> {
    let mut x = x;
    let mut primes: Vec<u64> = prime_list((x as f64).sqrt() as u64)
        .into_iter()
        .rev()
        .collect();
    let mut factors = Vec::new();

    let mut p = primes.pop().unwrap();
    while x != 1 {
        if x % p == 0 {
            factors.push(p);
            x /= p;
        } else {
            p = primes.pop().unwrap();
        }
    }
    factors
}

fn solve() -> u64 {
    prime_factors(600851475143).into_iter().max().unwrap()
}

ProjectEuler::problem!(solve);

#[test]
fn example() {
    assert_eq!(vec![5, 7, 13, 29], prime_factors(13195));
}
