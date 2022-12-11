use std::env;
use std::fs;
use std::ops::Index;
use either::Either;

fn exe_operation(operation: &Vec<Either<String, u128>>, old: &u128) -> u128 {
    let a = operation.index(0);
    let op = operation.index(1);
    let b = operation.index(2);

    let x = match a {
        Either::Left(s) => {
            if s == "old" {
                *old
            } else {
                s.parse::<u128>().unwrap()
            }
        },
        Either::Right(n) => *n,
    };
    let y = match b {
        Either::Left(s) => {
            if s == "old" {
                *old
            } else {
                s.parse::<u128>().unwrap()
            }
        },
        Either::Right(n) => *n,
    };
    let l = op.clone().unwrap_left();
    if *l == *"*" {
        x*y
    } else if *l == *"+" {
        x+y
    } else {
        panic!()
    }
}

fn main() {
    let file_path = "test.txt";

    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    for mut monkey in contents.split("\n\n") {
        while monkey.starts_with(" ") {
            monkey = monkey.strip_prefix(" ").unwrap()
        }

    }

    println!("With text:\n{contents}");
}
