[[COMP26020]]

- solidity is a language for writing smart contracts

### smart contracts
- a contract = collection of code + data that exists in a specific address on the Ethereum blockchain. Thus they can roughly be thought as being classes
- the functions of a contract can be thought as messages which can be sent to a specific contract - these functions can be called from different computers
- smart contracts exist on a network, i.e. rather than having a memory address, they have a network address instead
- smart contracts have a ==state== and code associated with it, and are able to send/receive messages
- smart contract constructors can only be called once - calling the constructor for the contract is known as ==deployment==

### indivisible actions
- contract functions can be thought of as singular, indivisible operations - the changes a function makes will only stand if ==the function completely finishes==
- by using the `revert()` method within a function, any changes which have been made will not stand

### message senders
- as mentioned above, calling a function within a smart contract can also be interpreted as whoever called it, sending a message
- the identity of who called the function is cared about within Solidity, unlike in other programming languages where you just call a procedure and thats that
- there is a `msg` variable within contracts, which holds info about who sent a message
==example contract which stores whoever called the contracts constructor in a variable:==
```Solidity
contract test
{
	address owner;

	constructor () public
	{
		owner = msg.sender
	}
}
```

### sending messages
- sending messages to another contract in Solidity just looks like a function call:
```Solidity
remoteContract.function();
```
- address types technically exist for each contract, so for instance instead of declaring an address of a contract of type `B` as just an `address`, it can be defined as type `B` instead
- if a function requires a payment (==cost of running==), this can be included within the function call:
```Solidity
remoteContract.function.value(7 wei)();
```
- `remoteContract.function.value(7 wei);` itself actually returns a function, which is why the additional `()` must be added

### cost of running
- the `msg` variable previously mentioned has two important attributes related to the cost of running a function:
	- `msg.gas` - a payment for the cost of processing a message. This is built into the language, and every instruction costs some amount of gas
	- `msg.value` - a payment for the service represented by the message. Functions will require some cost to run, but they may also require some extra cost (i.e. a product which costs something, but also has processing/shipping fees) - not every instruction may require some value
- to use `msg.value`, a function must be indicated as being `payable` - meanwhile for gas, since every contract function requires gas to perform instructions, the actual amount of gas required is implicit, and depends on how many instructions are in the actual function 
- a massive loop within a function will therefore cost a lot of gas

### keywords
- `view` - a function which doesn't change the state of the contract, just returns a value
- `revert()` - reverts a function meaning it is not completed, returning an error for the message sender