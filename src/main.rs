use std::collections::HashMap;
use std::fs::{self, File};
use std::io::{self, BufReader, Read, Write};

fn load_dechetcode() -> HashMap<char, String> {
    // ------ open the file ------
    let file = File::open("dechetCode.json").expect("Failed to open dechetCode.json");
    // ------ create a buffered reader ------
    let reader = BufReader::new(file);
    // ------ return the hashmap created from the JSON (like a python dictionary, but better) ------
    serde_json::from_reader(reader).expect("Failed to parse JSON")
}
fn main() {
    // ------ load the json file ------
    let dechet_code: HashMap<char, String> = load_dechetcode();

    // ------ also create reverse map for much faster decoding ------
    let dechet_code_rev: HashMap<&str, char> = dechet_code.iter().map(|(k, v)| (v.as_str(), *k)).collect();

    // ------ ask for the input file location ------
    println!("Enter the path to the file that must be encoded or decoded: ");
    let mut in_path = String::new();
    loop {
        in_path.clear();
        // input read error
        if io::stdin().read_line(&mut in_path).is_err() {
            println!("Error reading input. Please enter a valid file path: ");
            continue;
        }

        let path = in_path.trim();
        // check for missing input
        if path.is_empty() {
            println!("Input was empty. Please enter a valid file path: ");
            continue;
        }

        // check for invalid file types
        if !path.ends_with(".txt") && !path.ends_with(".edch") {
            println!("Invalid file type. Only .txt and .edch files are supported: ");
            continue;
        }

        // check if file exists and is openable
        if File::open(path).is_err() {
            println!("Could not open file. Please enter a valid file path: ");
            continue;
        }

        in_path = path.to_string();
        break;
    }

    // ------ open the input file and create a buffered reader ------
    let in_file = File::open(&in_path).expect("Failed to open input file");
    let mut in_reader = BufReader::new(in_file);

    // ------ read the input file contents ------
    let mut in_text = String::new();
    in_reader.read_to_string(&mut in_text).expect("Failed to read file");

    // ------ get the choice of the user ------
    println!("Decode an .edch file (0) or encode a .txt file (1)? Write one of the numbers in brackets: ");
    let mut in_choice = String::new();
    let choice: u8;
    loop {
        in_choice.clear();
        // input read error
        if io::stdin().read_line(&mut in_choice).is_err() {
            println!("Error reading input. Please enter 0 or 1: ");
            continue;
        }

        // check if input is even a number
        let num = match in_choice.trim().parse::<u8>() {
            Ok(n) => n,
            Err(_) => {
                println!("Invalid choice. Please enter 0 or 1: ");
                continue;
            }
        };
        
        // check if the number actually corresponds to a valid option
        if num != 0 && num != 1 {
            println!("Invalid choice. Please enter 0 or 1: ");
            continue;
        } else {
            choice = num;
            break;
        }
    }

    // HOHOHO, NOW WE GET TO THE COOL STUFF!
    // ------ check what we have to do ------
    match choice {
        0 => {
            println!("Decoding .edch file...");
            // output path extension replacement
            let out_path = in_path.replace(".edch", ".txt");
            // finally, we go replacin'
            let total = in_text.len() / 7;
            let mut out_text = String::with_capacity(total);
            let mut last_pct: i64 = -1;
            for (i, chunk) in in_text.as_bytes().chunks_exact(7).enumerate() {
                if let Some(&original) = dechet_code_rev.get(std::str::from_utf8(chunk).unwrap()) {
                    out_text.push(original);
                } else {
                    println!("Warning: Unknown code encountered at position {}", i * 7);
                }
                let pct = (i as i64 * 100) / total as i64;
                if pct != last_pct {
                    print!("\r{:.2}% complete", pct as f64);
                    last_pct = pct;
                    io::stdout().flush().ok();
                }
            }
            println!();
            fs::write(out_path, out_text).expect("Failed to write output file");
        }
        1 => {
            println!("Encoding .txt file...");
            // output path extension replacement
            let out_path = in_path.replace(".txt", ".edch");
            // replacin' but the other way around
            let total = in_text.chars().count();
            let mut out_text = String::with_capacity(total * 7);
            let mut last_pct: i64 = -1;
            for (i, letter) in in_text.chars().enumerate() {
                if let Some(code) = dechet_code.get(&letter) {
                    out_text.push_str(code);
                } else {
                    println!("Warning: Unknown character encountered: {}", letter);
                }
                let pct = (i as i64 * 100) / total as i64;
                if pct != last_pct {
                    print!("\r{:.2}% complete", pct as f64);
                    last_pct = pct;
                    io::stdout().flush().ok();
                }
            }
            println!();
            fs::write(out_path, out_text).expect("Failed to write output file");
        }
        _ => unreachable!(),
    }
}