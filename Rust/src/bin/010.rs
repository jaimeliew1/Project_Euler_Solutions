use ProjectEuler::prime_list;
fn solve() -> u64{
    prime_list(2000000).iter().sum()
}

ProjectEuler::problem!(solve);
