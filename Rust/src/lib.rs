pub fn prime_list(up_to: u64) -> Vec<u64> {
    let sieve_size = up_to + 1;
    let mut sieve: Vec<bool> = vec![false; sieve_size as usize];

    let mut p = 2;
    loop {
        if p * p >= sieve_size {
            break;
        }
        for f in p..=(up_to / p) {
            let index = p * f;
            sieve[index as usize] = true;
        }
        p += 1;
        while sieve[p as usize] {
            p += 1;
        }
    }
    sieve
        .into_iter()
        .enumerate()
        .skip(2)
        .filter_map(|(i, p)| if p { None } else { Some(i as u64) })
        .collect()
}

#[macro_export]
macro_rules! problem {
    ($solver:expr) => {
        fn main() {
            let now = std::time::Instant::now();
            let ans = $solver();
            let time = now.elapsed().as_micros();
            println!("{}", ans);
            println!("time elapsed: {}μs", time);
        }
    };
}
