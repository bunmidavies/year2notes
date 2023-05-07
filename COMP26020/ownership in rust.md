[[COMP26020]]

### definition
- rust's ==ownership system== forms a certain set of restrictions which a programmer must follow
- this allows the compiler to prevent certain memory errors (particularly memory errors where different parts of code make different assumptions about what certain memory locations should be doing)

### owners
- in rust, every value of a reference type has an ==owner==, which is a variable - rust enforces that:
	- every value only has ==one owner==
	- data is deallocated if the owner goes out of scope
	- assignments/function calls pass ownership between variables

### assignment = ownership transfer example
```rust
fn main() {
	let s = String::from("hello");

	let x = s;

	println!("{}",s);
	println!("{}",x);
}
```
- ==attempting to print s will result in an error== - the reason for this is that assignment passes ownership - therefore when `let x = s` was called, ownership was passed over to `x`
- if we move the print s to before `let x = s`, then the code works as expected

### function call = ownership transfer example
```rust
fn main() {
	let s = String::from("hello");

	myprint(s);

	println!("{}",s);
}

fn myprint(s : String) {
	println!("{}",s);
}
```
- attempting to print s in `main()` now also returns an error
- when calling `myprint`, the owernship of `s` is transferred over to `myprint`, and by the end of `myprint`, `s` gets deallocated since its gone out of scope
- one way to fix this is to make `myprint` return `s`, and reassign `s`, i.e. `let s = myprint(s)`
- a simpler way to fix this is through ==borrowing==

### borrowing
- borrowing allows a value to be referred to ==without taking ownership== of it
- rust shows a value being borrowed by prefixing it with `&`
- the ampersand can be used when declaring variables, declaring function arguments, etc.
- we can fix the function call error from the section above as such:
```rust
fn main() {
	let s = String::from("hello");

	myprint(s);

	println!("{}",s);
}

fn myprint(s : & String) {
	println!("{}",s);
}
```
- the ampersand in the signature for `myprint` now indicates that s will be borrowed