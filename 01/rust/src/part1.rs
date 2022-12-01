
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
    let mut max_cals = 0;
    let mut tmp: i32 = 0;
    for line in lines {
        if line == "" {
            if max_cals < tmp {
                max_cals = tmp;
            }
            tmp = 0;
        }
        else {
            tmp += line.parse::<i32>().unwrap();
        }
    }
    if max_cals < tmp {
        max_cals = tmp;
    }
    println!("{:?}", max_cals)
}
