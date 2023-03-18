[[COMP26120]]
as part of [[dynamic programming]]

### edit distance problem
***
![](https://i.imgur.com/57p1Es3.png)


we can define edit distance mathematically:
![](https://i.imgur.com/N0oBzUz.png)


take the example strings `sad` and `made`
we can create a ==2-dimensional== dp array, with the 1st string on the x, and the 2nd string on the y

the value within each cell will represent the ==number of operations== to get from the according string to the other

| |  | m | a | d | e |
|-- | -- | -- | -- | -- | -- |
| | 0 | 1 | 2 | 3 | 4 | 
| s| 1 |  |  |  | | 
| a| 2 |  |  |  | | 
| d| 3 |  |  |  | | 

once this table has been created with the ==known solutions== to the subproblems (i.e. it takes 4 operations to go from `made` to the empty string), the ==final solution== can be built up by building up the table, taking the minimum out of the ==left==,==top==, or ==top-left== value + 1, or + 0 if the current characters were ==equal==

| |  | m | a | d | e |
|-- | -- | -- | -- | -- | -- |
| | 0 | 1 | 2 | 3 | 4 | 
| s| 1 | 1 | 2 | 3 | 4 | 
| a| 2 | 2 | 1 | 2 | 3| 
| d| 3 | 3 | 2 | 1 | 2| 

