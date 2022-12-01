
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse file"))
        .collect()
}

fn main() {
    let lines = lines_from_file("input.txt");
    let mut max_cals = vec![0,0,0];    
    let mut tmp: i32 = 0;
    for line in lines {
        if line == "" {
            let min_value = *max_cals.iter().min().unwrap();
            let index = max_cals.iter().position(|&r| r == min_value).unwrap();
            if max_cals[index] < tmp {
                max_cals[index] = tmp;
            }
            tmp = 0;
        }
        else {
            tmp += line.parse::<i32>().unwrap();
        }
    }
    let min_value = *max_cals.iter().min().unwrap();
    let index = max_cals.iter().position(|&r| r == min_value).unwrap();
    if max_cals[index] < tmp {
        max_cals[index] = tmp;
    }
    println!("{:?}", max_cals);
    println!("{:?}", max_cals.iter().sum::<i32>());
}

