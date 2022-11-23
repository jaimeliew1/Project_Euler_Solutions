use std::collections::HashMap;

fn solve() -> u64 {
    let mut chain_length: HashMap<u64, u64> = HashMap::new();

    for i in 1..1000000 {
        let mut x: u64 = i;

        let mut length = 0;
        while x != 1 {
            match chain_length.get(&x) {
                Some(l) => {
                    length += l - 1;
                    break;
                }
                None => {
                    x = match x {
                        n if n % 2 == 0 => x / 2,
                        n => 3 * n + 1,
                    };
                    length += 1;
                }
            }
        }
        chain_length.entry(i as u64).or_insert(length + 1);
    }
    *chain_length.iter().max_by_key(|(_, y)| *y).unwrap().0
}

ProjectEuler::problem!(solve);
