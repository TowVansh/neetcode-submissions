impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        if strs.is_empty() { "~%@!~%@!".to_string() } else { strs.join("~%@!") }
    }

    pub fn decode(s: String) -> Vec<String> {
        if s == "~%@!~%@!" { vec![] } else { s.split("~%@!").map(String::from).collect() }
    }
}