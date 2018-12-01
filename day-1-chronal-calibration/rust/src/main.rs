use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::process::exit;

fn main() {
    let file = File::open("../data.txt").unwrap();
    let reader = BufReader::new(&file);
    let mut frequencies: Vec<i32> = vec![];
    for line in reader.lines() {
        let l = line.unwrap();
        frequencies.push(l.parse::<i32>().unwrap());
    }
    println!("{:?}", frequencies.iter().sum::<i32>());

    let mut current_frequency = 0;
    let mut seen_frequencies: Vec<i32> = vec![current_frequency];
    let mut count = 0;
    loop {
        for frequency in frequencies.iter() {
            current_frequency += frequency;
            if seen_frequencies.contains(&current_frequency) {
                println!("{}", current_frequency);
                exit(0);
            }
            seen_frequencies.push(current_frequency);
        }
        count += 1;
        println!("pass {} {}", count, current_frequency);
    }
}
